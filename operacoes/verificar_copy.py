"""
verificar_copy.py — trava de qualidade da copy (P2 da auditoria).

Falha quando algum script de disparo contém:
  - o jargão proibido "se fizer sentido";
  - acusações técnicas não confirmadas ("faltam fotos", "não tem fotos",
    "sem fotos", "@gmail.com", "sem site", "não tem WhatsApp");
  - promessa de resultado garantido ("garantimos", "100% garantido").

Rode antes de qualquer lote:  python verificar_copy.py
"""

from __future__ import annotations

import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Só os scripts que montam a mensagem enviada ao lead entram na varredura.
# Seed de painel (gerar_painel_100leads) e catálogo do Jev descrevem o lead,
# não são copy de abordagem — ficam de fora de propósito.
PREFIXO_ALVO = "disparador_"

PADROES = {
    "jargão 'se fizer sentido'": re.compile(r"se fizer sentido", re.IGNORECASE),
    "acusação 'faltam fotos'": re.compile(r"faltam?\s+fotos", re.IGNORECASE),
    "acusação 'não tem fotos'": re.compile(r"n[ãa]o\s+t[eê]m?\s+fotos", re.IGNORECASE),
    "acusação 'sem fotos'": re.compile(r"\bsem\s+fotos\b", re.IGNORECASE),
    "acusação '@gmail.com'": re.compile(r"@gmail\.com", re.IGNORECASE),
    "acusação 'sem site'": re.compile(r"\bsem\s+site\b", re.IGNORECASE),
    "acusação 'não tem WhatsApp'": re.compile(r"n[ãa]o\s+t[eê]m?\s+whatsapp", re.IGNORECASE),
    "promessa 'garantido'": re.compile(r"\bgarantid[oa]s?\b", re.IGNORECASE),
}


def varrer() -> list[str]:
    problemas = []
    for nome in sorted(os.listdir(BASE_DIR)):
        if not (nome.endswith(".py") and nome.startswith(PREFIXO_ALVO)):
            continue
        caminho = os.path.join(BASE_DIR, nome)
        for numero, linha in enumerate(open(caminho, encoding="utf-8", errors="replace"), 1):
            if linha.lstrip().startswith("#"):
                continue
            for rotulo, padrao in PADROES.items():
                if padrao.search(linha):
                    problemas.append(f"{nome}:{numero}  {rotulo}")
    return problemas


def main() -> int:
    problemas = varrer()
    if not problemas:
        print("Copy limpa: nenhum termo proibido encontrado nos scripts de operações.")
        return 0

    print("COPY COM TERMOS PROIBIDOS (corrija antes de disparar):")
    for problema in problemas:
        print(f"  - {problema}")
    print(f"\nTotal: {len(problemas)} ocorrência(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
