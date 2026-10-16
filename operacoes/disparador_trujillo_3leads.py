"""
disparador_trujillo_3leads.py — Fila Local Otimizada (Vila Trujillo & Região)
Vocação Comunicação & Marketing — Padrão Vocação Start 2026
Integrado com: Janelas de Ouro, Intervalos Anti-Ban e Compliance LGPD
"""

import os
import re
import sys
import time
import json
import random
import requests
from datetime import datetime

# Import do Módulo Central de Governança
from CONFIG_MOTOR_DISPARO_VOCACOES_START import (
    EVOLUTION_API_URL,
    INSTANCE_NAME,
    API_KEY,
    ADMIN_WHATSAPP,
    WHATSAPP_LIMITS,
    is_in_golden_window,
    generate_compliant_hook,
    is_blacklisted
)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR       = os.path.dirname(__file__)
DELIVERED_FILE = os.path.join(BASE_DIR, "delivered_leads.json")

# Fila higienizada com copy oficial Vocação Start + LGPD
QUEUE = [
    {
        "name": "LODONTO Espaço do Sorriso",
        "number": "5515991712908",
        "segment": "odontologia e estética dental",
        "neighborhood": "na Vila Trujillo",
        "hook": generate_compliant_hook(
            lead_name="LODONTO Espaço do Sorriso",
            segment="odontologia",
            neighborhood="na Vila Trujillo"
        )
    },
    {
        "name": "RBS Centro de Reabilitação Oral",
        "number": "5515991982675",
        "segment": "reabilitação oral e implantes",
        "neighborhood": "na Vila Trujillo",
        "hook": generate_compliant_hook(
            lead_name="RBS Centro de Reabilitação Oral",
            segment="implantes e reabilitação oral",
            neighborhood="na Vila Trujillo"
        )
    },
    {
        "name": "Studio Veronezi",
        "number": "5515991043048",
        "segment": "estética e beleza",
        "neighborhood": "na região do Trujillo",
        "hook": generate_compliant_hook(
            lead_name="Studio Veronezi",
            segment="estética e salão",
            neighborhood="na região do Trujillo"
        )
    }
]

def load_active_chats():
    try:
        url = f"{EVOLUTION_API_URL}/chat/findChats/{INSTANCE_NAME}"
        resp = requests.get(url, headers={"apikey": API_KEY}, timeout=15)
        if resp.status_code == 200:
            chats = resp.json()
            numbers = set()
            for chat in chats:
                jid = chat.get("id", "") or chat.get("remoteJid", "")
                if "@s.whatsapp.net" in jid:
                    digits = re.sub(r"\D", "", jid.split("@")[0])
                    if digits:
                        numbers.add(digits[-8:])
            return numbers
    except Exception as e:
        print(f"[!] Erro ao carregar chats: {e}")
    return set()

def has_existing_chat(number, active_set):
    last8 = re.sub(r"\D", "", number)[-8:]
    return last8 in active_set

def send_whatsapp(number, text):
    url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
    headers = {"apikey": API_KEY, "Content-Type": "application/json"}
    payload = {
        "number": number,
        "text": text,
        "options": {"linkPreview": False, "delay": 1500}
    }
    resp = requests.post(url, json=payload, headers=headers, timeout=20)
    return resp.status_code, resp.json()

def notify_admin(msg):
    try:
        send_whatsapp(ADMIN_WHATSAPP, msg)
    except Exception:
        pass

def mark_delivered(number, lead_name):
    delivered = {}
    if os.path.exists(DELIVERED_FILE):
        try:
            with open(DELIVERED_FILE, "r", encoding="utf-8") as f:
                delivered = json.load(f)
        except Exception:
            delivered = {}
    delivered[number] = {
        "lead_name": lead_name,
        "delivered_at": datetime.now().isoformat()
    }
    try:
        with open(DELIVERED_FILE, "w", encoding="utf-8") as f:
            json.dump(delivered, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[!] Erro ao salvar delivered_leads: {e}")

def wait_for_golden_window():
    """Aguarda ativamente até que o horário esteja em uma Janela de Ouro permitida."""
    while True:
        allowed, reason = is_in_golden_window()
        if allowed:
            print(f"[✓] {reason} Liberando disparo.")
            return True
        print(f"[⏳ PAUSA ESTRATÉGICA] {reason} Checando novamente em 60s...")
        time.sleep(60)

def run_queue():
    active_chats = load_active_chats()
    total = len(QUEUE)
    print("=" * 65)
    print("🚀 MOTOR VOCAÇÃO START — FILA OTIMIZADA COM JANELA DE OURO")
    print(f"   Meta diária: Máx {WHATSAPP_LIMITS['MAX_DAILY_SENDS']} envios/dia")
    print(f"   Intervalo anti-ban: {WHATSAPP_LIMITS['MIN_INTERVAL_SECONDS']//60} a {WHATSAPP_LIMITS['MAX_INTERVAL_SECONDS']//60} min")
    print("=" * 65)

    for i, lead in enumerate(QUEUE):
        idx = i + 1
        
        # 1. Validação de Janela de Ouro de Alta Conversão
        wait_for_golden_window()

        # 2. Validação de Opt-Out / Blacklist
        if is_blacklisted(lead["number"]):
            print(f"[{idx}/{total}] [⛔ BLACKLIST] {lead['name']} pediu descadastro prévio. Pulando.")
            continue

        # 3. Validação de Conversa Existente
        if has_existing_chat(lead["number"], active_chats):
            print(f"[{idx}/{total}] [⚠️ HISTÓRICO] {lead['name']} já possui conversa no WhatsApp. Pulando.")
            notify_admin(f"⚠️ *PULADO:* {lead['name']} ({lead['number']}) já tem histórico de conversa.")
            continue

        now_str = datetime.now().strftime("%H:%M:%S")
        print(f"\n[{idx}/{total}] [{now_str}] Enviando para {lead['name']} ({lead['number']})...")

        status, data = send_whatsapp(lead["number"], lead["hook"])
        msg_id = data.get("key", {}).get("id", "N/A")
        print(f"   Status: {status} | Msg ID: {msg_id}")

        mark_delivered(lead["number"], lead["name"])

        # 4. Intervalo Seguro Randômico Anti-Ban
        if i < total - 1:
            sleep_sec = random.randint(
                WHATSAPP_LIMITS["MIN_INTERVAL_SECONDS"],
                WHATSAPP_LIMITS["MAX_INTERVAL_SECONDS"]
            )
            sleep_min = round(sleep_sec / 60, 1)
            notify_admin(
                f"✅ *[{idx}/{total}] Disparo Enviado:* {lead['name']}\n"
                f"📱 {lead['number']}\n"
                f"⏱️ Próximo envio em {sleep_min} min ({sleep_sec}s)."
            )
            print(f"   Aguardando {sleep_min} min de intervalo seguro...")
            time.sleep(sleep_sec)
        else:
            notify_admin(
                f"✅ *[{idx}/{total}] Disparo Enviado:* {lead['name']}\n"
                f"📱 {lead['number']}\n"
                f"🏁 Lote local concluído com sucesso!"
            )

    print("\n★ FILA CONCLUÍDA EM CONFORMIDADE TOTAL COM AS REGRAS ★")
    notify_admin(f"🎉 *CICLO CONCLUÍDO:* Disparos da Vila Trujillo realizados dentro das Janelas de Ouro!")

if __name__ == "__main__":
    run_queue()
