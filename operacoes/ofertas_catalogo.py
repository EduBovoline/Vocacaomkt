"""
ofertas_catalogo.py — Fonte única do catálogo de ofertas da Vocação (P5).

Antes desta unificação, `jev_engine.py` (auto-responder) e `jev_classifier.py`
(plugin/skill) tinham critérios escritos à mão, com redações e escopos que
divergiam entre si — o que fazia o CRM, o PDF e a mensagem citarem produtos
diferentes para o mesmo lead.

Agora todo mundo lê daqui. A versão humana deste catálogo está em
`references/matriz-ofertas-niveis.md`; o script `verificar_catalogo.py`
confere se os dois continuam batendo.

Regra de manutenção: mudou preço, escopo ou critério? Mude AQUI e rode
`python verificar_catalogo.py`.
"""

from __future__ import annotations

# Chave -> dados oficiais. "micros" segue o padrão do Twenty CRM (valor * 1e6).
OFERTAS: dict[str, dict] = {
    "vocacao_maps_450": {
        "nome": "Vocação Presença no Maps",
        "preco": 450.0,
        "micros": 450_000_000,
        "prazo": "48h a 7 dias",
        "escopo": (
            "Reivindicação da ficha no nome do dono, dados e categorias corretos, "
            "link direto de WhatsApp e fotos tratadas."
        ),
        "nao_inclui": "Fotos novas presenciais e site.",
        "criterio_jev": (
            "Vocação Presença no Maps (R$ 450): blindagem, reivindicação e organização "
            "de fotos/WhatsApp na ficha do Google Maps (para negócios que precisam "
            "apenas regularizar o mapa básico)"
        ),
    },
    "tour_360_650": {
        "nome": "Tour Virtual 360° Avulso (Street View)",
        "preco": 650.0,
        "micros": 650_000_000,
        "prazo": "3 a 5 dias",
        "escopo": (
            "Captura presencial com GoPro Max (5 a 7 pontos), costura técnica e "
            "publicação no Google Street View oficial."
        ),
        "nao_inclui": "Mexer no site ou na ficha do Maps.",
        "criterio_jev": None,  # oferta avulsa; o Jev só a sugere via combo
    },
    "vocacao_start_850": {
        "nome": "Vocação Start (Maps + Vitrine One-Page)",
        "preco": 850.0,
        "micros": 850_000_000,
        "prazo": "7 dias úteis",
        "escopo": (
            "Google Maps otimizado + Vitrine Digital One-Page em subdomínio seguro "
            "(cliente.vocacao.digital) com botão direto de WhatsApp."
        ),
        "nao_inclui": "E-commerce com carrinho, blog e área de membros.",
        "criterio_jev": (
            "Vocação Start (R$ 850 - Carro-Chefe): Maps Otimizado + Vitrine One-Page em "
            "subdomínio seguro em 7 dias (para empresas sem site, com site quebrado ou "
            "dependentes de linktree/whatsapp solto)"
        ),
    },
    "combo_maps_tour360_950": {
        "nome": "Combo Maps + Tour 360° GoPro Max",
        "preco": 950.0,
        "micros": 950_000_000,
        "prazo": "7 dias úteis",
        "escopo": (
            "Otimização completa do Google Maps + Tour Virtual 360° GoPro Max "
            "publicado no Google Street View."
        ),
        "nao_inclui": "Criação de site.",
        "criterio_jev": (
            "Combo Maps + Tour 360° (R$ 950): Otimização do Maps + Tour Virtual 360° "
            "GoPro Max Street View (para locais onde o ambiente físico é o maior "
            "diferencial de venda: clínicas, studios de pilates, escolas)"
        ),
    },
    "vocacao_update_980": {
        "nome": "Vocação Update (Reforma Mobile-First)",
        "preco": 980.0,
        "micros": 980_000_000,
        "prazo": "5 dias úteis",
        "escopo": (
            "Reforma e modernização de site existente: carregamento abaixo de 0,5s, "
            "mobile-first e fluxo direto de pedido para o WhatsApp."
        ),
        "nao_inclui": "Reescrita do zero ou fotos presenciais.",
        "criterio_jev": (
            "Vocação Update (R$ 980): Reforma mobile-first ultra-rápida (<0.5s) em 5 dias "
            "(para empresas que já têm site antigo, pesado ou desatualizado)"
        ),
    },
}

# Ordem de apresentação nas mensagens e relatórios (do menor para o maior ticket).
ORDEM_OFERTAS = [
    "vocacao_maps_450",
    "tour_360_650",
    "vocacao_start_850",
    "combo_maps_tour360_950",
    "vocacao_update_980",
]

# Oferta padrão quando o classificador falha.
OFERTA_PADRAO = "vocacao_start_850"

# Perfis de maturidade usados pelo Jev (mantidos estáveis para o CRM).
PERFIS_MATURIDADE = {
    "sem_presenca": "Invisível ou sem site: apenas redes sociais ou ficha do Google Maps abandonada",
    "site_legado": "Possui site existente, mas é antigo, lento, não responsivo ou sem botão direto para WhatsApp",
    "espaco_ambiente": "Possui espaço físico atraente que se beneficiaria muito de tour virtual 360° no Street View",
    "regularizacao_maps": "Empresa consolidada no mundo real mas com ficha do Google Maps desatualizada ou não reivindicada",
}

URGENCIA_CRITERIOS = [
    "Baixa: Já tem presença razoável e canais de conversão ativos",
    "Média: Presença parcial com falhas óbvias de conversão no mobile",
    "Crítica: Sem vitrine funcional, sem botão de WhatsApp ou ficha do Maps queimando clientes no bairro",
]


def criterios_jev() -> dict[str, str]:
    """Critérios de escolha no formato `choice` aceito pela API do Jev."""
    return {
        chave: dados["criterio_jev"]
        for chave, dados in OFERTAS.items()
        if dados.get("criterio_jev")
    }


def obter(chave: str) -> dict:
    """Dados de uma oferta; cai na padrão quando a chave vem desconhecida."""
    return OFERTAS.get(chave, OFERTAS[OFERTA_PADRAO])


def micros(chave: str) -> int:
    return int(obter(chave)["micros"])


def preco(chave: str) -> float:
    return float(obter(chave)["preco"])


def reais(valor: float) -> str:
    """Formata 850.0 como 'R$ 850,00' (padrão pt-BR)."""
    inteiro, centavos = f"{valor:.2f}".split(".")
    grupos = []
    while len(inteiro) > 3:
        grupos.insert(0, inteiro[-3:])
        inteiro = inteiro[:-3]
    grupos.insert(0, inteiro)
    return f"R$ {'.'.join(grupos)},{centavos}"


def tabela_markdown() -> str:
    linhas = [
        "| Solução | O que inclui (escopo fechado) | O que NÃO inclui | Ticket | Prazo |",
        "| :--- | :--- | :--- | ---: | :--- |",
    ]
    for chave in ORDEM_OFERTAS:
        o = OFERTAS[chave]
        linhas.append(
            f"| **{o['nome']}** | {o['escopo']} | {o['nao_inclui']} | "
            f"**{reais(o['preco'])}** | {o['prazo']} |"
        )
    return "\n".join(linhas)


if __name__ == "__main__":
    print(tabela_markdown())
