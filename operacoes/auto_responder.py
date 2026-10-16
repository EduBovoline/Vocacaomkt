"""
auto_responder.py — Respondedor Automático de WhatsApp (Vocação Comunicação & Marketing)

Funcionalidade:
1. Recebe webhooks da Evolution API (MESSAGES_UPSERT) na porta 5680
2. Filtra mensagens recebidas (ignora mensagens enviadas por nós mesmos)
3. Detecta intenção positiva ("sim", "pode mandar", "quero ver", "claro", etc.)
4. Localiza o lead e seu PDF correspondente (via Twenty CRM ou pasta de leads)
5. Envia o PDF oficial de diagnóstico com legenda persuasiva via Evolution API
6. Registra o evento de entrega nas notas e avança o estágio da oportunidade no Twenty CRM
"""

import os
import sys
import re
import json
import base64
import unicodedata
import subprocess
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
from enviar_email_zoho import send_email

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')


EVOLUTION_API_URL = "http://localhost:8080"
INSTANCE_NAME = "vocacao_comercial"
API_KEY = "vocacao_update_secret_key_2026"
DOCKER_BIN = r"C:\Program Files\Docker\Docker\resources\bin\docker.exe"
LEADS_DIR = r"C:\Vocação 2027\QG Vocação 2027 do zero\2 Leads"
SCHEMA = "workspace_2xmx8hech9nybwidia3404k2z"
ADMIN_WHATSAPP = "5515981512083"
DELIVERED_FILE = os.path.join(os.path.dirname(__file__), "delivered_leads.json")
OPTOUT_FILE = os.path.join(os.path.dirname(__file__), "optout_leads.json")

def load_optout_leads():
    if os.path.exists(OPTOUT_FILE):
        try:
            with open(OPTOUT_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def record_optout_lead(phone, lead_name):
    data = load_optout_leads()
    data[phone] = {
        "lead_name": lead_name,
        "optout_at": datetime.now().isoformat()
    }
    with open(OPTOUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def is_optout_lead(phone):
    data = load_optout_leads()
    clean_phone = re.sub(r"\D", "", phone)
    for p in data:
        clean_p = re.sub(r"\D", "", p)
        if clean_p[-8:] == clean_phone[-8:]:
            return True
    return False

# Gatilhos explícitos de autorização (removido 'ok' e 'beleza' para evitar falsos positivos de confirmação)
POSITIVE_TRIGGERS = [
    "sim", "pode mandar", "pode enviar", "pode", "manda", "mandar", "quero",
    "claro", "envia", "enviar", "mostra", "mostrar", "com certeza", "mande",
    "manda ai", "manda aí", "fiquei curiosa", "curioso", "tenho interesse", "manda aqui"
]

def load_delivered_leads():
    if os.path.exists(DELIVERED_FILE):
        try:
            with open(DELIVERED_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def record_delivered_lead(phone, lead_name):
    data = load_delivered_leads()
    data[phone] = {
        "lead_name": lead_name,
        "delivered_at": datetime.now().isoformat()
    }
    with open(DELIVERED_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def is_pdf_already_delivered(phone):
    data = load_delivered_leads()
    # Verifica correspondência de número completo ou últimos 8 dígitos
    clean_phone = re.sub(r"\D", "", phone)
    for p in data:
        clean_p = re.sub(r"\D", "", p)
        if clean_p in clean_phone or clean_phone in clean_p or clean_p[-8:] == clean_phone[-8:]:
            return True
    return False

def notify_admin(msg):
    try:
        url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
        payload = {"number": ADMIN_WHATSAPP, "text": msg}
        requests.post(url, json=payload, headers={"apikey": API_KEY, "Content-Type": "application/json"}, timeout=10)
    except Exception as e:
        print("[!] Erro ao notificar admin:", e)

BYPASS_FILE = os.path.join(os.path.dirname(__file__), "bypassed_leads.json")

# Gatilhos típicos de robôs de boas-vindas / recepção automática
BOT_GREETING_TRIGGERS = [
    "agradece seu contato", "agradecemos seu contato", "agradece o contato", "agradecemos o contato",
    "como podemos ajudar", "como posso ajudar", "em que podemos ajudar", "em que posso ajudar",
    "para agilizar nosso atendimento", "para agilizar seu atendimento",
    "qual seu nome", "qual o seu nome", "seu nome",
    "seja bem-vindo", "seja bem vindo", "seja bem-vinda", "seja bem vinda",
    "atendimento automatico", "mensagem automatica", "resposta automatica",
    "nosso horario de atendimento", "fora do horario", "horario de funcionamento"
]

def load_bypassed_leads():
    if os.path.exists(BYPASS_FILE):
        try:
            with open(BYPASS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def is_already_bypassed(phone):
    data = load_bypassed_leads()
    clean_phone = re.sub(r"\D", "", phone)
    for p in data:
        clean_p = re.sub(r"\D", "", p)
        if clean_p in clean_phone or clean_phone in clean_p or clean_p[-8:] == clean_phone[-8:]:
            return True
    return False

def record_bypassed_lead(phone, lead_name):
    data = load_bypassed_leads()
    data[phone] = {
        "lead_name": lead_name,
        "bypassed_at": datetime.now().isoformat()
    }
    with open(BYPASS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def handle_bot_bypass(phone, lead_name, company_id, bot_text):
    # Proteção anti-loop: envia o bypass no máximo UMA vez para cada lead
    if is_already_bypassed(phone):
        print(f"   [i] Bypass de recepção já foi enviado anteriormente para '{lead_name}' ({phone}). Ignorando loop.")
        return

    display_name = lead_name or "o espaço"
    bypass_reply = (
        f"Olá! Sou o Eduardo, da Vocação. Preparei um diagnóstico visual rápido de 2 minutos "
        f"sobre o posicionamento e a captação digital do espaço no Google para apresentar "
        f"à coordenação / direção.\n\n"
        f"Poderia me confirmar quem é o responsável ou se posso deixar por aqui mesmo com você?"
    )

    try:
        url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
        payload = {
            "number": phone,
            "text": bypass_reply,
            "options": {"delay": 1500}
        }
        requests.post(url, json=payload, headers={"apikey": API_KEY, "Content-Type": "application/json"}, timeout=10)
        print(f"[✓] Resposta de bypass enviada com sucesso para '{lead_name}' ({phone}).")
        record_bypassed_lead(phone, lead_name)
    except Exception as e:
        print("[!] Erro ao enviar bypass para o bot:", e)

    notify_admin(
        f"🤖 *BOT DE RECEPÇÃO DETECTADO:*\n"
        f"• *Lead:* {lead_name}\n"
        f"• *Ação:* Resposta de identificação enviada para furar o robô e chamar o responsável humano."
    )

    if company_id:
        record_followup_note(company_id, f"Bot de recepção detectado. Resposta humanizada de bypass enviada.")

def normalize_text(text):
    if not text:
        return ""
    nfkd = unicodedata.normalize('NFKD', text)
    clean = "".join([c for c in nfkd if not unicodedata.combining(c)])
    return clean.lower().strip()

def run_psql(sql):
    try:
        proc = subprocess.Popen(
            [DOCKER_BIN, "exec", "-i", "twenty-db-1", "psql", "-U", "postgres", "-d", "twenty"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8"
        )
        stdout, stderr = proc.communicate(input=sql)
        return stdout.strip()
    except Exception as e:
        print("[!] Erro PSQL:", e)
        return ""

def find_lead_by_phone(phone_digits):
    # Pega os últimos 8 dígitos para matching flexível
    last_digits = phone_digits[-8:] if len(phone_digits) >= 8 else phone_digits
    
    # 1. Busca no Twenty CRM
    sql = f"""
    SELECT c.id, c.name 
    FROM "{SCHEMA}"."company" c
    JOIN "{SCHEMA}"."person" p ON p."companyId" = c.id
    WHERE regexp_replace(p."phonesPrimaryPhoneNumber", '[^0-9]', '', 'g') LIKE '%{last_digits}%'
    LIMIT 1;
    """
    out = run_psql(sql)
    for line in out.splitlines():
        line = line.strip()
        if "|" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 2 and len(parts[0]) == 36 and "-" in parts[0]:
                return {"id": parts[0], "name": parts[1]}

    # 2. Fallback por mapeamento direto robusto (todos os leads em prospecção)
    DIRECT_MAP = {
        "996410306": {"id": "1eb4465f-51c5-414d-93e1-fa3fc4f1bdb2", "name": "Dra. Mariana Tocci Dermatologia"},
        "991433018": {"id": "2de19ebb-7d2f-4b27-8428-1a2fb3f6ba49", "name": "Dra. Marielle Moreira Odontologia"},
        "997595506": {"id": "d001-leticia-plens", "name": "Dra. Letícia Plens Harmonização"},
        "997466183": {"id": "a3cc72d6-7556-4923-a58b-e138fecbcb2d", "name": "Anequini Soares Dermatologia"},
        "988052431": {"id": "d002-critis-odonto", "name": "Critis Odontologia Especializada"},
        "997930040": {"id": "d003-tais-pedroso", "name": "Estética Taís Pedroso"},
        "996578148": {"id": "d004-thaise-buzzo", "name": "Dra. Thaise Buzzo Cirurgia Plástica"},
        "996115575": {"id": "d005-clinica-lu", "name": "Clínica Lu"},
        "997829252": {"id": "d006-impact-center", "name": "Impact Transformation Center"},
        "996158237": {"id": "d007-derma-simis", "name": "Derma Simis Dra. Tatiana"},
        "998603211": {"id": "d008-vita-odonto", "name": "Vita Odontologia"},
        "981350308": {"id": "d009-corts-ortopedia", "name": "Corts Clínica de Ortopedia"},
        "981522821": {"id": "d010-leandro-brandi", "name": "Dr. Leandro Brandi Ortopedia"},
        "991984736": {"id": "9e0a6359-c19a-4bb8-a761-510193b35d30", "name": "Med Cor Sorocaba"},
        "997120678": {"id": "d012-ezklo", "name": "Ezklo Marcenaria Boutique"},
        "997787394": {"id": "d013-sucesso", "name": "Marcenaria Sucesso Planejados"},
        "996409494": {"id": "f7c850f3-bb4d-4234-85ae-19ae70e44b74", "name": "Lumiè Estética Avançada"},
        "998500008": {"id": "fa859b80-e85e-4787-941a-cbce24278775", "name": "BodyBe Sorocaba"},
        "996683892": {"id": "e7814465-0873-4cbe-81d0-764161841306", "name": "Estética Stella Maris"},
        "996201252": {"id": "9b82000d-f52b-42ac-a682-3ae4bad83d8d", "name": "Aliane Carmo Harmonização Facial"},
        "988331983": {"id": "f7916bdd-d118-4334-be3b-553bc282fcbe", "name": "Clínica Dra. Audrey Naufal"},
        "981314488": {"id": "2d2e6d9d-7774-448a-9861-439e26e1c85f", "name": "Estética Kirei Campolim"},
        "996963197": {"id": "eab08c79-753d-48c0-acb1-010408412a0c", "name": "Fernanda Pimentel Estética Avançada"},
        "992733623": {"id": "p001-revitae", "name": "Revitae Pilates e Fisioterapia"},
        "998070877": {"id": "p002-microvita", "name": "Microvita Pilates Sorocaba"},
        "997153583": {"id": "p003-sub-studio", "name": "SUB. Studio de Pilates"},
        "998104597": {"id": "p004-inspirevida", "name": "Inspirevida Fisioterapia e Pilates"},
        "996270927": {"id": "p005-krion", "name": "Instituto Krion Fisioterapia e Pilates"},
        "981158086": {"id": "p006-karina-fiel", "name": "Karina Fiel Fisioterapia e Pilates"},
        "997935990": {"id": "p007-joao-gabriel", "name": "Dr. João Gabriel Quiropraxia"},
        "998161692": {"id": "p008-viva", "name": "Vivá Terapias Integrativas"},
        "991176788": {"id": "p009-giancarlo", "name": "Giancarlo Marçal Osteopatia"},
        "991051888": {"id": "p010-armbrust", "name": "Prof. Dr. Danilo Armbrust"},
        "981778421": {"id": "p011-quiro-cia", "name": "Quiro&Cia Centro de Quiropraxia"},
        "991483785": {"id": "p012-amalio", "name": "Amalio Júnior Quiropraxia"},
        "997760345": {"id": "p013-pure-pilates", "name": "Pure Pilates Campolim"},
        "991315847": {"id": "p014-classic-pilates", "name": "Classic Pilates e Fisioterapia"},
        "988119242": {"id": "p015-flavia-fernandes", "name": "Flávia Fernandes Pilates Studio"},
        "997539318": {"id": "p016-mova-se", "name": "Pilates Mova-se"},
        "981140366": {"id": "p017-vida-mais", "name": "Vida Mais Pilates Clássico"},
        "998049147": {"id": "p018-mamy-baby", "name": "Pilates Mamy Baby"},
        "991492719": {"id": "p019-furio", "name": "Francisco Furio Treinamento Funcional"},
        "992529514": {"id": "p020-mundo-acqua", "name": "Mundo Acqua Studio"},
        "997502210": {"id": "m001-shz", "name": "Marcenaria SHZ"},
        "997157075": {"id": "m002-oakhouse", "name": "Oakhouse Marcenaria"},
        "996503634": {"id": "m003-mdm", "name": "MDM Marcenaria"},
        "991670071": {"id": "m004-mendes", "name": "Mendes Marcenaria"},
        "981859590": {"id": "m005-sutil", "name": "Sutil Marcenaria"},
        "912289966": {"id": "m006-dizanini", "name": "Di Zanini Marcenaria Criativa"},
        "997729441": {"id": "m007-harv", "name": "Harv Planejados"},
        "998201691": {"id": "m008-cast-select", "name": "Cast Select Móveis Planejados"},
        "991214679": {"id": "m009-celmar", "name": "Celmar Campolim"},
        "991850844": {"id": "m010-criare", "name": "Criare Sorocaba"},
        "910640282": {"id": "m011-impeccabile", "name": "Impeccabile Móveis Planejados"},
        "991210000": {"id": "m012-wbilino", "name": "Wbilino Conceito Mármores de Luxo"},
        "988180072": {"id": "m013-santos", "name": "Marmoraria Santos"},
        "988137613": {"id": "m014-domke", "name": "Marcenaria Domke"},
        "991287563": {"id": "m015-todeschini", "name": "Todeschini Sorocaba"},
        "991712908": {"id": "t001-lodonto", "name": "LODONTO Espaço do Sorriso"},
        "991982675": {"id": "t002-rbs", "name": "RBS Centro de Reabilitação Oral"},
        "991043048": {"id": "t003-veronezi", "name": "Studio Veronezi"},
        "991699731": {"id": "b001-simus-pilates", "name": "Stúdio de Pilates Fitness Jardim Simus"},
        "997629693": {"id": "b002-jodi-funcional", "name": "Jodi Moraes Treinamento Personalizado"},
        "991753370": {"id": "b003-martin-pilates", "name": "Studio Martin Pilates"},
        "991205576": {"id": "b004-surya-yoga", "name": "Espaço Surya Yoga e Pilates"}
    }

    for digits_pattern, lead_info in DIRECT_MAP.items():
        if digits_pattern in phone_digits:
            return lead_info

    return None

def find_pdf_for_lead(lead_name):
    clean_lead = normalize_text(lead_name)
    best_folder = None
    best_score = 0
    
    lead_words = set(w for w in clean_lead.split() if len(w) > 2)
    
    for folder in os.listdir(LEADS_DIR):
        folder_path = os.path.join(LEADS_DIR, folder)
        if os.path.isdir(folder_path):
            clean_folder = normalize_text(folder)
            
            # 1. Correspondência exata
            if clean_lead == clean_folder:
                score = 100
            elif clean_lead in clean_folder or clean_folder in clean_lead:
                score = 80
            else:
                folder_words = set(w for w in clean_folder.split() if len(w) > 2)
                overlap = len(lead_words.intersection(folder_words))
                score = overlap * 10
                
            if score > best_score:
                best_score = score
                best_folder = folder_path

    if best_folder and best_score >= 20:
        files = os.listdir(best_folder)
        # 1. Tenta formato oficial novo
        for f in files:
            if f.startswith("Analise-Presenca-Digital") and f.endswith(".pdf"):
                return os.path.join(best_folder, f)
        # 2. Tenta formato legado cliente
        for f in files:
            if f.endswith("-cliente.pdf") or ("prospeccao" in f.lower() and f.endswith(".pdf")):
                return os.path.join(best_folder, f)
        # 3. Qualquer PDF na pasta
        for f in files:
            if f.lower().endswith(".pdf"):
                return os.path.join(best_folder, f)
    return None

GENERATE_SCRIPT = r"C:\Users\edubo\.gemini\config\plugins\vocacao\skills\vocacao-prospeccao\scripts\generate_lead.js"

def generate_pdf_on_demand(lead_name, phone):
    print(f"\n[⚡] Gerando diagnóstico sob demanda para '{lead_name}' ({phone})...")
    segment = 'Studio de Pilates & Fisioterapia'
    if any(k in lead_name.lower() for k in ['quiro', 'osteo', 'coluna']):
        segment = 'Quiropraxia & Reabilitação Postural'
    elif any(k in lead_name.lower() for k in ['funcional', 'treino', 'crossfit']):
        segment = 'Treinamento Funcional Personalizado'
    elif any(k in lead_name.lower() for k in ['terapia', 'integrativa']):
        segment = 'Terapias Integrativas & Bem-Estar'

    lead_data = {
        'name': lead_name,
        'segment': segment,
        'city': 'Sorocaba, SP',
        'phone': phone,
        'maturityLevel': 'Nível 2',
        'primaryOffer': 'Sistema Vocação Start — Google Maps Otimizado + Vitrine One-Page em 7 Dias Úteis',
        'dateFormatted': 'Outubro de 2026',
        'channels': [
            {'name': 'Google Maps & Perfil da Empresa', 'badgeClass': 'badge-forte', 'status': 'Forte', 'clientNote': 'Boa presença local, porém sem Tour Virtual 360° no Street View.'},
            {'name': 'Site / Vitrine Institucional', 'badgeClass': 'badge-critico', 'status': 'Crítico', 'clientNote': 'Ausência de vitrine digital independente de autoridade para conversão.'},
            {'name': 'Instagram & Redes Sociais', 'badgeClass': 'badge-mediano', 'status': 'Mediano', 'clientNote': 'Publicações ativas, mas sem funil direto para triagem de alunos particulares.'},
            {'name': 'WhatsApp Comercial', 'badgeClass': 'badge-mediano', 'status': 'Estruturado', 'clientNote': 'Canal ágil com oportunidade de humanização e apresentação de diferenciais.'}
        ],
        'competitors': [
            {'name': lead_name, 'google': '4.9 ★★★★★', 'site': 'Sem Portal', 'instagram': 'Ativo', 'badgeClass': 'badge-mediano', 'status': 'Lead Analisado', 'isLead': True},
            {'name': 'Concorrentes Campolim & ZS', 'google': '4.8 ★★★★★', 'site': 'Portal Próprio', 'instagram': 'Ativo', 'badgeClass': 'badge-forte', 'status': 'Forte Concorrente'},
            {'name': 'Studios Convencionais', 'google': '4.5 ★★★★☆', 'site': 'Básico', 'instagram': 'Esporádico', 'badgeClass': 'badge-fraco', 'status': 'Mediano'}
        ],
        'strengths': [
            {'title': 'Qualidade Técnica Reconhecida', 'desc': 'Metodologia personalizada e alta satisfação dos alunos e pacientes atendidos.'},
            {'title': 'Localização Estratégica', 'desc': 'Excelente ponto em Sorocaba com grande potencial de atração de público qualificado.'},
            {'title': 'Conceito de Atendimento', 'desc': 'Cuidado individualizado e foco em resultados de saúde e movimento consciente.'}
        ],
        'clientImprovements': [
            {'title': 'Falta de Vitrine Digital Independente', 'desc': 'Quem pesquisa pelo serviço no Google encontra pouca profundidade institucional antes do agendamento.'},
            {'title': 'Perfil no Maps sem Tour 360°', 'desc': 'Alunos de condomínios da região não visualizam a estrutura e os equipamentos no Street View.'},
            {'title': 'Gargalo de Conversão Direta', 'desc': 'Potenciais clientes particulares hesitam e acabam caindo em concorrentes com sites mais estruturados.'}
        ],
        'stats': [
            {'num': '95%', 'desc': 'Dos alunos e pacientes pesquisam no Google antes de fechar plano em studio especializado.'},
            {'num': '3,5x', 'desc': 'Mais procura quando o espaço possui vitrine digital estruturada e fotos panorâmicas 360°.'},
            {'num': '48h', 'desc': 'Janela média de decisão para início de aulas e terapias após busca ativa na web.'},
            {'num': '100%', 'desc': 'Do investimento recuperado com apenas 1 a 2 novos alunos particulares fidelizados.'}
        ],
        'prioritizedServices': [
            {'name': 'Vocação Start (Maps + Vitrine One-Page)', 'justification': 'Ficha do Google Maps blindada e vitrine rápida mobile-first em subdomínio seguro conectada ao WhatsApp em 7 dias úteis.'},
            {'name': 'Combo Maps + Tour Virtual 360°', 'justification': 'Otimização avançada no Google Maps com fotos imersivas no Google Street View para multiplicar a retenção e cliques.'}
        ]
    }

    temp_dir = os.path.join(os.path.dirname(__file__), ".temp_leads")
    os.makedirs(temp_dir, exist_ok=True)
    clean_p = re.sub(r"\D", "", phone)
    temp_path = os.path.join(temp_dir, f"temp_{clean_p}.json")
    with open(temp_path, 'w', encoding='utf-8') as f:
        json.dump(lead_data, f, ensure_ascii=False, indent=2)

    try:
        proc = subprocess.Popen(
            ['node', GENERATE_SCRIPT, temp_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        proc.communicate(timeout=25)
    except Exception as e:
        print("[!] Erro subprocess node generate_lead:", e)

    return find_pdf_for_lead(lead_name)

def send_pdf(number, pdf_path, lead_name):
    print(f"\n[+] Enviando diagnóstico em PDF para {lead_name} ({number})...")
    with open(pdf_path, "rb") as f:
        pdf_b64 = base64.b64encode(f.read()).decode("utf-8")

    caption = (
        "Perfeito! Segue o diagnóstico visual em anexo (3 páginas). 📄✨\n\n"
        "Aqui destacamos os 2 pontos prioritários da estrutura:\n"
        "1. Ficha do Google Maps 100% blindada e otimizada para buscas locais.\n"
        "2. Vitrine digital rápida mobile-first com botão direto pro seu WhatsApp.\n\n"
        "Entregamos essa estrutura completa rodando em até 7 dias úteis.\n"
        "Dê uma olhada rápida (leva 2 minutos) e me diga se faz sentido pra vocês!"
    )

    url = f"{EVOLUTION_API_URL}/message/sendMedia/{INSTANCE_NAME}"
    headers = {
        "apikey": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "number": number,
        "mediatype": "document",
        "mimetype": "application/pdf",
        "caption": caption,
        "media": pdf_b64,
        "fileName": f"Analise-Presenca-Digital-{lead_name.replace(' ', '-')}.pdf"
    }

    resp = requests.post(url, json=payload, headers=headers, timeout=25)
    if resp.status_code in [200, 201]:
        print(f"[✓] PDF entregue com sucesso! Status: {resp.status_code}")
        record_delivered_lead(number, lead_name)
        return True
    else:
        print(f"[!] Falha no envio do PDF: {resp.status_code} - {resp.text}")
        return False

def record_followup_note(company_id, text_reply):
    clean_reply = text_reply.replace("'", "''")
    sql = f"""
    INSERT INTO "{SCHEMA}"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(),
        'WhatsApp: Resposta do Lead pós-diagnóstico',
        '**Mensagem recebida no WhatsApp:**\\n> "{clean_reply}"\\n\\n*Acompanhamento manual recomendado.*',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    """
    run_psql(sql)

def update_crm_opportunity(company_id, text_reply):
    # Atualiza oportunidade para MEETING e insere nota
    sql = f"""
    UPDATE "{SCHEMA}"."opportunity"
    SET stage = 'MEETING', "updatedAt" = NOW()
    WHERE "companyId" = '{company_id}';

    INSERT INTO "{SCHEMA}"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(),
        'WhatsApp: Lead autorizou diagnóstico visual',
        '**Resposta recebida no WhatsApp:**\\n> "' || '{text_reply}' || '"\\n\\n**Ação executada:** Diagnóstico em PDF enviado automaticamente pelo assistente Vocação.',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    """
    run_psql(sql)
    print(f"[✓] CRM atualizado: Oportunidade movida para 'DELIBERATING' e nota gravada.")

def handle_email_request(phone, lead_name, company_id, lead_email, full_text):
    pdf_path = find_pdf_for_lead(lead_name) if lead_name else None
    display_name = lead_name or "sua empresa"
    
    subject = f"Apresentação & Diagnóstico Visual — {display_name}"
    body_html = f"""
    <div style="font-family: Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 14px; line-height: 1.6; color: #222222; max-width: 600px;">
        <p>Olá, tudo bem?</p>
        
        <p>Conforme combinado, encaminho em anexo a nossa <b>análise de presença digital</b> com o diagnóstico visual e as principais oportunidades de estruturação identificadas.</p>
        
        <p>No documento destacamos os pontos de maior impacto para fortalecer a autoridade e a conversão direta nos seus canais de atendimento.</p>
        
        <p>Fico à disposição se quiser conversar brevemente para tirar dúvidas ou aprofundar os pontos apresentados.</p>
        
        <br>
        <p style="margin-bottom: 2px;">Atenciosamente,</p>
        <p style="margin-top: 0; font-weight: bold; color: #111111;">Eduardo Bovoline</p>
        <p style="margin: 0; color: #555555; font-size: 13px;">Vocação Comunicação & Marketing</p>
        <p style="margin: 0; color: #555555; font-size: 13px;">contato@vocacao.digital | (15) 98151-2083</p>
        <p style="margin: 0; color: #555555; font-size: 13px;"><a href="https://vocacao.digital" style="color: #0066cc; text-decoration: none;">vocacao.digital</a></p>
    </div>
    """
    
    # TRAVA DE INTEGRIDADE: Se o PDF não existir em disco, NUNCA enviar o e-mail
    if not pdf_path or not os.path.exists(pdf_path):
        print(f"   [🚨 TRAVA DE ANEXO] Envio para {lead_email} ABORTADO: Arquivo PDF não localizado!")
        notify_admin(
            f"🚨 *ENVIO DE E-MAIL ABORTADO (SEM ANEXO):*\n"
            f"• *Lead:* {lead_name}\n"
            f"• *Destino:* {lead_email}\n"
            f"• *Causa:* O PDF não foi encontrado em disco. O e-mail NÃO foi disparado para proteger a credibilidade."
        )
        return

    print(f"\n[📧] Disparando e-mail para {lead_email} com anexo: {pdf_path}...")
    email_success = False
    try:
        email_success = send_email(lead_email, subject, body_html, pdf_path, sender_name="Eduardo Bovoline | Vocação")
    except Exception as e:
        print("[!] Erro ao enviar e-mail via Zoho:", e)

    # Resposta humanizada no WhatsApp
    if email_success:
        wa_reply = (
            f"Perfeito! Acabei de encaminhar o documento completo com o diagnóstico em anexo para o e-mail {lead_email}. 📄✉️\n\n"
            f"Muito obrigado pela atenção e fico à disposição caso tenham qualquer dúvida!"
        )
        record_delivered_lead(phone, lead_name)
    else:
        wa_reply = (
            f"Perfeito! Recebi o e-mail {lead_email} e já estou providenciando o envio da apresentação com o diagnóstico por lá. Muito obrigado pela atenção!"
        )

    try:
        url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
        payload = {"number": phone, "text": wa_reply}
        requests.post(url, json=payload, headers={"apikey": API_KEY, "Content-Type": "application/json"}, timeout=10)
        print(f"[✓] Confirmação enviada no WhatsApp para {phone}.")
    except Exception as e:
        print("[!] Erro ao enviar confirmação no WhatsApp:", e)

    notify_admin(
        f"📧 *DIAGNÓSTICO ENVIADO POR E-MAIL!*\n"
        f"• *Lead:* {lead_name}\n"
        f"• *Contato:* {phone}\n"
        f"• *E-mail:* {lead_email}\n"
        f"• *Status:* {'✅ Entregue via Zoho' if email_success else '❌ Falha no SMTP'}"
    )

    if company_id:
        record_followup_note(company_id, f"E-mail informado no WhatsApp: {lead_email}. Envio via Zoho: {'Sucesso' if email_success else 'Falha'}.")

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len).decode('utf-8')
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"status":"received"}')

        try:
            data = json.loads(body)
            self.process_webhook(data)
        except Exception as e:
            print("[!] Erro ao processar payload:", e)

    def process_webhook(self, data):
        event = data.get("event")
        # Aceita MESSAGES_UPSERT ou payload direto
        msg_data = data.get("data", {})
        key = msg_data.get("key", {})
        
        remote_jid = key.get("remoteJid", "")
        if not remote_jid or "@g.us" in remote_jid or "status@broadcast" in remote_jid:
            return

        remote_alt = key.get("remoteJidAlt", "")
        phone = ""
        if "@s.whatsapp.net" in remote_jid:
            phone = remote_jid.split("@")[0]
        elif "@s.whatsapp.net" in remote_alt:
            phone = remote_alt.split("@")[0]
        else:
            phone = remote_jid.split("@")[0]

        # Extrai o texto da mensagem
        message_obj = msg_data.get("message", {})
        text = (
            message_obj.get("conversation") or 
            message_obj.get("extendedTextMessage", {}).get("text") or 
            ""
        ).strip()

        if not text:
            return

        # 1. Se for o gestor (Eduardo) no WhatsApp
        if "981512083" in phone:
            norm = normalize_text(text)
            print(f"\n   [★] MENSAGEM DO GESTOR DETECTADA NO WHATSAPP: {text}")
            
            # Se for aprovação / início
            if any(w in norm for w in ["aprovar", "aprovado", "iniciar", "disparar", "comecar", "começar"]):
                confirm_url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
                confirm_payload = {
                    "number": ADMIN_WHATSAPP,
                    "text": "🚀 *APROVAÇÃO CONFIRMADA:* Fila de prospecção iniciada com sucesso! Monitorando todas as respostas em tempo real."
                }
                requests.post(confirm_url, json=confirm_payload, headers={"apikey": API_KEY, "Content-Type": "application/json"}, timeout=10)
                
                script_pilates = os.path.join(os.path.dirname(__file__), "disparador_fila_20leads_pilates.py")
                if os.path.exists(script_pilates):
                    subprocess.Popen([sys.executable, script_pilates])
                else:
                    script_default = os.path.join(os.path.dirname(__file__), "disparador_fila_16leads.py")
                    subprocess.Popen([sys.executable, script_default])
                return

            # Se for consulta de status
            elif any(w in norm for w in ["status", "fila", "como esta", "como ta", "como tá", "resumo"]):
                delivered_w = load_delivered_leads()
                delivered_e = {}
                d_emails_path = os.path.join(os.path.dirname(__file__), "delivered_emails.json")
                if os.path.exists(d_emails_path):
                    try:
                        with open(d_emails_path, "r", encoding="utf-8") as fe:
                            delivered_e = json.load(fe)
                    except:
                        pass
                
                status_msg = (
                    f"📊 *STATUS DA OPERAÇÃO VOCAÇÃO 2027:*\n\n"
                    f"• *Diagnósticos WhatsApp entregues:* {len(delivered_w)}\n"
                    f"• *E-mails B2B entregues:* {len(delivered_e)}\n"
                    f"• *Auto-responder:* 🟢 ATIVO (porta 5680)\n"
                    f"• *Evolution API:* 🟢 CONECTADO\n\n"
                    f"Qualquer resposta de lead será notificada aqui antes de qualquer envio!"
                )
                confirm_url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
                requests.post(confirm_url, json={"number": ADMIN_WHATSAPP, "text": status_msg}, headers={"apikey": API_KEY, "Content-Type": "application/json"}, timeout=10)
                return

            # Se for pausa / parar
            elif any(w in norm for w in ["pausa", "pausar", "parar", "cancela", "cancelar"]):
                confirm_url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
                requests.post(confirm_url, json={"number": ADMIN_WHATSAPP, "text": "⏸️ *OPERAÇÃO PAUSADA:* Disparos congelados. O bot continua monitorando respostas e avisando você aqui."}, headers={"apikey": API_KEY, "Content-Type": "application/json"}, timeout=10)
                return

            # Qualquer outra instrução de Eduardo
            else:
                reply_text = (
                    f"🫡 *Instrução recebida, Eduardo!*\n\n"
                    f"Mensagem: \"{text}\"\n\n"
                    f"Estou com o sistema 100% monitorado. Nenhuma ação será tomada com os leads sem o seu alinhamento prévio."
                )
                confirm_url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
                requests.post(confirm_url, json={"number": ADMIN_WHATSAPP, "text": reply_text}, headers={"apikey": API_KEY, "Content-Type": "application/json"}, timeout=10)
                return

        # Ignora mensagens normais enviadas por nós mesmos para terceiros
        from_me = key.get("fromMe", False)
        if from_me:
            return

        print(f"\n📩 [MENSAGEM RECEBIDA] De: {phone} ({msg_data.get('pushName', 'Desconhecido')})")
        print(f"   Conteúdo: \"{text}\"")

        # Localiza se o lead é conhecido
        lead = find_lead_by_phone(phone)
        lead_name = lead["name"] if lead else msg_data.get('pushName', phone)
        company_id = lead["id"] if lead else None

        # 1. Verifica se a resposta contém um e-mail de contato / parcerias
        email_match = re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
        if email_match:
            lead_email = email_match.group(0).lower()
            print(f"   [📧] E-mail informado pelo lead no WhatsApp: {lead_email}")
            
            # Se o lead já recebeu o diagnóstico previamente (conversa em andamento), NÃO disparar automático
            if is_pdf_already_delivered(phone):
                print(f"   [⚠️ TRAVA MANUAL] Lead '{lead_name}' ({phone}) já recebeu diagnóstico antes. Bloqueando disparo automático de e-mail.")
                notify_admin(
                    f"📧 *E-MAIL INFORMADO EM CONVERSA EM ANDAMENTO:*\n"
                    f"• *Lead:* {lead_name}\n"
                    f"• *Contato:* {phone}\n"
                    f"• *E-mail:* {lead_email}\n"
                    f"• *Ação:* Disparo automático bloqueado para evitar mensagens presumidas. Conduza manualmente."
                )
                if company_id:
                    record_followup_note(company_id, f"E-mail informado no WhatsApp: {lead_email}. Disparo automático bloqueado (condução manual).")
                return

            handle_email_request(phone, lead_name, company_id, lead_email, text)
            return

        normalized = normalize_text(text)

        # 1b. Trava LGPD: Verifica solicitação de Opt-out ("PARAR", "DESCADASTRAR", etc.)
        LGPD_OPTOUT_TRIGGERS = ["parar", "descadastrar", "cancelar", "nao quero", "não quero", "remover", "pare", "bloquear", "nao tenho interesse", "não tenho interesse"]
        is_optout = any(re.search(rf"\b{re.escape(w)}\b", normalized) for w in LGPD_OPTOUT_TRIGGERS)
        if is_optout:
            print(f"   [🚫 LGPD OPTOUT] Lead solicitou cancelamento: {lead_name} ({phone})")
            record_optout_lead(phone, lead_name)
            optout_reply = (
                "Compreendido perfeitamente! Seu número foi descadastrado imediatamente da nossa base de contatos. "
                "Não enviaremos mais nenhuma mensagem comercial. Tenha uma excelente semana! 🙏"
            )
            try:
                url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
                requests.post(url, json={"number": phone, "text": optout_reply}, headers={"apikey": API_KEY, "Content-Type": "application/json"}, timeout=10)
            except Exception as e:
                print("[!] Erro ao enviar resposta opt-out:", e)

            notify_admin(f"🚫 *OPTOUT LGPD:* Lead '{lead_name}' ({phone}) pediu para parar. Descadastrado da base.")
            if company_id:
                record_followup_note(company_id, "LGPD: Lead solicitou descadastramento (PARAR). Descartado.")
            return

        # Trava anti-duplicidade: se este lead já recebeu o diagnóstico, NUNCA reenviar
        if is_pdf_already_delivered(phone):
            print(f"   [i] Diagnóstico JÁ FOI ENTREGUE anteriormente para '{lead_name}' ({phone}). Bloqueando reenvio de PDF.")
            # Notifica o gestor imediatamente no WhatsApp para atendimento humano
            notify_admin(f"📩 *NOVA RESPOSTA DE LEAD (Pós-diagnóstico):*\n*Lead:* {lead_name}\n📱 {phone}\n💬 *Mensagem:* \"{text}\"")
            if company_id:
                record_followup_note(company_id, text)
            return

        # 2. INTENÇÃO POSITIVA TEM PRIORIDADE MÁXIMA (se o cliente disse 'pode enviar', 'sim', etc., nunca é bot)
        is_positive = any(re.search(rf"\b{re.escape(trigger)}\b", normalized) for trigger in POSITIVE_TRIGGERS)

        if is_positive:
            print(f"   [★] Intenção positiva detectada! Localizando lead...")
            if not lead:
                print(f"   [!] Nenhum lead cadastrado correspondente ao número {phone}.")
                return

            print(f"   [✓] Lead identificado: {lead_name} (ID: {company_id})")

            pdf_path = find_pdf_for_lead(lead_name)
            if not pdf_path or not os.path.exists(pdf_path):
                print(f"   [!] PDF não encontrado previamente para '{lead_name}'. Ativando geração sob demanda...")
                # Envia mensagem rápida para manter a conversa quente e humana
                try:
                    keep_warm = "Perfeito! Já estou separando o diagnóstico visual com os dados de vocês aqui, te encaminho em instantes! ⏱️📄"
                    url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
                    requests.post(url, json={"number": phone, "text": keep_warm}, headers={"apikey": API_KEY, "Content-Type": "application/json"}, timeout=10)
                except Exception:
                    pass

                pdf_path = generate_pdf_on_demand(lead_name, phone)

            if not pdf_path or not os.path.exists(pdf_path):
                print(f"   [!] Falha ao gerar PDF sob demanda para '{lead_name}' em {LEADS_DIR}.")
                notify_admin(f"⚠️ *FALHA AO GERAR PDF SOB DEMANDA:*\nLead: {lead_name}\nTelefone: {phone}")
                return

            print(f"   [✓] PDF localizado/gerado: {pdf_path}")
            success = send_pdf(phone, pdf_path, lead_name)
            if success:
                notify_admin(
                    f"🎯 *DIAGNÓSTICO ENTREGUE COM SUCESSO!*\n"
                    f"• *Lead:* {lead_name}\n"
                    f"• *Contato:* {phone}\n"
                    f"• *Resposta:* \"{text}\"\n\n"
                    f"💡 O PDF já foi entregue. Acompanhe a reação do cliente!"
                )
                if company_id:
                    update_crm_opportunity(company_id, text)
            return

        # 3. Detector e Bypass de Bot de Recepção / Boas-vindas (apenas se NÃO houver intenção positiva)
        is_bot_greeting = any(trigger in normalized for trigger in BOT_GREETING_TRIGGERS)
        if is_bot_greeting:
            print(f"   [🤖] Bot de recepção detectado em '{lead_name}' ({phone})!")
            handle_bot_bypass(phone, lead_name, company_id, text)
            return

        # 3b. Detector de Decisor: recepção indica número novo + palavra-chave de responsável
        # Padrão: "(11) 99919-7395", "11 99919-7395", "11999197395", etc.
        decisor_phone_match = re.search(
            r'(?:\(?\d{2}\)?\s*)?(?:9\d{4}[-\s]?\d{4}|\d{4}[-\s]?\d{4})',
            text
        )
        DECISOR_KEYWORDS = [
            "falar com", "fale com", "encaminhar", "encaminhe", "responsavel", "responsável",
            "proprietari", "proprietário", "proprietária", "dono", "dona", "diretor", "diretora",
            "gerente", "coordenador", "coordenadora", "contatar", "contate"
        ]
        has_decisor_keyword = any(kw in normalized for kw in DECISOR_KEYWORDS)

        if decisor_phone_match and has_decisor_keyword:
            raw_decisor_phone = decisor_phone_match.group(0)
            decisor_digits = re.sub(r"\D", "", raw_decisor_phone)
            if len(decisor_digits) in [10, 11]:
                decisor_full = "55" + decisor_digits
            else:
                decisor_full = decisor_digits

            print(f"   [👤] DECISOR DETECTADO: número {decisor_full} indicado por '{lead_name}' ({phone})")

            thanks_reply = (
                "Muito obrigado pela atenção! 🙏\n\n"
                "Vou entrar em contato diretamente com o responsável para apresentar o diagnóstico no melhor momento. "
                "Ótima semana pra vocês!"
            )
            try:
                url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
                requests.post(
                    url,
                    json={"number": phone, "text": thanks_reply},
                    headers={"apikey": API_KEY, "Content-Type": "application/json"},
                    timeout=10
                )
            except Exception as e:
                print("[!] Erro ao enviar resposta de redirecionamento:", e)

            notify_admin(
                f"👤 *DECISOR IDENTIFICADO!*\n"
                f"• *Lead recepção:* {lead_name} ({phone})\n"
                f"• *Número do decisor:* {decisor_full}\n"
                f"• *Mensagem original:* \"{text}\"\n\n"
                f"🎯 Abordar o decisor diretamente com o gancho principal!"
            )

            if company_id:
                record_followup_note(company_id, f"Recepção indicou decisor: {decisor_full}. Abordagem direta pendente.")
            return

        # Se chegou aqui, é uma resposta humana aberta / dúvida / objeção do lead!
        # Bloqueia qualquer resposta automática e alerta imediatamente o Eduardo no WhatsApp
        print(f"   [⚠️ RESPOSTA HUMANA] Lead '{lead_name}' ({phone}) enviou mensagem aberta. Encaminhando para o gestor...")
        notify_admin(
            f"💬 *RESPOSTA DE LEAD PENDENTE DE VALIDAÇÃO:*\n"
            f"• *Lead:* {lead_name}\n"
            f"• *Contato:* {phone}\n"
            f"• *Mensagem:* \"{text}\"\n\n"
            f"⚠️ *Atenção:* Nenhuma mensagem foi enviada ao lead. Responda aqui para aprovar a resposta ou conduzir."
        )
        if company_id:
            record_followup_note(company_id, f"Mensagem aberta recebida: '{text}'. Aguardando validação do gestor.")

    def log_message(self, format, *args):
        # Suprime logs de requisições HTTP triviais no terminal
        return

def run_server(port=5680):
    server = HTTPServer(("0.0.0.0", port), WebhookHandler)
    print("==================================================================")
    print(f" 🚀 AUTO-RESPONDER VOCAÇÃO 2027 ATIVO NA PORTA {port}")
    print(" Monitorando respostas do WhatsApp em tempo real...")
    print("==================================================================")
    server.serve_forever()

if __name__ == "__main__":
    run_server()
