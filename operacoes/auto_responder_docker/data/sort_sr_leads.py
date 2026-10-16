import json
import re

sr_path = 'auto_responder_docker/data/leads_100_santa_rosalia_brasilandia.json'
with open(sr_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def is_mobile(lead):
    clean = re.sub(r'\D', '', str(lead.get('phone', '')))
    return clean.startswith('55159') or (len(clean) == 11 and clean.startswith('159'))

mobiles = [l for l in data if is_mobile(l)]
landlines = [l for l in data if not is_mobile(l)]

sorted_data = mobiles + landlines

with open(sr_path, 'w', encoding='utf-8') as f:
    json.dump(sorted_data, f, indent=2, ensure_ascii=False)

print(f"Ordenados com sucesso: {len(mobiles)} celulares no topo, {len(landlines)} fixos ao final. Total: {len(sorted_data)}")
