import subprocess
import requests
import json
import re

import sys
sys.stdout.reconfigure(encoding='utf-8')

def run_sql(sql):
    cmd = ["docker", "exec", "-i", "twenty-db-1", "psql", "-U", "postgres", "-d", "twenty", "-t", "-A", "-c", sql]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    return r.stdout.strip()

API_KEY = "vocacao_update_secret_key_2026"
url = "http://localhost:8080/chat/findMessages/vocacao_comercial"
headers = {"apikey": API_KEY, "Content-Type": "application/json"}

# 1. Pega todas as empresas, telefones e oportunidades
sql_get = """
SELECT c.id, c.name, COALESCE(p."phonesPrimaryPhoneNumber", ''), o.id, COALESCE(o.stage::text, 'NEW')
FROM "workspace_2xmx8hech9nybwidia3404k2z".company c
LEFT JOIN "workspace_2xmx8hech9nybwidia3404k2z".person p ON p."companyId" = c.id
LEFT JOIN "workspace_2xmx8hech9nybwidia3404k2z".opportunity o ON o."companyId" = c.id;
"""

rows = run_sql(sql_get).split("\n")
contacted_updated = 0
virgin_kept = 0

for r in rows:
    if not r.strip():
        continue
    parts = r.split("|")
    if len(parts) >= 5:
        c_id, name, raw_phone, opp_id, cur_stage = parts[0], parts[1], parts[2], parts[3], parts[4]
        clean_phone = re.sub(r"\D", "", raw_phone)
        if not clean_phone:
            continue
        if not clean_phone.startswith("55") and len(clean_phone) in [10, 11]:
            clean_phone = "55" + clean_phone

        # Checa mensagens na Evolution API
        payload = {"where": {"key": {"remoteJid": f"{clean_phone}@s.whatsapp.net"}}}
        has_msg = False
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=5)
            records = resp.json().get("messages", {}).get("records", [])
            if records and len(records) > 0:
                has_msg = True
        except Exception:
            pass

        if has_msg:
            # Determina o estágio adequado:
            # BodyBe e Med Cor -> MEETING
            # Outros contatados -> SCREENING
            new_stage = "MEETING" if any(w in name.lower() for w in ["bodybe", "med cor"]) else "SCREENING"
            
            if opp_id:
                upd_sql = f"""
                UPDATE "workspace_2xmx8hech9nybwidia3404k2z".opportunity
                SET stage = '{new_stage}', "updatedAt" = NOW()
                WHERE id = '{opp_id}';
                """
                run_sql(upd_sql)
            else:
                # Cria oportunidade em SCREENING se não existia
                ins_sql = f"""
                INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z".opportunity 
                (id, name, stage, "companyId", "createdAt", "updatedAt")
                VALUES (gen_random_uuid(), 'Oportunidade - {name.replace("'", "''")}', '{new_stage}', '{c_id}', NOW(), NOW());
                """
                run_sql(ins_sql)
            contacted_updated += 1
            print(f"✅ [CONTATADO -> {new_stage}] {name} ({clean_phone})")
        else:
            # Mantém em NEW
            if opp_id and cur_stage != "NEW":
                run_sql(f"UPDATE \"workspace_2xmx8hech9nybwidia3404k2z\".opportunity SET stage = 'NEW' WHERE id = '{opp_id}';")
            virgin_kept += 1
            print(f"🌱 [VIRGEM -> NEW] {name} ({clean_phone})")

print(f"\nSincronização concluída!")
print(f"Total Contatados atualizados para SCREENING/MEETING: {contacted_updated}")
print(f"Total Virgens confirmados em NEW: {virgin_kept}")
