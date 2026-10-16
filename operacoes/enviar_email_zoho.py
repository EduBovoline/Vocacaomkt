"""
enviar_email_zoho.py — Disparador de E-mails via Zoho Mail (contato@vocacao.digital)
Vocação Comunicação & Marketing
"""

import os
import sys
import smtplib

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formataddr
from email.header import Header

ZOHO_SMTP_HOST = "smtp.zoho.com"
ZOHO_SMTP_PORT = 465
ZOHO_USER = os.getenv("ZOHO_USER", "contato@vocacao.digital")
ZOHO_PASSWORD = os.getenv("ZOHO_PASSWORD", "HGA9SmwGmfhy")

def send_email(to_email, subject, body_html, attachment_path=None, sender_name="Vocação Comunicação & Marketing"):
    if not ZOHO_PASSWORD:
        print("[!] Senha de aplicativo do Zoho Mail (ZOHO_PASSWORD) não configurada.")
        return False

    msg = MIMEMultipart()
    msg['From'] = formataddr((str(Header(sender_name, 'utf-8')), ZOHO_USER))
    msg['To'] = to_email
    msg['Subject'] = str(Header(subject, 'utf-8'))

    msg.attach(MIMEText(body_html, 'html', 'utf-8'))

    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:
            part = MIMEApplication(f.read(), Name=os.path.basename(attachment_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
            msg.attach(part)

    try:
        with smtplib.SMTP_SSL(ZOHO_SMTP_HOST, ZOHO_SMTP_PORT) as server:
            server.login(ZOHO_USER, ZOHO_PASSWORD)
            server.sendmail(ZOHO_USER, to_email, msg.as_string())
        print(f"[OK] E-mail enviado com sucesso para {to_email} via Zoho Mail!")
        return True
    except Exception as e:
        print(f"[!] Erro ao enviar e-mail via Zoho: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso: python enviar_email_zoho.py <destinatario> <assunto> <corpo_html> [caminho_anexo]")
        sys.exit(1)
    to = sys.argv[1]
    subj = sys.argv[2]
    body = sys.argv[3]
    att = sys.argv[4] if len(sys.argv) > 4 else None
    send_email(to, subj, body, att)
