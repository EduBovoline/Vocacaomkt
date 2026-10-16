import json
import re

with open('auto_responder_docker/data/leads_100_santa_rosalia_brasilandia.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

mobiles = []
for l in data:
    clean = re.sub(r'\D', '', str(l.get('phone', '')))
    if clean.startswith('55159') or (len(clean) == 11 and clean.startswith('159')):
        mobiles.append(l)

print(f"Total Santa Rosalia com celular direto (15 9...): {len(mobiles)}")
for m in mobiles[:5]:
    print(f"- {m['name']} | Cel: {m['phone']} | Endereço: {m.get('address')}")
