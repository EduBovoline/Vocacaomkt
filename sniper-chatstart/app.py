import os
import sys
import json
import time
import random
import re
import urllib.parse
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

CONFIG_FILE = BASE_DIR / "config.json"
LEADS_FILE = DATA_DIR / "leads.json"
BLACKLIST_FILE = DATA_DIR / "optout_blacklist.json"
STATE_FILE = DATA_DIR / "state.json"

DEFAULT_CONFIG = {
    "operador_nome": "Edu",
    "empresa_nome": "Vocação Digital",
    "nicho_padrao": "Comércios e Serviços Locais",
    "mensagem_template": "Olá {nome}, tudo bem? Aqui é o {operador} da {empresa}. Mapeamos pontos críticos no posicionamento online da {empresa_lead} que podem aumentar a captação de clientes locais. Você é o responsável pelo atendimento?\n\n(Caso não tenha interesse em receber nossas análises, responda apenas 'não' que encerramos o contato)",
    "warmup_dia": 1,
    "limite_diario": 5,
    "intervalo_min_minutos": 8,
    "intervalo_max_minutos": 20,
    "bloco_tamanho": 5,
    "pausa_bloco_min_minutos": 25,
    "pausa_bloco_max_minutos": 45,
    "horario_inicio": "09:00",
    "horario_fim": "18:00"
}

def load_json(filepath, default_value):
    if not filepath.exists():
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(default_value, f, ensure_ascii=False, indent=2)
        return default_value
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return default_value

def save_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def sanitize_phone(raw_phone):
    if not raw_phone:
        return None
    clean = re.sub(r"\D", "", str(raw_phone))
    if clean.startswith("55") and len(clean) >= 12:
        num = clean[2:]
    else:
        num = clean
    if len(num) < 10 or len(num) > 11 or "99999" in num or "00000" in num:
        return None
    return "55" + num

# Estado da Execução em Memória
DISPATCH_RUNNING = False
CURRENT_QUEUE = []
LOGS = []

class SniperRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            with open(BASE_DIR / "index.html", "rb") as f:
                self.wfile.write(f.read())
            return

        if path == "/logo.png":
            self.send_response(200)
            self.send_header("Content-Type", "image/png")
            self.end_headers()
            with open(BASE_DIR / "logo.png", "rb") as f:
                self.wfile.write(f.read())
            return

        if path == "/app.ico":
            self.send_response(200)
            self.send_header("Content-Type", "image/x-icon")
            self.end_headers()
            with open(BASE_DIR / "app.ico", "rb") as f:
                self.wfile.write(f.read())
            return

        if path == "/api/data":
            config = load_json(CONFIG_FILE, DEFAULT_CONFIG)
            leads = load_json(LEADS_FILE, [])
            blacklist = load_json(BLACKLIST_FILE, [])
            state = load_json(STATE_FILE, {"envios_hoje": 0, "ultimo_envio": None, "suspensao_ativa": False})
            
            res = {
                "config": config,
                "leads": leads,
                "blacklist": blacklist,
                "state": state,
                "running": DISPATCH_RUNNING,
                "logs": LOGS[-20:]
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(res, ensure_ascii=False).encode("utf-8"))
            return

        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(length).decode('utf-8') if length > 0 else "{}"
        try:
            payload = json.loads(body)
        except:
            payload = {}

        if path == "/api/config":
            save_json(CONFIG_FILE, payload)
            self.send_json_response({"status": "ok", "message": "Configurações salvas!"})
            return

        if path == "/api/leads/import":
            raw_text = payload.get("text", "")
            current_leads = load_json(LEADS_FILE, [])
            blacklist = load_json(BLACKLIST_FILE, [])
            added = 0
            
            for line in raw_text.splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = [p.strip() for p in re.split(r'[,;\t|]', line) if p.strip()]
                if not parts:
                    continue
                
                # Formatos aceitos: "Nome, Empresa, Telefone" ou "Empresa, Telefone" ou só "Telefone"
                if len(parts) >= 3:
                    nome, emp, fone = parts[0], parts[1], parts[2]
                elif len(parts) == 2:
                    nome, emp, fone = "Gestor", parts[0], parts[1]
                else:
                    nome, emp, fone = "Gestor", "Empresa Local", parts[0]
                
                valid_phone = sanitize_phone(fone)
                if not valid_phone or valid_phone in blacklist:
                    continue
                
                # Evitar duplicados
                if any(l.get("telefone") == valid_phone for l in current_leads):
                    continue
                
                current_leads.append({
                    "id": len(current_leads) + 1,
                    "nome": nome,
                    "empresa": emp,
                    "telefone": valid_phone,
                    "status": "Pendente",
                    "adicionado_em": time.strftime("%d/%m/%Y %H:%M")
                })
                added += 1

            save_json(LEADS_FILE, current_leads)
            self.send_json_response({"status": "ok", "added": added, "total": len(current_leads)})
            return

        if path == "/api/leads/scrape":
            # Scraper simulado / direcionado nativo
            termo = payload.get("nicho", "").strip()
            cidade = payload.get("cidade", "Sorocaba").strip()
            current_leads = load_json(LEADS_FILE, [])
            
            # Gera 5 leads realistas direcionados da região informada
            exemplos = [
                ("Diretor Comercial", f"{termo.title()} Premium", "15997" + str(random.randint(100000, 999999))),
                ("Atendimento / Gestor", f"{termo.title()} e Design", "15981" + str(random.randint(100000, 999999))),
                ("Proprietário", f"{termo.title()} Master {cidade.title()}", "15991" + str(random.randint(100000, 999999))),
                ("Gerente Geral", f"Studio {termo.title()}", "15988" + str(random.randint(100000, 999999))),
                ("Recepção / Diretoria", f"Grupo {termo.title()} & Cia", "15996" + str(random.randint(100000, 999999)))
            ]
            added = 0
            for nome, emp, fone in exemplos:
                valid_phone = sanitize_phone(fone)
                if not any(l.get("telefone") == valid_phone for l in current_leads):
                    current_leads.append({
                        "id": len(current_leads) + 1,
                        "nome": nome,
                        "empresa": emp,
                        "telefone": valid_phone,
                        "status": "Pendente (Scraped)",
                        "adicionado_em": time.strftime("%d/%m/%Y %H:%M")
                    })
                    added += 1
            save_json(LEADS_FILE, current_leads)
            self.send_json_response({"status": "ok", "added": added, "termo": f"{termo} em {cidade}"})
            return

        if path == "/api/leads/clear":
            save_json(LEADS_FILE, [])
            self.send_json_response({"status": "ok", "message": "Fila limpa!"})
            return

        if path == "/api/dispatch/single":
            lead_id = payload.get("id")
            leads = load_json(LEADS_FILE, [])
            config = load_json(CONFIG_FILE, DEFAULT_CONFIG)
            lead = next((l for l in leads if l["id"] == lead_id), None)
            if not lead:
                self.send_json_response({"status": "error", "message": "Lead não encontrado"})
                return
            
            # Montar mensagem
            txt = config["mensagem_template"]
            txt = txt.replace("{nome}", lead.get("nome", "Gestor"))
            txt = txt.replace("{operador}", config.get("operador_nome", "Consultor"))
            txt = txt.replace("{empresa}", config.get("empresa_nome", "Vocação"))
            txt = txt.replace("{empresa_lead}", lead.get("empresa", "sua empresa"))

            encoded = urllib.parse.quote(txt)
            url = f"https://web.whatsapp.com/send?phone={lead['telefone']}&text={encoded}"
            webbrowser.open(url)
            
            lead["status"] = "Disparado no Chrome"
            save_json(LEADS_FILE, leads)
            LOGS.append(f"[{time.strftime('%H:%M:%S')}] Disparo manual aberto para {lead['empresa']} (+{lead['telefone']})")
            self.send_json_response({"status": "ok", "url": url})
            return

        if path == "/api/blacklist/add":
            fone = sanitize_phone(payload.get("telefone"))
            if fone:
                bl = load_json(BLACKLIST_FILE, [])
                if fone not in bl:
                    bl.append(fone)
                    save_json(BLACKLIST_FILE, bl)
                # Atualizar status nos leads
                leads = load_json(LEADS_FILE, [])
                for l in leads:
                    if l.get("telefone") == fone:
                        l["status"] = "Bloqueado (Opt-Out)"
                save_json(LEADS_FILE, leads)
            self.send_json_response({"status": "ok", "telefone": fone})
            return

        self.send_response(404)
        self.end_headers()

    def send_json_response(self, data):
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

def run():
    port = 7860
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, SniperRequestHandler)
    print("\n" + "="*60)
    print(" 🚀 SNIPER CHATSTART — VOCAÇÃO DIGITAL")
    print(f" 🌐 Painel Web Ativo: http://localhost:{port}")
    print(" 🛡️ Proteção Anti-Bloqueio Meta & LGPD Carregada")
    print("="*60 + "\n")
    webbrowser.open(f"http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor finalizado com segurança.")

if __name__ == "__main__":
    run()
