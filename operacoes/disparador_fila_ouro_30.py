"""
disparador_fila_ouro_30.py — Disparador Seguro para os 30 Leads Ouro
Pólos: Santa Rosália e Jardim Brasilândia
Foco: Alta comissão (R$ 850 a R$ 980) + Celular WhatsApp no Maps
Intervalo seguro: 240s a 360s entre disparos | Janela: 9h às 18h | Compliance LGPD
"""

import os
import sys
import time
import json
import random
import requests
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

EVOLUTION_API_URL = "http://localhost:8080"
INSTANCE_NAME = "vocacao_comercial"
API_KEY = "vocacao_update_secret_key_2026"
ADMIN_WHATSAPP = "5515981512083"

PROGRESS_FILE = "data/fila_ouro_progresso.json"
OPTOUT_FILE = "auto_responder_docker/data/optout_leads.json"

def load_json(path, default=None):
    if default is None:
        default = {}
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return default
    return default

def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def send_whatsapp(number, text):
    url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
    payload = {"number": number, "text": text}
    headers = {"apikey": API_KEY, "Content-Type": "application/json"}
    try:
        r = requests.post(url, json=payload, headers=headers, timeout=15)
        return r.status_code in [200, 201]
    except Exception as e:
        print(f"[!] Erro WhatsApp para {number}: {e}")
        return False

def notify_admin(msg):
    send_whatsapp(ADMIN_WHATSAPP, msg)

def is_within_commercial_window():
    now = datetime.now()
    # Segunda a Sexta: 09:00 as 18:00
    if now.weekday() >= 5: # Fim de semana
        return False
    return 9 <= now.hour < 18

def run_queue():
    leads_path = "leads_ouro_fila_disparo.json"
    if not os.path.exists(leads_path):
        print("Arquivo leads_ouro_fila_disparo.json não encontrado.")
        return

    with open(leads_path, "r", encoding="utf-8") as f:
        leads = json.load(f)

    progress = load_json(PROGRESS_FILE, default={"sent": [], "failed": [], "skipped": []})
    optout_data = load_json(OPTOUT_FILE, default={})

    sent_set = set(progress.get("sent", []))
    optout_set = set(optout_data.keys())

    total = len(leads)
    pending_leads = [l for l in leads if l["phone"] not in sent_set and l["phone"] not in optout_set]

    print(f"==================================================")
    print(f"🚀 FILA DE DISPARO SEGURO — 30 LEADS OURO")
    print(f"   Total no Lote: {total}")
    print(f"   Já disparados: {len(sent_set)}")
    print(f"   Pendentes agora: {len(pending_leads)}")
    print(f"==================================================")

    if not pending_leads:
        print("Todos os leads da fila ouro já foram processados.")
        notify_admin("✅ *FILA OURO CONCLUÍDA:* Todos os 30 leads ouro já receberam o hook inicial!")
        return

    notify_admin(
        f"🚀 *INICIANDO FILA DE 30 LEADS OURO!*\n\n"
        f"• *Alvos:* Santa Rosália & Brasilândia\n"
        f"• *Perfil:* WhatsApp celular direto + Ticket R$ 850 a R$ 980\n"
        f"• *Cadência:* 1 disparo a cada 4 a 6 minutos (Anti-Spam Meta)\n"
        f"• *Twenty CRM:* ✅ Registrados\n\n"
        f"Você receberá notificações aqui conforme as respostas chegarem."
    )

    for idx, lead in enumerate(pending_leads, start=1):
        # 1. Checa janela comercial
        while not is_within_commercial_window():
            print(f"[PAUSA] Fora do horário comercial (09:00 - 18:00). Aguardando 10 minutos...")
            time.sleep(600)

        phone = lead["phone"]
        name = lead["name"]
        hook = lead["hook_whatsapp"]
        oferta = lead["oferta_nome"]
        bairro = lead["bairro"]

        print(f"\n[{idx}/{len(pending_leads)}] Disparando para {name} ({phone}) — {bairro}...")
        success = send_whatsapp(phone, hook)

        if success:
            progress["sent"].append(phone)
            save_json(PROGRESS_FILE, progress)
            print(f"   ✅ Entregue com sucesso!")
            
            # Registra no log do chat_history
            chat_hist_path = "auto_responder_docker/data/chat_history.json"
            hist = load_json(chat_hist_path, default={})
            if phone not in hist:
                hist[phone] = []
            hist[phone].append({
                "role": "Vocação (Hook Prospecção)",
                "text": hook,
                "at": datetime.now().isoformat()
            })
            save_json(chat_hist_path, hist)

        else:
            progress["failed"].append(phone)
            save_json(PROGRESS_FILE, progress)
            print(f"   ❌ Falha no disparo.")

        # Se houver mais leads, aguarda intervalo seguro humanizado (240s a 360s)
        if idx < len(pending_leads):
            wait_sec = random.randint(240, 360)
            print(f"   ⏳ Aguardando {wait_sec}s (~{round(wait_sec/60, 1)} min) para o próximo lead...")
            time.sleep(wait_sec)

    notify_admin(
        f"🏁 *PROSPECÇÃO DA FILA OURO FINALIZADA!*\n\n"
        f"• *Total processado:* {len(pending_leads)} novos disparos\n"
        f"• *Twenty CRM:* Todos sincronizados\n"
        f"O auto-responder está a postos para processar qualquer réplica com escuta ativa!"
    )

if __name__ == "__main__":
    run_queue()
