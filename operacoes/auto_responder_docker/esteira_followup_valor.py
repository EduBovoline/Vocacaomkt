"""
esteira_followup_valor.py — Esteira Automatizada de Follow-up de Valor (D+3 e D+7)
Vocação Comunicação & Marketing
Anti-bloqueio Meta | Janela Comercial (9h às 18h) | Espaçamento Seguro de 7 Minutos
"""

import os
import sys
import re
import json
import time
import requests
from datetime import datetime, timedelta

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

EVOLUTION_API_URL = os.environ.get("EVOLUTION_API_URL", "http://localhost:8080")
INSTANCE_NAME = os.environ.get("INSTANCE_NAME", "vocacao_comercial")
API_KEY = os.environ.get("API_KEY", "vocacao_update_secret_key_2026")
ADMIN_WHATSAPP = os.environ.get("ADMIN_WHATSAPP", "5515981512083")

DATA_DIR = os.environ.get("DATA_DIR", r"c:\Vocação 2027\QG Vocação 2027 do zero\auto_responder_docker\data")
HISTORY_FILE = os.path.join(DATA_DIR, "chat_history.json")
OPTOUT_FILE = os.path.join(DATA_DIR, "optout_leads.json")
FOLLOWUP_STATE_FILE = os.path.join(DATA_DIR, "followup_state.json")

# Contatos pessoais e indicações (nunca recebem follow-up robótico)
EXCLUDED_PHONES = ["981512083", "981781911", "1807055946", "11976035867"]

MSG_D3 = (
    "Olá! Passando rápido para compartilhar um dado prático da região: hoje, mais de 70% dos clientes locais "
    "decidem se chamam no WhatsApp olhando a nota e as fotos do Maps antes.\n\n"
    "O nosso trabalho aqui na Vocação é justamente garantir que a sua empresa seja a primeira escolha visual "
    "de quem busca no bairro. Se fizer sentido entender como fazemos isso na prática, me avise por aqui!"
)

MSG_D7 = (
    "Olá! Sei que a rotina é corrida. Desenvolvemos estruturas rápidas que colocam empresas locais no topo "
    "das buscas com botão direto de contato em até 7 dias úteis.\n\n"
    "Como não tivemos retorno, vou encerrar as mensagens por aqui para não incomodar. "
    "Se em algum momento quiser elevar o posicionamento digital de vocês, fico à disposição!"
)

def load_json(path):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def send_whatsapp(number, text):
    url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
    headers = {"apikey": API_KEY, "Content-Type": "application/json"}
    payload = {"number": number, "text": text, "options": {"delay": 1500}}
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=20)
        return resp.status_code in [200, 201], resp.text
    except Exception as e:
        return False, str(e)

def notify_admin(msg):
    send_whatsapp(ADMIN_WHATSAPP, msg)

def is_business_hours():
    now = datetime.now()
    if now.weekday() >= 5:  # Sábado ou Domingo
        return False
    return 9 <= now.hour < 18

def evaluate_and_run(dry_run=False):
    print("=" * 60)
    print("★ ESTEIRA DE FOLLOW-UP DE VALOR (D+3 e D+7) ★")
    print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Modo: {'SIMULAÇÃO (DRY RUN)' if dry_run else 'ENVIO REAL'}")
    print("=" * 60)

    if not dry_run and not is_business_hours():
        print("[!] Fora da janela comercial (9h às 18h em dias úteis). Envio suspenso para proteção.")
        return

    history = load_json(HISTORY_FILE)
    optouts = load_json(OPTOUT_FILE)
    state = load_json(FOLLOWUP_STATE_FILE)

    now = datetime.now()
    pending_actions = []

    for phone, msgs in history.items():
        clean = re.sub(r"\D", "", phone)
        if any(ex in clean for ex in EXCLUDED_PHONES):
            continue

        # Se pediu optout ("PARAR"), ignora
        if clean in optouts or phone in optouts:
            continue

        # Verifica se o lead respondeu algo humano
        human_replied = False
        initial_dispatch_time = None

        for m in msgs:
            role = m.get("role", "")
            txt = m.get("text", "")
            at_str = m.get("at", "")

            if "Hook" in role or "Prospecção" in role:
                if not initial_dispatch_time and at_str:
                    try:
                        initial_dispatch_time = datetime.fromisoformat(at_str)
                    except Exception:
                        pass
            elif "Lead" in role:
                # Se disse PARAR
                if any(w in txt.lower() for w in ["parar", "descadastrar", "cancelar"]):
                    human_replied = True
                    break
                # Se respondeu qualquer coisa, é lead vivo: não recebe follow-up frio automático
                human_replied = True
                break

        if human_replied or not initial_dispatch_time:
            continue

        days_passed = (now - initial_dispatch_time).days
        lead_state = state.get(clean, {})

        # Critério D+3 (>= 3 dias)
        if days_passed >= 3 and not lead_state.get("d3_sent"):
            pending_actions.append({
                "phone": clean,
                "type": "D+3",
                "days": days_passed,
                "text": MSG_D3
            })
        # Critério D+7 (>= 7 dias após D+3)
        elif days_passed >= 7 and lead_state.get("d3_sent") and not lead_state.get("d7_sent"):
            pending_actions.append({
                "phone": clean,
                "type": "D+7",
                "days": days_passed,
                "text": MSG_D7
            })

    total = len(pending_actions)
    print(f"[+] Total de leads elegíveis para Follow-up de Valor: {total}")

    if total == 0:
        print("[i] Nenhum lead na janela de D+3 ou D+7 no momento.")
        return

    for i, act in enumerate(pending_actions):
        idx = i + 1
        print(f"\n[{idx}/{total}] Preparando Follow-up {act['type']} para {act['phone']} (D+{act['days']})...")
        if dry_run:
            print(f"[SIMULADO] Texto: {act['text'][:80]}...")
            continue

        ok, resp = send_whatsapp(act["phone"], act["text"])
        if ok:
            print(f"-> [OK] Enviado com sucesso.")
            if act["phone"] not in state:
                state[act["phone"]] = {}
            if act["type"] == "D+3":
                state[act["phone"]]["d3_sent"] = datetime.now().isoformat()
            elif act["type"] == "D+7":
                state[act["phone"]]["d7_sent"] = datetime.now().isoformat()
            save_json(FOLLOWUP_STATE_FILE, state)

            notify_admin(
                f"📈 *FOLLOW-UP DE VALOR ({act['type']}) ENVIADO:*\n"
                f"• *Lead:* {act['phone']}\n"
                f"• *Tempo decorrido:* D+{act['days']}\n"
                f"• *Próximo envio da esteira:* em 7 minutos."
            )
        else:
            print(f"-> [FALHA] Erro ao enviar: {resp}")

        if i < total - 1 and not dry_run:
            print("[⏱️] Aguardando intervalo de proteção anti-bloqueio (7 minutos / 420s)...")
            time.sleep(420)

    print("\n★ ESTEIRA DE FOLLOW-UP CONCLUÍDA ★")

if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    evaluate_and_run(dry_run=dry)
