"""
disparador_lote_emails_frios.py — Disparo em Lote de E-mails Frios B2B via Zoho Mail
Vocação Comunicação & Marketing — Setembro / 2026
"""

import os
import sys
import time
import json
import random
import requests
from datetime import datetime
from disparador_email_b2b import send_b2b_email, load_delivered_emails

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

EVOLUTION_API_URL = "http://localhost:8080"
INSTANCE_NAME     = "vocacao_comercial"
API_KEY           = "vocacao_update_secret_key_2026"
ADMIN_WHATSAPP    = "5515981512083"

def notify_admin(msg):
    try:
        url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
        payload = {"number": ADMIN_WHATSAPP, "text": msg}
        requests.post(url, json=payload, headers={"apikey": API_KEY, "Content-Type": "application/json"}, timeout=10)
    except Exception as e:
        print("[!] Erro ao notificar admin:", e)

# Lote selecionado de leads frios qualificados de Sorocaba com e-mail corporativo
LEADS_BATCH = [
    {
        "name": "Maxima Automóveis",
        "email": "contato@maximaautomoveis.com.br",
        "segment": "Garagem Multimarcas & Seminovos",
        "neighborhood": "Parque Campolim",
        "responsible": "Diretoria Maxima"
    },
    {
        "name": "Állus Veículos",
        "email": "contato@allusveiculos.com.br",
        "segment": "Seminovos Selecionados",
        "neighborhood": "Vila Lucy / General Carneiro",
        "responsible": "Equipe Állus"
    },
    {
        "name": "Ômega Veículos",
        "email": "contato@omegaveiculos.net",
        "segment": "Revenda Multimarcas Tradicional",
        "neighborhood": "Cerrado / General Carneiro",
        "responsible": "Equipe Ômega"
    },
    {
        "name": "Cabral Multimarcas",
        "email": "contato@cabralmultimarcas.com.br",
        "segment": "Mega Loja Multimarcas",
        "neighborhood": "Eixo Ipanema",
        "responsible": "Diretoria Cabral"
    },
    {
        "name": "Nexmotors Veículos",
        "email": "contato@nexmotors.com.br",
        "segment": "Seminovos Selecionados",
        "neighborhood": "Jardim Vera Cruz / Pannunzio",
        "responsible": "Equipe Nexmotors"
    },
    {
        "name": "GC Veículos",
        "email": "contato@gcveiculos.com.br",
        "segment": "Seminovos Selecionados",
        "neighborhood": "Jardim Santa Rosália",
        "responsible": "Equipe GC"
    },
    {
        "name": "Flamil Veículos",
        "email": "contato@flamilveiculos.com.br",
        "segment": "Garagem Tradicional",
        "neighborhood": "Vila Angélica",
        "responsible": "Equipe Flamil"
    },
    {
        "name": "KS Motors",
        "email": "contato@ksmotors.com.br",
        "segment": "Garagem Multimarcas",
        "neighborhood": "Jardim Emília / Washington Luiz",
        "responsible": "Equipe KS Motors"
    }
]

def run_batch():
    delivered = load_delivered_emails()
    pending = [l for l in LEADS_BATCH if l["email"].lower() not in delivered]
    
    total = len(pending)
    print("=" * 60)
    print(f"🚀 INICIANDO SESSÃO DE DISPARO DE E-MAILS FRIOS (ZOHO MAIL)")
    print(f"   Total pendentes no lote: {total}")
    print("=" * 60)
    
    if total == 0:
        print("[!] Todos os leads deste lote já receberam e-mail anteriormente.")
        return

    notify_admin(
        f"📧 *INICIANDO LOTE DE E-MAILS FRIOS:*\n"
        f"• *Alvos:* {total} comércios locais (Seminovos & Garagens)\n"
        f"• *Canal:* Zoho Mail (`contato@vocacao.digital`)\n"
        f"• *Cadência:* 70 a 110 segundos entre envios para proteção de entregabilidade."
    )

    enviados = 0
    for i, lead in enumerate(pending):
        idx = i + 1
        now_str = datetime.now().strftime("%H:%M:%S")
        print(f"\n[{idx}/{total}] [{now_str}] Enviando para {lead['name']} <{lead['email']}>...")
        
        success = send_b2b_email(lead)
        if success:
            enviados += 1
            print(f"[✓] E-mail entregue com sucesso ({enviados}/{total}).")
        
        # Intervalo anti-spam entre 70 e 110 segundos (exceto no último)
        if i < total - 1:
            wait_s = random.randint(70, 110)
            print(f"   Aguardando {wait_s}s para próximo disparo seguro...")
            time.sleep(wait_s)

    notify_admin(
        f"✅ *LOTE DE E-MAILS FINALIZADO COM SUCESSO!*\n"
        f"• *Total enviados:* {enviados}/{total}\n"
        f"• *Horário de conclusão:* {datetime.now().strftime('%H:%M')}\n"
        f"• Qualquer resposta recebida na caixa de entrada do Zoho será processada."
    )
    print("\n★ SESSÃO DE E-MAILS B2B FINALIZADA COM SUCESSO! ★")

if __name__ == "__main__":
    run_batch()
