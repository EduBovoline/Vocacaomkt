"""
verificar_fila_disparo.py — pré-voo obrigatório das filas de prospecção (P4).

Lê um JSON de leads (lista de objetos com `name`/`phone`/`number`/`email`),
aplica as mesmas regras usadas no envio e mostra o que entraria e o que seria
descartado. Não envia nada e não altera arquivos.

Uso:
    python verificar_fila_disparo.py leads_ouro_fila_disparo.json
    python verificar_fila_disparo.py leads.json --checar-mx --strict
    python verificar_fila_disparo.py leads.json --json relatorio.json

Saída: resumo no terminal; com --json grava o relatório completo.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

from vocacao_seguranca import is_mobile_phone, normalizar_telefone, validar_email_mx

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def carregar(caminho: str) -> list[dict]:
    with open(caminho, encoding="utf-8") as f:
        dados = json.load(f)
    if isinstance(dados, dict):
        # aceita {"leads": [...]}, {"queue": [...]} ou {"fila": [...]}
        for chave in ("leads", "queue", "fila", "items"):
            if isinstance(dados.get(chave), list):
                return dados[chave]
        return [dados]
    if not isinstance(dados, list):
        raise ValueError("JSON precisa ser uma lista de leads ou um objeto com 'leads'/'fila'")
    return dados


def telefone_do(lead: dict):
    return lead.get("number") or lead.get("phone") or lead.get("telefone") or lead.get("whatsapp")


def carregar_contatados() -> set[str]:
    contatados: set[str] = set()
    for nome in ("delivered_leads.json",):
        caminho = os.path.join(BASE_DIR, nome)
        if not os.path.exists(caminho):
            continue
        try:
            dados = json.load(open(caminho, encoding="utf-8"))
        except Exception:
            continue
        if isinstance(dados, dict):
            contatados.update(str(k) for k in dados)
        elif isinstance(dados, list):
            for item in dados:
                if isinstance(item, dict):
                    numero = telefone_do(item)
                    if numero:
                        contatados.add(normalizar_telefone(numero))
    return contatados


def analisar(leads: list[dict], checar_mx: bool) -> dict:
    contatados = carregar_contatados()
    vistos: set[str] = set()
    relatorio = {
        "total": len(leads),
        "validos": [],
        "telefone_invalido": [],
        "duplicados": [],
        "ja_contatados": [],
        "email_sem_mx": [],
        "sem_contato": [],
    }

    for lead in leads:
        nome = lead.get("name") or lead.get("nome") or "(sem nome)"
        telefone = telefone_do(lead)
        email = lead.get("email") or lead.get("e-mail")

        if not telefone and not email:
            relatorio["sem_contato"].append({"nome": nome, "motivo": "sem telefone e sem e-mail"})
            continue

        if telefone:
            normalizado = normalizar_telefone(telefone)
            if not is_mobile_phone(telefone):
                relatorio["telefone_invalido"].append(
                    {"nome": nome, "telefone": str(telefone), "motivo": "não é celular válido"}
                )
                continue
            if normalizado in vistos:
                relatorio["duplicados"].append({"nome": nome, "telefone": normalizado})
                continue
            if normalizado in contatados:
                relatorio["ja_contatados"].append({"nome": nome, "telefone": normalizado})
                continue
            vistos.add(normalizado)

        if checar_mx and email:
            ok, motivo = validar_email_mx(email)
            if not ok:
                relatorio["email_sem_mx"].append(
                    {"nome": nome, "email": str(email), "motivo": motivo}
                )
                continue

        relatorio["validos"].append({"nome": nome, "telefone": telefone, "email": email})

    relatorio["resumo"] = {
        "validos": len(relatorio["validos"]),
        "telefone_invalido": len(relatorio["telefone_invalido"]),
        "duplicados": len(relatorio["duplicados"]),
        "ja_contatados": len(relatorio["ja_contatados"]),
        "email_sem_mx": len(relatorio["email_sem_mx"]),
        "sem_contato": len(relatorio["sem_contato"]),
    }
    return relatorio


def imprimir(relatorio: dict) -> None:
    r = relatorio["resumo"]
    print("=" * 62)
    print(f"PRÉ-VOO DA FILA — {relatorio['total']} registros lidos")
    print("=" * 62)
    print(f"  prontos para disparo .......... {r['validos']}")
    print(f"  telefone fixo/inválido ....... {r['telefone_invalido']}")
    print(f"  duplicados na própria fila ... {r['duplicados']}")
    print(f"  já contatados antes .......... {r['ja_contatados']}")
    print(f"  e-mail sem MX ................ {r['email_sem_mx']}")
    print(f"  sem telefone e sem e-mail .... {r['sem_contato']}")

    for titulo, chave in (
        ("TELEFONE FIXO/INVÁLIDO (NÃO ENVIAR)", "telefone_invalido"),
        ("DUPLICADOS", "duplicados"),
        ("JÁ CONTATADOS", "ja_contatados"),
        ("E-MAIL SEM MX (NÃO ENVIAR)", "email_sem_mx"),
        ("SEM CONTATO", "sem_contato"),
    ):
        itens = relatorio[chave]
        if not itens:
            continue
        print(f"\n{titulo}:")
        for item in itens[:20]:
            detalhe = item.get("telefone") or item.get("email") or ""
            print(f"  - {item['nome']}: {detalhe} ({item.get('motivo', '')})")
        if len(itens) > 20:
            print(f"  ... e mais {len(itens) - 20}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Pré-voo de fila de disparo")
    parser.add_argument("arquivo", help="JSON com a lista de leads")
    parser.add_argument("--checar-mx", action="store_true", help="consulta DNS MX dos e-mails")
    parser.add_argument("--json", dest="saida", help="grava o relatório completo neste arquivo")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="sai com código 1 se houver qualquer registro descartado",
    )
    args = parser.parse_args()

    try:
        leads = carregar(args.arquivo)
    except Exception as exc:
        print(f"[ERRO] Não foi possível ler {args.arquivo}: {exc}")
        return 2

    relatorio = analisar(leads, args.checar_mx)
    imprimir(relatorio)

    if args.saida:
        with open(args.saida, "w", encoding="utf-8") as f:
            json.dump(relatorio, f, ensure_ascii=False, indent=2)
        print(f"\nRelatório gravado em {args.saida}")

    if args.strict and any(
        relatorio["resumo"][k]
        for k in ("telefone_invalido", "duplicados", "ja_contatados", "email_sem_mx", "sem_contato")
    ):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
