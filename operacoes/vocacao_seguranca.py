"""
vocacao_seguranca.py — Guardas compartilhados de disparo da Vocação.

Centraliza as regras que a auditoria de outubro/2026 encontrou duplicadas (ou
ausentes) nos scripts de prospecção:

  P3 — encoding: força UTF-8 na saída padrão e detecta texto corrompido
       (mojibake) antes de qualquer envio;
  P4 — telefonia: só celular com DDD válido entra na fila de WhatsApp;
  P4 — e-mail: valida sintaxe e existência de registro MX antes do SMTP;
  P4 — cadência: bloqueia disparos fora das Janelas de Ouro e em fim de semana.

Uso típico em um disparador:

    from vocacao_seguranca import pode_disparar_whatsapp, texto_corrompido

    ok, motivo = pode_disparar_whatsapp(numero)
    if not ok:
        print(f"[SKIP] {numero}: {motivo}")
        return

Nada aqui envia mensagem: são apenas funções de decisão, para que o mesmo
critério valha para todos os canais.
"""

from __future__ import annotations

import os
import re
import sys
import unicodedata
from datetime import datetime

__all__ = [
    "forcar_utf8",
    "apenas_digitos",
    "normalizar_telefone",
    "is_mobile_phone",
    "validar_email_sintaxe",
    "validar_email_mx",
    "pode_enviar_email",
    "texto_corrompido",
    "checar_janela",
    "pode_disparar_whatsapp",
]


# ---------------------------------------------------------------------------
# P3 — encoding
# ---------------------------------------------------------------------------
def forcar_utf8() -> None:
    """Garante que stdout/stderr não explodam com acentos no console Windows."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass


forcar_utf8()


# Caracteres que aparecem quando um texto UTF-8 é lido como Windows-1252.
# Exemplos reais registrados na auditoria: "Olǭ!", "vocǦs", "regiǜo".
_MOJIBAKE_CHARS = re.compile("[ǭǦǜǩǪǬȩ\uFFFD]")
_MOJIBAKE_SEQUENCES = re.compile(r"(Ã[\u0080-\u00BF]|â€[\u0090-\u009F\u2018-\u201D])")


def texto_corrompido(texto: str) -> bool:
    """True quando o texto carrega marcas típicas de encoding quebrado."""
    if not texto:
        return False
    if _MOJIBAKE_CHARS.search(texto):
        return True
    return bool(_MOJIBAKE_SEQUENCES.search(texto))


# ---------------------------------------------------------------------------
# P4 — telefonia
# ---------------------------------------------------------------------------
DDD_VALIDOS = {
    11, 12, 13, 14, 15, 16, 17, 18, 19,
    21, 22, 24, 27, 28,
    31, 32, 33, 34, 35, 37, 38,
    41, 42, 43, 44, 45, 46, 47, 48, 49,
    51, 53, 54, 55,
    61, 62, 63, 64, 65, 66, 67, 68, 69,
    71, 73, 74, 75, 77, 79,
    81, 82, 83, 84, 85, 86, 87, 88, 89,
    91, 92, 93, 94, 95, 96, 97, 98, 99,
}


def apenas_digitos(valor) -> str:
    return re.sub(r"\D", "", str(valor or ""))


def normalizar_telefone(telefone) -> str:
    """Devolve o número só com dígitos, no formato 55DDDNUMERO quando possível."""
    digitos = apenas_digitos(telefone)
    if not digitos:
        return ""
    if digitos.startswith("0055"):
        digitos = digitos[4:]
    if not digitos.startswith("55"):
        digitos = "55" + digitos
    return digitos


def is_mobile_phone(telefone) -> bool:
    """
    Aceita apenas celular brasileiro: DDD válido + 9 + 8 dígitos.

    Rejeita fixos de 8 dígitos (ex.: 15 3233-XXXX), números sem DDD,
    DDDs inexistentes e sequências repetidas (ex.: 99999999999).
    """
    digitos = apenas_digitos(telefone)
    if digitos.startswith("0055"):
        digitos = digitos[4:]
    if digitos.startswith("55") and len(digitos) in (12, 13):
        digitos = digitos[2:]

    if len(digitos) != 11:
        return False

    ddd = int(digitos[:2])
    if ddd not in DDD_VALIDOS:
        return False

    if digitos[2] != "9":
        return False

    assinante = digitos[3:]
    # 9 0000-0000 e repetições do mesmo dígito não são linhas reais.
    if assinante == "00000000" or len(set(assinante)) == 1:
        return False

    return True


# ---------------------------------------------------------------------------
# P4 — e-mail (sintaxe + MX)
# ---------------------------------------------------------------------------
_EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$")

_MX_CACHE: dict[str, tuple[bool, str]] = {}


def validar_email_sintaxe(email) -> bool:
    return bool(_EMAIL_RE.match(str(email or "").strip()))


def _mx_via_dnspython(dominio: str) -> tuple[bool, str] | None:
    try:
        import dns.resolver  # type: ignore
    except Exception:
        return None
    try:
        respostas = dns.resolver.resolve(dominio, "MX", lifetime=4)
        registros = sorted(str(r.exchange).rstrip(".") for r in respostas)
        if not registros:
            return False, "domínio sem registro MX"
        return True, f"MX {', '.join(registros[:3])}"
    except Exception as exc:  # NXDOMAIN, NoAnswer, timeout...
        return False, f"sem MX válido ({type(exc).__name__})"


def _mx_via_nslookup(dominio: str) -> tuple[bool, str] | None:
    import shutil
    import subprocess

    if not shutil.which("nslookup"):
        return None
    try:
        saida = subprocess.run(
            ["nslookup", "-type=mx", dominio],
            capture_output=True,
            text=True,
            timeout=8,
        ).stdout
    except Exception:
        return None

    if re.search(r"MX preference|mail exchanger", saida, re.IGNORECASE):
        return True, "MX confirmado via nslookup"
    # Mensagens de NXDOMAIN variam com o idioma do Windows; o prefixo "***"
    # e o texto entre aspas são estáveis o suficiente para o descarte.
    if re.search(r"\*\*\*|NXDOMAIN|Non-existent|inexistente", saida, re.IGNORECASE):
        return False, "domínio sem MX (NXDOMAIN)"
    return None


def _dominio_resolve(dominio: str) -> tuple[bool, str]:
    """Último recurso sem dnspython/nslookup: pelo menos descarta NXDOMAIN."""
    import socket

    try:
        socket.getaddrinfo(dominio, None)
        return True, "domínio resolve, MX não confirmado (instale dnspython)"
    except Exception:
        return False, "domínio não resolve (provável endereço inexistente)"


def validar_email_mx(email, usar_cache: bool = True) -> tuple[bool, str]:
    """
    Verifica sintaxe e existência de MX do domínio.

    Retorna (ok, motivo). Quando não há dnspython nem nslookup disponíveis,
    devolve (True, "MX não verificado ...") para não travar a operação — mas o
    motivo deixa claro que a checagem não aconteceu.
    """
    endereco = str(email or "").strip().lower()
    if not validar_email_sintaxe(endereco):
        return False, "sintaxe de e-mail inválida"

    dominio = endereco.rsplit("@", 1)[1]
    if usar_cache and dominio in _MX_CACHE:
        return _MX_CACHE[dominio]

    resultado = _mx_via_dnspython(dominio)
    if resultado is None:
        resultado = _mx_via_nslookup(dominio)
    if resultado is None:
        resultado = _dominio_resolve(dominio)

    if usar_cache:
        _MX_CACHE[dominio] = resultado
    return resultado


def pode_enviar_email(email) -> tuple[bool, str]:
    """Decisão única para disparos B2B: sintaxe + MX."""
    return validar_email_mx(email)


# ---------------------------------------------------------------------------
# P4 — janela de cadência
# ---------------------------------------------------------------------------
def _permitir_fora_da_janela() -> bool:
    return os.environ.get("VOCACAO_PERMITIR_FORA_JANELA", "").strip().lower() in {
        "1", "true", "sim", "yes", "on",
    }


def checar_janela(dt: datetime | None = None) -> tuple[bool, str]:
    """Usa o motor oficial de janelas; cai num espelho local se o import falhar."""
    if _permitir_fora_da_janela():
        return True, "janela ignorada por VOCACAO_PERMITIR_FORA_JANELA=1"

    momento = dt or datetime.now()
    try:
        from CONFIG_MOTOR_DISPARO_VOCACOES_START import is_in_golden_window

        return is_in_golden_window(momento)
    except Exception:
        pass

    # Espelho da regra oficial (mantido apenas como rede de segurança).
    if momento.weekday() >= 5:
        return False, "Fim de semana: disparos comerciais congelados."
    hora = momento.time()
    if (hora.hour, hora.minute) >= (10, 0) and (hora.hour, hora.minute) <= (11, 45):
        return True, "Dentro da Janela de Ouro (10h00-11h45)."
    if (hora.hour, hora.minute) >= (14, 15) and (hora.hour, hora.minute) <= (16, 45):
        return True, "Dentro da Janela de Ouro (14h15-16h45)."
    return False, f"Fora da Janela de Ouro ({hora.strftime('%H:%M')})."


def pode_disparar_whatsapp(
    telefone,
    texto: str | None = None,
    dt: datetime | None = None,
    verificar_janela: bool = True,
) -> tuple[bool, str]:
    """
    Guarda completa antes de chamar a Evolution API.

    Ordem: celular válido -> texto não corrompido -> janela de cadência.
    """
    if not is_mobile_phone(telefone):
        return False, "número não é celular válido (fixo/DDD inválido/sem 9º dígito)"

    if texto and texto_corrompido(texto):
        return False, "texto com encoding corrompido (mojibake)"

    if verificar_janela:
        return checar_janela(dt)

    return True, "ok"


if __name__ == "__main__":
    # Autoteste rápido: python vocacao_seguranca.py
    casos = {
        "5515997502210": True,
        "15997502210": True,
        "551532331234": False,   # fixo
        "1532331234": False,     # fixo sem DDD
        "551599750221": False,   # 12 dígitos com 55 já removido -> curto
        "5510097502210": False,  # DDD inválido
        "5515999999999": False,  # assinante repetido
    }
    falhas = 0
    for numero, esperado in casos.items():
        obtido = is_mobile_phone(numero)
        marca = "ok" if obtido == esperado else "FALHOU"
        if obtido != esperado:
            falhas += 1
        print(f"[{marca}] {numero}: esperado={esperado} obtido={obtido}")
    print("mojibake 'Olǭ!':", texto_corrompido("Olǭ!"))
    print("texto normal:", texto_corrompido("Olá, tudo bem?"))
    sys.exit(1 if falhas else 0)
