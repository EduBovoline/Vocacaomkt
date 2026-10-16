import urllib.request
import json

res = json.loads(urllib.request.urlopen('http://localhost:5680/api/subcrm-data').read().decode())
sr = res.get('santa_rosalia_leads', [])
ht = res.get('high_ticket_leads', [])
print(f"SR Leads: {len(sr)} | HT Leads: {len(ht)} | Total: {len(sr) + len(ht)}")
print("\nPrimeiros 3 leads:")
for l in sr[:3]:
    print(f"- {l['name']} | Cel: {l['phone']} | Maps: {l['maps_url']}")
