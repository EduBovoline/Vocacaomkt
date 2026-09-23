"""
auto_responder.py — Respondedor Automático de WhatsApp (Vocação Comunicação & Marketing)

Funcionalidade:
1. Recebe webhooks da Evolution API (MESSAGES_UPSERT) na porta 5680
2. Filtra mensagens recebidas (ignora mensagens enviadas por nós mesmos)
3. Detecta intenção positiva ("sim", "pode mandar", "quero ver", "claro", etc.)
4. Localiza o lead e seu PDF correspondente (via Twenty CRM ou pasta de leads)
5. Envia o PDF oficial de diagnóstico com legenda persuasiva via Evolution API
6. Registra o evento de entrega nas notas e avança o estágio da oportunidade no Twenty CRM
"""

import os
import sys
import re
import json
import base64
import unicodedata
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')


EVOLUTION_API_URL = "http://localhost:8080"
INSTANCE_NAME = "vocacao_comercial"
API_KEY = "vocacao_update_secret_key_2026"
DOCKER_BIN = r"C:\Program Files\Docker\Docker\resources\bin\docker.exe"
LEADS_DIR = r"C:\Vocação 2027\QG Vocação 2027 do zero\2 Leads"
SCHEMA = "workspace_2xmx8hech9nybwidia3404k2z"

POSITIVE_TRIGGERS = [
    "sim", "pode", "manda", "mandar", "quero", "claro", "envia", "enviar",
    "mostra", "mostrar", "ok", "com certeza", "mande", "blz", "beleza",
    "opa", "manda ai", "manda aí", "fiquei curiosa", "curioso", "tenho interesse"
]

def normalize_text(text):
    if not text:
        return ""
    nfkd = unicodedata.normalize('NFKD', text)
    clean = "".join([c for c in nfkd if not unicodedata.combining(c)])
    return clean.lower().strip()

def run_psql(sql):
    try:
        proc = subprocess.Popen(
            [DOCKER_BIN, "exec", "-i", "twenty-db-1", "psql", "-U", "postgres", "-d", "twenty"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8"
        )
        stdout, stderr = proc.communicate(input=sql)
        return stdout.strip()
    except Exception as e:
        print("[!] Erro PSQL:", e)
        return ""

def find_lead_by_phone(phone_digits):
    # Pega os últimos 8 dígitos para matching flexível
    last_digits = phone_digits[-8:] if len(phone_digits) >= 8 else phone_digits
    
    # 1. Busca no Twenty CRM
    sql = f"""
    SELECT c.id, c.name 
    FROM "{SCHEMA}"."company" c
    JOIN "{SCHEMA}"."person" p ON p."companyId" = c.id
    WHERE regexp_replace(p."phonesPrimaryPhoneNumber", '[^0-9]', '', 'g') LIKE '%{last_digits}%'
    LIMIT 1;
    """
    out = run_psql(sql)
    for line in out.splitlines():
        line = line.strip()
        if "|" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 2 and len(parts[0]) == 36 and "-" in parts[0]:
                return {"id": parts[0], "name": parts[1]}

    # 2. Fallback por mapeamento direto
    if "981314488" in phone_digits:
        return {"id": "2d2e6d9d-7774-448a-9861-439e26e1c85f", "name": "Estética Kirei Campolim"}
    if "996963197" in phone_digits:
        return {"id": "eab08c79-753d-48c0-acb1-010408412a0c", "name": "Fernanda Pimentel Estética Avançada"}

    return None

def find_pdf_for_lead(lead_name):
    # Procura a pasta do lead
    for folder in os.listdir(LEADS_DIR):
        folder_path = os.path.join(LEADS_DIR, folder)
        if os.path.isdir(folder_path):
            if lead_name.lower() in folder.lower() or folder.lower() in lead_name.lower():
                for f in os.listdir(folder_path):
                    if f.endswith("-cliente.pdf") or (f.endswith(".pdf") and "prospeccao" in f):
                        return os.path.join(folder_path, f)
    return None

def send_pdf(number, pdf_path, lead_name):
    print(f"\n[+] Enviando diagnóstico em PDF para {lead_name} ({number})...")
    with open(pdf_path, "rb") as f:
        pdf_b64 = base64.b64encode(f.read()).decode("utf-8")

    caption = (
        "Perfeito! Segue o diagnóstico visual em anexo (3 páginas). 📄✨\n\n"
        "O ponto mais crítico que detectamos na presença digital de vocês em Sorocaba "
        "está detalhado na *página 2*.\n\n"
        "Dê uma olhada de 2 minutos e me diga se faz sentido para vocês!"
    )

    url = f"{EVOLUTION_API_URL}/message/sendMedia/{INSTANCE_NAME}"
    headers = {
        "apikey": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "number": number,
        "mediatype": "document",
        "mimetype": "application/pdf",
        "caption": caption,
        "media": pdf_b64,
        "fileName": f"Diagnostico-Visual-{lead_name.replace(' ', '-')}.pdf"
    }

    resp = requests.post(url, json=payload, headers=headers, timeout=25)
    if resp.status_code in [200, 201]:
        print(f"[✓] PDF entregue com sucesso! Status: {resp.status_code}")
        return True
    else:
        print(f"[!] Falha no envio do PDF: {resp.status_code} - {resp.text}")
        return False

def update_crm_opportunity(company_id, text_reply):
    # Atualiza oportunidade para MEETING e insere nota
    sql = f"""
    UPDATE "{SCHEMA}"."opportunity"
    SET stage = 'MEETING', "updatedAt" = NOW()
    WHERE "companyId" = '{company_id}';

    INSERT INTO "{SCHEMA}"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(),
        'WhatsApp: Lead autorizou diagnóstico visual',
        '**Resposta recebida no WhatsApp:**\\n> "' || '{text_reply}' || '"\\n\\n**Ação executada:** Diagnóstico em PDF enviado automaticamente pelo assistente Vocação.',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    """
    run_psql(sql)
    print(f"[✓] CRM atualizado: Oportunidade movida para 'DELIBERATING' e nota gravada.")

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len).decode('utf-8')
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"status":"received"}')

        try:
            data = json.loads(body)
            self.process_webhook(data)
        except Exception as e:
            print("[!] Erro ao processar payload:", e)

    def process_webhook(self, data):
        event = data.get("event")
        # Aceita MESSAGES_UPSERT ou payload direto
        msg_data = data.get("data", {})
        key = msg_data.get("key", {})
        
        # Ignora mensagens enviadas por nós mesmos
        from_me = key.get("fromMe", False)
        if from_me:
            return

        remote_jid = key.get("remoteJid", "")
        if not remote_jid or "@s.whatsapp.net" not in remote_jid:
            return

        phone = remote_jid.split("@")[0]

        # Extrai o texto da mensagem
        message_obj = msg_data.get("message", {})
        text = (
            message_obj.get("conversation") or 
            message_obj.get("extendedTextMessage", {}).get("text") or 
            ""
        ).strip()

        if not text:
            return

        print(f"\n📩 [MENSAGEM RECEBIDA] De: {phone} ({msg_data.get('pushName', 'Desconhecido')})")
        print(f"   Conteúdo: \"{text}\"")

        # 1. Se for o gestor (Eduardo) aprovando a fila no WhatsApp
        if "981512083" in phone:
            norm = normalize_text(text)
            if any(w in norm for w in ["aprovar", "aprovado", "ok", "pode", "iniciar", "sim"]):
                print(f"   [★] APROVAÇÃO DO GESTOR DETECTADA! Iniciando disparador de 7 minutos...")
                disparador_script = os.path.join(os.path.dirname(__file__), "disparador_fila_7min.py")
                subprocess.Popen([sys.executable, disparador_script])
                return

        # 2. Verifica intenção positiva de clientes
        normalized = normalize_text(text)
        is_positive = any(re.search(rf"\b{re.escape(trigger)}\b", normalized) for trigger in POSITIVE_TRIGGERS)

        if not is_positive:
            print(f"   [i] Resposta recebida não é solicitação direta do diagnóstico.")
            return


        print(f"   [★] Intenção positiva detectada! Localizando lead...")
        lead = find_lead_by_phone(phone)
        if not lead:
            print(f"   [!] Nenhum lead cadastrado correspondente ao número {phone}.")
            return

        lead_name = lead["name"]
        company_id = lead["id"]
        print(f"   [✓] Lead identificado: {lead_name} (ID: {company_id})")

        pdf_path = find_pdf_for_lead(lead_name)
        if not pdf_path or not os.path.exists(pdf_path):
            print(f"   [!] PDF não encontrado para o lead '{lead_name}' em {LEADS_DIR}.")
            return

        print(f"   [✓] PDF localizado: {pdf_path}")
        success = send_pdf(phone, pdf_path, lead_name)
        if success:
            update_crm_opportunity(company_id, text)

    def log_message(self, format, *args):
        # Suprime logs de requisições HTTP triviais no terminal
        return

def run_server(port=5680):
    server = HTTPServer(("0.0.0.0", port), WebhookHandler)
    print("==================================================================")
    print(f" 🚀 AUTO-RESPONDER VOCAÇÃO 2027 ATIVO NA PORTA {port}")
    print(" Monitorando respostas do WhatsApp em tempo real...")
    print("==================================================================")
    server.serve_forever()

if __name__ == "__main__":
    run_server()
