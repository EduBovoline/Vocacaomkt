import os
import json
import re
import requests

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()

def analyze_and_generate_reply(message_text: str, sender_name: str = "", chat_history: list = None) -> dict:
    """
    Analisa a mensagem do lead considerando o HISTÓRICO COMPLETO da conversa.
    Gera uma resposta consultiva em nome de Eduardo (Vocação), focando em escuta ativa (80%)
    e NUNCA empurrando diagnósticos ou ofertas prematuras.
    """
    api_key = os.environ.get("GEMINI_API_KEY", GEMINI_API_KEY).strip()
    display_name = sender_name.strip() if sender_name else "tudo bem"

    history_formatted = ""
    if chat_history:
        history_formatted = "\n".join([f"- {h['role']}: \"{h['text']}\"" for h in chat_history[-6:]])

    system_instruction = (
        "Você é o Eduardo Bovoline, fundador da Vocação Comunicação & Marketing em Sorocaba/SP.\n"
        "Você conversa como um profissional de verdade no WhatsApp: direto, humano, respeitoso e consultivo, sem ser rude.\n\n"
        "DIRETRIZES DE OURO DA VOCAÇÃO:\n"
        "1. ESCUTA ATIVA (80% / 20%): NUNCA empurre diagnóstico, oferta, preço ou proposta antes de compreender ao menos 80% do negócio do lead.\n"
        "2. DIRETO E HUMANO (SEM BAJULAÇÃO): Não use comentários forçados de falsa empatia ou elogios vazios (evite 'Que fantástico!', 'Que maravilha!', 'Compreendo sua dor'). Seja natural, direto e educado.\n"
        "3. REGRA DA PERGUNTA ÚNICA: NUNCA faça mais de uma pergunta por mensagem. Faça apenas UMA pergunta clara e objetiva para entender a realidade do cliente.\n"
        "4. LINGUAGEM ÁGIL: Mensagens curtas de 1 a 2 linhas, ideais para leitura rápida no WhatsApp.\n"
        "5. LGPD: Se pedir para parar/remover, classifique como OPTOUT e encerre com brevidade.\n\n"
        "Responda SOMENTE um JSON válido:\n"
        "{\n"
        '  "intent": "QUALIFICATION" | "QUESTION" | "OBJECTION" | "POSITIVE" | "OPTOUT",\n'
        '  "stage": "LISTENING" | "DIAGNOSING" | "READY_TO_OFFER",\n'
        '  "reasoning": "análise rápida do momento do cliente",\n'
        '  "suggested_reply": "mensagem curta, direta, humana, com rigorosamente UMA pergunta objetiva pronta para envio"\n'
        "}"
    )

    prompt = (
        f"{system_instruction}\n\n"
        f"Histórico recente da conversa com {sender_name}:\n{history_formatted}\n\n"
        f"Nova mensagem recebida do lead: \"{message_text}\"\n\n"
        "Gere a resposta adequada (JSON):"
    )

    # Chamada à Gemini API com timeout ágil de 8s
    # Modelos prioritários: gemini-3.8-flash com fallback rápido
    for model_name in ["gemini-3.8-flash", "gemini-flash-lite-latest"]:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature": 0.3,
                "maxOutputTokens": 600
            }
        }
        try:
            resp = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=8)
            if resp.status_code == 200:
                res_json = resp.json()
                raw_text = res_json["candidates"][0]["content"]["parts"][0]["text"].strip()
                clean_json = re.sub(r"^```(json)?\s*", "", raw_text, flags=re.MULTILINE)
                clean_json = re.sub(r"\s*```$", "", clean_json, flags=re.MULTILINE).strip()
                parsed = json.loads(clean_json)
                if parsed.get("suggested_reply"):
                    return parsed
        except Exception:
            continue

    # Fallback consultivo direto, humano e com apenas UMA pergunta
    lower = message_text.lower()
    if any(k in lower for k in ["industrial", "fabrica", "fábrica", "distribui", "distribuição", "atacado", "regiao", "região"]):
        reply = (
            f"Entendido, {display_name}. Hoje vocês atendem mais redes de supermercados ou comércios e padarias locais?"
        )
    elif any(k in lower for k in ["padaria", "pão", "confeitaria"]):
        reply = (
            f"Legal, {display_name}. O forte de vocês hoje é mais o fluxo de balcão e café ou também atendem encomendas e festas?"
        )
    elif any(k in lower for k in ["clinica", "clínica", "médica", "medica", "odonto", "dente", "dentista", "saude", "saúde"]):
        reply = (
            f"Entendi, {display_name}. Hoje a maior parte dos pacientes chega por indicação ou pelas buscas do Google?"
        )
    elif any(k in lower for k in ["marcenaria", "móvel", "moveis", "planejados", "arquitet"]):
        reply = (
            f"Entendido, {display_name}. Vocês atendem mais o cliente final direto ou atuam em parceria com escritórios de arquitetura?"
        )
    else:
        reply = (
            f"Legal, {display_name}. Hoje os novos clientes chegam mais pelo boca a boca ou vocês recebem contatos vindos da internet?"
        )

    return {
        "intent": "QUALIFICATION",
        "stage": "LISTENING",
        "reasoning": "Aprofundamento de escuta ativa sobre o modelo de negócio do lead",
        "suggested_reply": reply
    }
