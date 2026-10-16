import urllib.request
import json

res = json.loads(urllib.request.urlopen('http://localhost:5680/api/subcrm-data').read().decode())
sr = res.get('santa_rosalia_leads', [])

for l in sr[:2]:
    print(f"\n=== {l['name']} (Site: '{l.get('site', '')}') ===")
    print(f"Hook A:\n{l.get('hook_a')}")
