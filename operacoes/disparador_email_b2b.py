"""
disparador_email_b2b.py — Motor de Prospecção por E-mail B2B (Sistema Vocação Start)
Vocação Comunicação & Marketing — Outubro / 2026
Base Legal: Art. 7º, IX da LGPD (Legítimo Interesse Comercial B2B)
"""

import os
import sys
import time
import json
import random
from datetime import datetime
from enviar_email_zoho import send_email

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(__file__)
DELIVERED_EMAILS_FILE = os.path.join(BASE_DIR, "delivered_emails.json")

def load_delivered_emails():
    if os.path.exists(DELIVERED_EMAILS_FILE):
        try:
            with open(DELIVERED_EMAILS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def record_delivered_email(email, company_name):
    data = load_delivered_emails()
    data[email.lower()] = {
        "company_name": company_name,
        "sent_at": datetime.now().isoformat()
    }
    with open(DELIVERED_EMAILS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def is_email_already_delivered(email):
    data = load_delivered_emails()
    return email.lower() in data

def build_email_html(responsible_name, company_name, segment, neighborhood):
    resp = responsible_name if responsible_name else "Responsável"
    bairro = f"na região do {neighborhood}" if neighborhood else "em Sorocaba"
    
    html = f"""
    <div style="font-family: Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 14px; line-height: 1.6; color: #222222; max-width: 600px;">
        <p>Olá, <b>{resp}</b>, tudo bem?</p>
        
        <p>Meu nome é <b>Edu Bovoline</b>, sou de Sorocaba e atuo com estruturação digital local na <b>Vocação Comunicação & Marketing</b>.</p>
        
        <p>Estava analisando os comércios do segmento de <b>{segment}</b> {bairro} e notei que a <b>{company_name}</b> possui um excelente histórico de atendimento, porém a apresentação digital de vocês no Google Maps ainda não reflete a autoridade real do negócio.</p>
        
        <p>Hoje, quem procura pelo seu serviço no smartphone encontra informações desatualizadas e não tem um botão direto para iniciar atendimento no seu WhatsApp.</p>
        
        <p>Montamos uma demonstração prática de como posicionar a sua empresa como referência no bairro com uma estrutura segura, rápida e com carregamento instantâneo.</p>
        
        <p><b>Posso te encaminhar essa análise por aqui ou pelo WhatsApp?</b></p>
        
        <br>
        <p style="margin-bottom: 2px;">Atenciosamente,</p>
        <p style="margin-top: 0; font-weight: bold; color: #111111;">Edu Bovoline</p>
        <p style="margin: 0; color: #555555; font-size: 13px;">Vocação Comunicação & Marketing — Sorocaba/SP</p>
        <p style="margin: 0; color: #555555; font-size: 13px;">WhatsApp: (15) 98151-2083 | <a href="https://vocacao.digital" style="color: #0066cc; text-decoration: none;">vocacao.digital</a></p>
        
        <br><hr style="border: none; border-top: 1px solid #e0e0e0; margin: 20px 0 10px 0;">
        <p style="font-size: 11px; color: #888888; line-height: 1.4; margin: 0;">
            <b>Aviso LGPD:</b> Este e-mail comercial tem caráter exclusivamente institucional e B2B (Art. 7º, IX da Lei 13.709/2018), com dados públicos do Google Maps. Caso não deseje receber nossas análises de posicionamento, basta responder 'DESCADASTRAR' para a remoção imediata dos seus dados da nossa base.
        </p>
    </div>
    """
    return html

def send_b2b_email(lead):
    email = lead.get("email", "").strip().lower()
    company = lead.get("name", "Sua Empresa")
    responsible = lead.get("responsible", "")
    segment = lead.get("segment", "Serviços")
    neighborhood = lead.get("neighborhood", "Sorocaba")
    
    if not email or "@" not in email:
        print(f"   [!] E-mail inválido para {company}: '{email}'. Pulando.")
        return False
        
    if is_email_already_delivered(email):
        print(f"   [SKIP] E-mail já enviado anteriormente para {email} ({company}). Pulando.")
        return False

    subject = f"Presença da {company} nas buscas do Google no {neighborhood}"
    body_html = build_email_html(responsible, company, segment, neighborhood)

    print(f"\n[📧] Disparando e-mail B2B para {company} ({email})...")
    success = send_email(email, subject, body_html, sender_name="Edu Bovoline | Vocação")
    if success:
        print(f"[✓] E-mail entregue com sucesso para {email}!")
        record_delivered_email(email, company)
        return True
    else:
        print(f"[!] Falha no envio para {email}.")
        return False

def run_email_queue(leads_list, min_delay=20, max_delay=45):
    total = len(leads_list)
    print("=" * 60)
    print(f"🚀 MOTOR DE PROSPECÇÃO B2B POR E-MAIL — SISTEMA VOCAÇÃO START")
    print(f"   Total de alvos: {total} | Intervalo: {min_delay}s a {max_delay}s")
    print("=" * 60)
    
    for i, lead in enumerate(leads_list):
        idx = i + 1
        print(f"\n[{idx}/{total}] Processando {lead.get('name')} <{lead.get('email')}>...")
        send_b2b_email(lead)
        
        if i < total - 1:
            wait_s = random.randint(min_delay, max_delay)
            print(f"   Aguardando {wait_s}s para próximo envio seguro via Zoho...")
            time.sleep(wait_s)
            
    print("\n★ FILA DE E-MAILS CONCLUÍDA COM SUCESSO! ★")

if __name__ == "__main__":
    # Teste de conexão ou execução direta
    print("Módulo carregado com sucesso. Para disparar, passe a lista de leads em 'run_email_queue()'.")
