"""
verificar_catalogo.py — auditoria automática do catálogo de ofertas (P5).

Compara a fonte única em Python (`ofertas_catalogo.py`), o documento humano
(`references/matriz-ofertas-niveis.md`) e os motores do Jev que ainda tenham
catálogo embutido. Sai com código 1 se algo divergir — serve para rodar antes
de qualquer disparo em lote.

Uso:
    python verificar_catalogo.py
    python verificar_catalogo.py --fix-doc   # regenera apenas a tabela do MD
"""

from __future__ import annotations

import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from ofertas_catalogo import OFERTAS, ORDEM_OFERTAS, reais

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOC = os.path.join(BASE_DIR, "references", "matriz-ofertas-niveis.md")
ENGINES = [
    os.path.join(BASE_DIR, "auto_responder_docker", "jev_engine.py"),
]

# Preços que ainda podem aparecer em textos históricos, mas não no catálogo.
PRECOS_PROIBIDOS = {"150", "180", "250", "297", "350", "397", "497", "697", "797"}


def falhas_no_documento() -> list[str]:
    if not os.path.exists(DOC):
        return [f"documento ausente: {DOC}"]

    texto = open(DOC, encoding="utf-8").read()
    problemas = []
    for chave in ORDEM_OFERTAS:
        oferta = OFERTAS[chave]
        valor = reais(oferta["preco"])
        if valor not in texto:
            problemas.append(f"{chave}: preço {valor} não aparece na matriz")
        nome_curto = oferta["nome"].split(" (")[0]
        if nome_curto not in texto:
            problemas.append(f"{chave}: nome '{nome_curto}' não aparece na matriz")
    return problemas


def falhas_nos_motores() -> list[str]:
    problemas = []
    for caminho in ENGINES:
        if not os.path.exists(caminho):
            problemas.append(f"motor ausente: {caminho}")
            continue
        fonte = open(caminho, encoding="utf-8").read()
        if "ofertas_catalogo" not in fonte:
            problemas.append(f"{os.path.basename(caminho)}: não importa o catálogo único")
        for proibido in PRECOS_PROIBIDOS:
            if re.search(rf"R\$\s*{proibido}\b", fonte):
                problemas.append(
                    f"{os.path.basename(caminho)}: cita preço fora da esteira (R$ {proibido})"
                )
    return problemas


def main() -> int:
    problemas = falhas_no_documento() + falhas_nos_motores()
    if problemas:
        print("CATÁLOGO INCONSISTENTE:")
        for p in problemas:
            print(f"  - {p}")
        return 1

    print(f"Catálogo consistente: {len(OFERTAS)} ofertas conferidas em {DOC}.")
    for chave in ORDEM_OFERTAS:
        print(f"  {chave:<26} {reais(OFERTAS[chave]['preco'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
