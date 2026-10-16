import os
import sys
import json
import uuid

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

JSON_PATH = r"C:\Vocação 2027\QG Vocação 2027 do zero\leads_100_santa_rosalia_brasilandia.json"
QUEUE_SCRIPT_PATH = r"C:\Vocação 2027\QG Vocação 2027 do zero\disparador_fila_santa_rosalia_brasilandia.py"

SCHEMA = "workspace_2xmx8hech9nybwidia3404k2z"
EDUARDO_MEMBER_ID = "1c0b8905-7e8f-4f50-90a1-6c67135bb381"

def import_lead_via_sql(lead):
    c_id = str(uuid.uuid4())
    p_id = str(uuid.uuid4())
    o_id = str(uuid.uuid4())
    n_id = str(uuid.uuid4())

    name = lead["name"].replace("'", "''")
    addr = lead["addr"].replace("'", "''")
    phone = lead["phone"]
    bairro = lead["bairro"]
    cat = lead["cat"]
    oferta_nome = lead["oferta_nome"].replace("'", "''")
    oferta_micros = lead["oferta_micros"]
    urgencia = lead["urgencia_score"]
    perda = int(lead["perda_conversao_local"] * 100)

    sql = f"""
    -- Company
    INSERT INTO "{SCHEMA}"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '{c_id}', NOW(), NOW(), '{name}', '{addr}',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '{EDUARDO_MEMBER_ID}'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "{SCHEMA}"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '{p_id}', NOW(), NOW(), 'Responsável Comercial', '{name}',
        '{phone}', '{c_id}', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '{EDUARDO_MEMBER_ID}'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "{SCHEMA}"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '{o_id}', NOW(), NOW(), '{name} — {oferta_nome}', 'NEW', {oferta_micros}, 'BRL',
        '{c_id}', '{p_id}', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '{EDUARDO_MEMBER_ID}'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "{SCHEMA}"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '{n_id}', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** {bairro} ({addr})\\n**Categoria:** {cat}\\n\\n**Qualificação Jev:**\\n- **Oferta de Melhor Fit:** {oferta_nome}\\n- **Grau de Urgência:** {urgencia}/2\\n- **Perda de Clientes Locais:** {perda}%\\n- **Telefone:** {phone}',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '{EDUARDO_MEMBER_ID}'
    );

    -- NoteTarget
    INSERT INTO "{SCHEMA}"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '{n_id}', '{c_id}', '{p_id}', '{o_id}',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '{EDUARDO_MEMBER_ID}'
    );
    """
    return sql

def generate_queue_script(leads):
    queue_list_str = json.dumps([
        {
            "name": l["name"],
            "number": l["phone"],
            "bairro": l["bairro"],
            "hook": l["hook_whatsapp"],
            "oferta": l["oferta_nome"]
        } for l in leads
    ], indent=4, ensure_ascii=False)

    content = f'''"""
disparador_fila_santa_rosalia_brasilandia.py — Fila de Prospecção (100 Leads)
Pólos: Santa Rosália e Jardim Brasilândia — Qualificados por Jev System One
Cadência segura com warm-up escalonado (intervalo 6 a 9 min) e conformidade LGPD
"""

import os
import sys
import time
import random
import requests
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

EVOLUTION_API_URL = "http://localhost:8080"
INSTANCE_NAME = "vocacao_comercial"
API_KEY = "vocacao_update_secret_key_2026"
ADMIN_WHATSAPP = "5515981512083"

QUEUE = {queue_list_str}

DELIVERED_FILE = os.path.join(os.path.dirname(__file__), "delivered_leads.json")

def is_already_delivered(phone):
    if os.path.exists(DELIVERED_FILE):
        try:
            with open(DELIVERED_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return phone in data or phone[-8:] in str(data)
        except Exception:
            return False
    return False

def send_whatsapp(number, text):
    url = f"{{EVOLUTION_API_URL}}/message/sendText/{{INSTANCE_NAME}}"
    headers = {{"apikey": API_KEY, "Content-Type": "application/json"}}
    payload = {{
        "number": number,
        "text": text,
        "options": {{"linkPreview": False, "delay": 1200}}
    }}
    resp = requests.post(url, json=payload, headers=headers, timeout=20)
    return resp.status_code, resp.json()

def notify_admin(msg):
    send_whatsapp(ADMIN_WHATSAPP, msg)

def run_queue(limit=5):
    print(f"🚀 Iniciando lote seguro de {{limit}} disparos (Santa Rosália & Jardim Brasilândia)...")
    sent = 0
    for idx, item in enumerate(QUEUE):
        if sent >= limit:
            break

        phone = item["number"]
        name = item["name"]

        if is_already_delivered(phone):
            continue

        print(f"\\n[{{idx+1}}/{{len(QUEUE)}}] Disparando para {{name}} ({{phone}})...")
        status, res = send_whatsapp(phone, item["hook"])

        if status in [200, 201]:
            sent += 1
            notify_admin(
                f"📤 *DISPARO REALIZADO (PÓLO {{item['bairro'].upper()}}):*\\n"
                f"• *Lead:* {{name}}\\n"
                f"• *Oferta Jev:* {{item['oferta']}}\\n"
                f"• *Contato:* {{phone}}"
            )
            if sent < limit:
                wait_sec = random.randint(360, 540) # 6 a 9 min
                print(f"   [⏳] Aguardando cadência segura: {{wait_sec // 60}} min...")
                time.sleep(wait_sec)

    notify_admin(f"🏁 *LOTE CONCLUÍDO:* {{sent}} mensagens disparadas com segurança.")

if __name__ == "__main__":
    qty = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    run_queue(limit=qty)
'''
    with open(QUEUE_SCRIPT_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[✓] Script da fila gerado: {QUEUE_SCRIPT_PATH}")

def main():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        leads = json.load(f)

    print(f"[*] Gerando script SQL de importação para {len(leads)} leads...")
    all_sql = []
    for l in leads:
        all_sql.append(import_lead_via_sql(l))

    sql_file = r"C:\Vocação 2027\QG Vocação 2027 do zero\importar_100leads_twenty.sql"
    with open(sql_file, "w", encoding="utf-8") as f:
        f.write("\n".join(all_sql))
    print(f"[✓] Arquivo SQL gerado: {sql_file}")

    # Gera também o script da fila de disparo
    generate_queue_script(leads)

    # Executa a importação no Docker Twenty CRM
    cmd = f'docker exec -i twenty-db-1 psql -U postgres -d twenty < "{sql_file}"'
    print(f"[*] Para importar tudo no Twenty CRM, execute: {cmd}")

if __name__ == "__main__":
    main()
