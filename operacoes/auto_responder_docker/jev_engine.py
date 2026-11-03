import os
import json
import urllib.request

# P5 (auditoria): catálogo único. O módulo fica em operacoes/ no host e é
# montado em /app/ofertas_catalogo.py pelo docker-compose.
try:
    from ofertas_catalogo import (
        OFERTAS,
        OFERTA_PADRAO,
        PERFIS_MATURIDADE,
        URGENCIA_CRITERIOS,
        criterios_jev,
        obter,
    )
except ImportError:  # execução direta a partir de auto_responder_docker/
    import sys

    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from ofertas_catalogo import (
        OFERTAS,
        OFERTA_PADRAO,
        PERFIS_MATURIDADE,
        URGENCIA_CRITERIOS,
        criterios_jev,
        obter,
    )

TYPESAFE_API_KEY = os.environ.get(
    "TYPESAFE_API_KEY",
    "apikey_278f4d2c99533a740b5bf6020382067c3ac_b34e23a969f2da90dbbf1e2c838fd90b5be744be8f333c43bce904635c26c40c"
)
TYPESAFE_URL = "https://api.typesafe.ai/v1/systemone"

# Compatibilidade com quem já importa OFFER_PRICES daqui.
OFFER_PRICES = {
    chave: {"name": dados["nome"], "price": dados["preco"], "micros": dados["micros"]}
    for chave, dados in OFERTAS.items()
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
            "criteria": criterios_jev(),
        },
        "perfil_maturidade": {
            "type": "choice",
            "instructions": "Qual é a situação atual da presença digital do lead?",
            "criteria": PERFIS_MATURIDADE,
        },
        "perda_conversao_local": {
            "type": "noul",
            "instructions": "O lead apresenta forte probabilidade de estar perdendo clientes da região/bairro para concorrentes devido a falhas na presença digital no Google Maps?"
        },
        "urgencia_presenca": {
            "type": "score",
            "instructions": "Qual é o nível de urgência da estruturação digital deste lead?",
            "criteria": URGENCIA_CRITERIOS,
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
            oferta_key = ans.get("oferta_principal", {}).get("choice", OFERTA_PADRAO)
            oferta_meta = obter(oferta_key)

            return {
                "status": "success",
                "oferta_key": oferta_key,
                "oferta_nome": oferta_meta["nome"],
                "oferta_preco": oferta_meta["preco"],
                "oferta_micros": oferta_meta["micros"],
                "oferta_confianca": ans.get("oferta_principal", {}).get("confidence", 0.85),
                "perfil_maturidade": ans.get("perfil_maturidade", {}).get("choice", "sem_presenca"),
                "perda_conversao_local": ans.get("perda_conversao_local", {}).get("noul", 0.75),
                "urgencia_score": ans.get("urgencia_presenca", {}).get("score", 1),
                "raw": ans
            }
    except Exception as e:
        print(f"[!] Erro Jev System One: {e}. Usando oferta padrão {OFERTA_PADRAO}.")
        def_meta = obter(OFERTA_PADRAO)
        return {
            "status": "fallback",
            "oferta_key": OFERTA_PADRAO,
            "oferta_nome": def_meta["nome"],
            "oferta_preco": def_meta["preco"],
            "oferta_micros": def_meta["micros"],
            "oferta_confianca": 0.8,
            "perfil_maturidade": "sem_presenca",
            "perda_conversao_local": 0.7,
            "urgencia_score": 1,
            "raw": {}
        }
