import os
import re
import sys
import time
import json
import random
import requests
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

sys.path.append(r"C:\Vocação 2027\QG Vocação 2027 do zero")
from disparador_email_b2b import send_b2b_email
from CONFIG_MOTOR_DISPARO_VOCACOES_START import EVOLUTION_API_URL, INSTANCE_NAME, API_KEY, ADMIN_WHATSAPP

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
    except Exception as e:
        print("[!] Erro notify admin:", e)

# ── FASE 1: DISPARO POR E-MAIL (ZOHO) ──
email_leads = [
    {
        "name": "Studio Martin Pilates",
        "responsible": "Equipe Studio Martin",
        "email": "pilatesmartin@gmail.com",
        "segment": "Studio de Pilates & Movimento",
        "neighborhood": "Vila Hortência"
    },
    {
        "name": "Espaço Surya",
        "responsible": "Equipe Espaço Surya",
        "email": "yogaemsorocaba@gmail.com",
        "segment": "Yoga, Pilates & Terapias Integrativas",
        "neighborhood": "Vila Fiori / Zona Norte"
    }
]

print("=== [1/2] DISPARANDO E-MAILS B2B VIA ZOHO ===")
notify_admin("🚀 *DISPARO DE BAIRROS INICIADO:* Disparando e-mails para Studio Martin (Vila Hortência) e Espaço Surya (Vila Fiori)...")

for el in email_leads:
    print(f"Enviando e-mail para {el['name']} <{el['email']}>...")
    send_b2b_email(el)
    time.sleep(25)

notify_admin("✅ *E-MAILS ENTREGUES:* Studio Martin e Espaço Surya abordados com sucesso no canal e-mail.")

# ── FASE 2: DISPARO POR WHATSAPP COM ANTI-BAN ──
wa_leads = [
    {
        "name": "Stúdio de Pilates Fitness",
        "number": "5515991699731",
        "hook": (
            "Olá, tudo bem? Analisei a presença digital do Stúdio de Pilates na Rua Benedito Ferreira Telles no Jardim Simus "
            "e notei um ponto relevante: o espaço tem ótimo atendimento, mas quem pesquisa por pilates no Jardim Simus no Google "
            "encontra poucos elementos visuais antes de chamar no WhatsApp. "
            "Posso te enviar um diagnóstico visual de 2 minutos mostrando como mudar isso?\n\n"
            "_Contato comercial via dados públicos do Google Maps. Se não desejar receber mensagens, basta responder 'PARAR'._"
        )
    },
    {
        "name": "Jodi Moraes Treinamento Personalizado",
        "number": "5515997629693",
        "hook": (
            "Olá Jodi, tudo bem? Analisei a presença digital do seu espaço de treinamento personalizado na Vila Hortência "
            "e notei uma oportunidade clara: a entrega de vocês no treino funcional é excelente, mas quem pesquisa por personal "
            "e funcional na região encontra poucos canais diretos de contato antes de agendar. "
            "Posso te enviar um diagnóstico rápido mostrando como estruturar essa vitrine?\n\n"
            "_Contato comercial via dados públicos do Google Maps. Se não desejar receber mensagens, basta responder 'PARAR'._"
        )
    }
]

print("\n=== [2/2] DISPARANDO WHATSAPP COM CADÊNCIA ANTI-BAN ===")
for i, wl in enumerate(wa_leads):
    idx = i + 1
    total = len(wa_leads)
    now_str = datetime.now().strftime("%H:%M:%S")
    print(f"\n[{idx}/{total}] [{now_str}] Enviando WhatsApp para {wl['name']} ({wl['number']})...")
    
    st, resp = send_whatsapp(wl["number"], wl["hook"])
    print(f"Status: {st}")
    
    if i < total - 1:
        wait_s = random.randint(480, 600)  # 8 a 10 min
        wait_m = round(wait_s / 60, 1)
        notify_admin(
            f"✅ *[{idx}/{total}] WhatsApp Enviado:* {wl['name']}\n"
            f"📱 {wl['number']}\n"
            f"⏱️ Próximo envio em {wait_m} min (anti-ban)."
        )
        print(f"Aguardando {wait_m} min anti-ban...")
        time.sleep(wait_s)
    else:
        notify_admin(
            f"✅ *[{idx}/{total}] WhatsApp Enviado:* {wl['name']}\n"
            f"📱 {wl['number']}\n"
            f"🏁 *DISPARO DE BAIRROS FINALIZADO COM SUCESSO!*"
        )

print("\n★ OPERAÇÃO COMPLETA CONCLUÍDA! ★")
