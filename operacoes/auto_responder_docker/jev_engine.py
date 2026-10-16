import os
import json
import urllib.request

TYPESAFE_API_KEY = os.environ.get(
    "TYPESAFE_API_KEY",
    "apikey_278f4d2c99533a740b5bf6020382067c3ac_b34e23a969f2da90dbbf1e2c838fd90b5be744be8f333c43bce904635c26c40c"
)
TYPESAFE_URL = "https://api.typesafe.ai/v1/systemone"

OFFER_PRICES = {
    "vocacao_start_850": {"name": "Vocação Start (Maps + Vitrine One-Page)", "price": 850.0, "micros": 850000000},
    "vocacao_update_980": {"name": "Vocação Update (Reforma Mobile-First)", "price": 980.0, "micros": 980000000},
    "combo_maps_tour360_950": {"name": "Combo Maps + Tour 360° GoPro Max", "price": 950.0, "micros": 950000000},
    "vocacao_maps_450": {"name": "Vocação Presença no Maps (Blindagem)", "price": 450.0, "micros": 450000000}
}

def qualify_with_jev(lead_name: str, message_text: str = "", context: str = "") -> dict:
    lead_info = {
        "nome": lead_name,
        "mensagem_lead": message_text,
        "contexto": context or f"Empresa ou clínica localizada em Sorocaba/SP em prospecção pela Vocação Comunicação & Marketing."
    }

    questions = {
        "oferta_principal": {
            "type": "choice",
            "instructions": "Qual oferta da esteira oficial da Vocação Comunicação & Marketing tem o melhor fit imediato para este lead?",
            "criteria": {
                "vocacao_start_850": "Vocação Start (R$ 850 - Carro-Chefe): Maps Otimizado + Vitrine One-Page em subdomínio seguro em 7 dias (para empresas sem site, com site quebrado ou dependentes de linktree/whatsapp solto)",
                "vocacao_update_980": "Vocação Update (R$ 980): Reforma mobile-first ultra-rápida (<0.5s) em 5 dias (para empresas que já têm site antigo, pesado ou desatualizado)",
                "combo_maps_tour360_950": "Combo Maps + Tour 360° (R$ 950): Otimização do Maps + Tour Virtual 360° GoPro Max Street View (para locais onde o ambiente físico é o maior diferencial de venda: clínicas, studios de pilates, escolas)",
                "vocacao_maps_450": "Vocação Presença no Maps (R$ 450): Blindagem, reivindicação e organização de fotos/WhatsApp na ficha do Google Maps (para negócios que precisam apenas regularizar o mapa básico)"
            }
        },
        "perfil_maturidade": {
            "type": "choice",
            "instructions": "Qual é a situação atual da presença digital do lead?",
            "criteria": {
                "sem_presenca": "Invisível ou sem site: apenas redes sociais ou ficha do Google Maps abandonada",
                "site_legado": "Possui site existente, mas é antigo, lento, não responsivo ou sem botão direto para WhatsApp",
                "espaco_ambiente": "Possui espaço físico atraente que se beneficiaria muito de tour virtual 360° no Street View",
                "regularizacao_maps": "Empresa consolidada no mundo real mas com ficha do Google Maps desatualizada ou não reivindicada"
            }
        },
        "perda_conversao_local": {
            "type": "noul",
            "instructions": "O lead apresenta forte probabilidade de estar perdendo clientes da região/bairro para concorrentes devido a falhas na presença digital no Google Maps?"
        },
        "urgencia_presenca": {
            "type": "score",
            "instructions": "Qual é o nível de urgência da estruturação digital deste lead?",
            "criteria": [
                "Baixa: Já tem presença razoável e canais de conversão ativos",
                "Média: Presença parcial com falhas óbvias de conversão no mobile",
                "Crítica: Sem vitrine funcional, sem botão de WhatsApp ou ficha do Maps queimando clientes no bairro"
            ]
        }
    }

    payload = {
        "model": "jev-latest",
        "state": lead_info,
        "questions": questions
    }

    req = urllib.request.Request(
        TYPESAFE_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TYPESAFE_API_KEY}",
            "User-Agent": "Vocacao-AutoResponder-Jev/2.0"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            ans = data.get("answers", {})
            oferta_key = ans.get("oferta_principal", {}).get("choice", "vocacao_start_850")
            oferta_meta = OFFER_PRICES.get(oferta_key, OFFER_PRICES["vocacao_start_850"])

            return {
                "status": "success",
                "oferta_key": oferta_key,
                "oferta_nome": oferta_meta["name"],
                "oferta_preco": oferta_meta["price"],
                "oferta_micros": oferta_meta["micros"],
                "oferta_confianca": ans.get("oferta_principal", {}).get("confidence", 0.85),
                "perfil_maturidade": ans.get("perfil_maturidade", {}).get("choice", "sem_presenca"),
                "perda_conversao_local": ans.get("perda_conversao_local", {}).get("noul", 0.75),
                "urgencia_score": ans.get("urgencia_presenca", {}).get("score", 1),
                "raw": ans
            }
    except Exception as e:
        print(f"[!] Erro Jev System One: {e}. Usando oferta padrão Vocação Start.")
        def_meta = OFFER_PRICES["vocacao_start_850"]
        return {
            "status": "fallback",
            "oferta_key": "vocacao_start_850",
            "oferta_nome": def_meta["name"],
            "oferta_preco": def_meta["price"],
            "oferta_micros": def_meta["micros"],
            "oferta_confianca": 0.8,
            "perfil_maturidade": "sem_presenca",
            "perda_conversao_local": 0.7,
            "urgencia_score": 1,
            "raw": {}
        }
