import subprocess
import json
import requests
import re
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

def run_query(sql):
    cmd = ["docker", "exec", "-i", "twenty-db-1", "psql", "-U", "postgres", "-d", "twenty", "-t", "-A", "-c", sql]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print("SQL ERROR:", r.stderr)
    return r.stdout.strip()

sql = """
SELECT 
    c.id, 
    c.name, 
    COALESCE(p."phonesPrimaryPhoneNumber", ''),
    COALESCE(o.stage::text, 'NO_OPP'),
    COALESCE(c."addressAddressCity", 'Sorocaba')
FROM "workspace_2xmx8hech9nybwidia3404k2z".company c
LEFT JOIN "workspace_2xmx8hech9nybwidia3404k2z".person p ON p."companyId" = c.id
LEFT JOIN "workspace_2xmx8hech9nybwidia3404k2z".opportunity o ON o."companyId" = c.id
ORDER BY c.name;
"""

raw_rows = run_query(sql).split("\n")
crm_leads = []
for line in raw_rows:
    if not line.strip():
        continue
    parts = line.split("|")
    if len(parts) >= 4:
        crm_leads.append({
            "id": parts[0],
            "name": parts[1],
            "phone": parts[2],
            "stage": parts[3],
            "city": parts[4] if len(parts) > 4 else "Sorocaba"
        })

print(f"Total Empresas cadastradas no Twenty CRM: {len(crm_leads)}")

# Consultar histórico real da Evolution API
API_KEY = "vocacao_update_secret_key_2026"
url = "http://localhost:8080/chat/findMessages/vocacao_comercial"
headers = {"apikey": API_KEY, "Content-Type": "application/json"}

contacted_leads = []
virgin_leads = []

for l in crm_leads:
    clean_phone = re.sub(r"\D", "", l["phone"])
    if not clean_phone:
        virgin_leads.append(l)
        continue
    if not clean_phone.startswith("55") and len(clean_phone) in [10, 11]:
        clean_phone = "55" + clean_phone
    
    payload = {"where": {"key": {"remoteJid": f"{clean_phone}@s.whatsapp.net"}}}
    has_msg = False
    records = []
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=5)
        records = resp.json().get("messages", {}).get("records", [])
        if records:
            has_msg = True
    except Exception:
        pass
    
    if has_msg:
        l["total_msgs"] = len(records)
        last_ts = records[-1].get("messageTimestamp")
        l["last_contact_date"] = datetime.fromtimestamp(last_ts).strftime("%d/%m/%Y %H:%M") if last_ts else "N/A"
        contacted_leads.append(l)
    else:
        virgin_leads.append(l)

print(f"\n==========================================")
print(f"AUDITORIA COMPLETA DE LEADS NO TWENTY CRM")
print(f"==========================================")
print(f"1. JÁ CONTATADOS NO WHATSAPP: {len(contacted_leads)}")
print(f"2. LEADS VIRGENS (PRONTOS PARA DISPARO): {len(virgin_leads)}")

print(f"\n--- LISTA DOS JÁ CONTATADOS ({len(contacted_leads)}) ---")
for c in contacted_leads:
    print(f"• [{c['stage']}] {c['name']} ({c['phone']}) - Último contato: {c.get('last_contact_date')} ({c.get('total_msgs')} msgs)")

print(f"\n--- AMOSTRA DE LEADS VIRGENS NO CRM ({len(virgin_leads)}) ---")
for v in virgin_leads[:10]:
    print(f"• [{v['stage']}] {v['name']} ({v['phone']})")

# Salva arquivo consolidado para alimentar o painel e o CRM
with open("c:/Vocação 2027/QG Vocação 2027 do zero/scratch/crm_leads_auditados.json", "w", encoding="utf-8") as f:
    json.dump({
        "contacted": contacted_leads,
        "virgin": virgin_leads
    }, f, indent=2, ensure_ascii=False)
