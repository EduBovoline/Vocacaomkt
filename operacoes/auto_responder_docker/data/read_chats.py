import json
import sys

ch = json.load(open('auto_responder_docker/data/chat_history.json', 'r', encoding='utf-8'))
for p in ['5511976035867', '5515996683892', '5515998500008', '5515996409494']:
    if p in ch:
        print(f"\n=== CHAT {p} ===")
        for m in ch[p]:
            safe_text = m.get('text', '').encode('ascii', errors='replace').decode('ascii')
            print(f"{m.get('role')}: {safe_text}")
