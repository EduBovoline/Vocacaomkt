import csv
import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

leads_dir = r"c:\Vocação 2027\QG Vocação 2027 do zero\1 Leads"
data_dir = r"c:\Vocação 2027\QG Vocação 2027 do zero\auto_responder_docker\data"

all_leads = []

def parse_csv(filename, category, default_segment, default_oferta):
    path = os.path.join(leads_dir, filename)
    if not os.path.exists(path):
        return []
    items = []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        reader = csv.reader(f, delimiter=";")
        header = next(reader, None)
        for row in reader:
            if len(row) >= 9 and row[2].strip():
                phone = re.sub(r"\D", "", row[8])
                if phone and not phone.startswith("55") and len(phone) in [10, 11]:
                    phone = "55" + phone
                items.append({
                    "id": row[0].strip(),
                    "name": row[2].strip().replace('"', ''),
                    "segment": row[5].strip().replace('"', '') if len(row) > 5 and row[5].strip() else default_segment,
                    "category": category,
                    "bairro": row[6].strip().replace('"', '') if len(row) > 6 else "Sorocaba",
                    "address": row[7].strip().replace('"', '') if len(row) > 7 else "",
                    "phone": phone,
                    "maps_url": row[9].strip().replace('"', '') if len(row) > 9 else "",
                    "email": row[10].strip().replace('"', '') if len(row) > 10 else "",
                    "site": row[11].strip().replace('"', '') if len(row) > 11 else "",
                    "gargalo": row[12].strip().replace('"', '') if len(row) > 12 else "",
                    "ticket": row[14].strip().replace('"', '') if len(row) > 14 else "Alto Padrão",
                    "priority": row[16].strip().replace('"', '') if len(row) > 16 else "Alta",
                    "hook_a": row[17].strip().replace('"', '') if len(row) > 17 else "",
                    "hook_b": row[18].strip().replace('"', '') if len(row) > 18 else "",
                    "jev_oferta": default_oferta,
                    "jev_urgencia": 2 if "Crítica" in (row[16] if len(row) > 16 else "") else 1,
                    "jev_perda": 85 if "marcenaria" in category else (80 if "garagem" in category else 72)
                })
    return items

marc = parse_csv("Planilha_Prospeccao_Marcenaria_Alto_Ticket_Sorocaba.csv", "marcenarias", "Marcenaria Autoral & Alto Padrão", "Vocação Update & SSL (R$ 980)")
gar = parse_csv("Planilha_Prospeccao_Garagens_Seminovos_Sorocaba.csv", "garagens", "Garagem & Seminovos Selecionados", "Combo Maps + Tour 360° (R$ 950)")
ind = parse_csv("Planilha_Prospeccao_Industrias_Sorocaba.csv", "industrias", "Indústria & Manufatura B2B", "Portal B2B & Domínio (R$ 1.500)")

all_leads = marc + gar + ind

out_path = os.path.join(data_dir, "leads_alto_ticket_verificados.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_leads, f, indent=2, ensure_ascii=False)

print(f"Total de Leads de Alto Ticket carregados com sucesso: {len(all_leads)}")
print(f"Marcenarias: {len(marc)}")
print(f"Garagens: {len(gar)}")
print(f"Indústrias: {len(ind)}")
