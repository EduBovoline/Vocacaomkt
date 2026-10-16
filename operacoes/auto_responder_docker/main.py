import os
import sys
import re
import json
import time
import random
import threading
import urllib.parse
import base64
import unicodedata
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests

from gemini_classifier import analyze_and_generate_reply
from jev_engine import qualify_with_jev
from crm_db import (
    find_lead_in_db,
    record_lead_interaction,
    update_lead_opportunity,
    create_followup_task
)
from enviar_email import send_email

EVOLUTION_API_URL = os.environ.get("EVOLUTION_API_URL", "http://vocacao-evolution-api:8080")
INSTANCE_NAME = os.environ.get("INSTANCE_NAME", "vocacao_comercial")
API_KEY = os.environ.get("API_KEY", "vocacao_update_secret_key_2026")
ADMIN_WHATSAPP = os.environ.get("ADMIN_WHATSAPP", "5515981512083")
PORT = int(os.environ.get("PORT", 5680))
PERSONAL_EXCLUDED_NUMBERS = ["981512083", "981781911", "1807055946"]

DATA_DIR = os.environ.get("DATA_DIR", "/app/data")
LEADS_DIR = os.environ.get("LEADS_DIR", "/app/leads")

DELIVERED_FILE = os.path.join(DATA_DIR, "delivered_leads.json")
OPTOUT_FILE = os.path.join(DATA_DIR, "optout_leads.json")
BYPASS_FILE = os.path.join(DATA_DIR, "bypassed_leads.json")
HISTORY_FILE = os.path.join(DATA_DIR, "chat_history.json")

def load_chat_history(phone):
    data = load_json_file(HISTORY_FILE)
    return data.get(phone, [])

def append_chat_history(phone, role, text):
    data = load_json_file(HISTORY_FILE)
    if phone not in data:
        data[phone] = []
    data[phone].append({"role": role, "text": text, "at": datetime.now().isoformat()})
    save_json_file(HISTORY_FILE, data)

PENDING_APPROVALS = {}

POSITIVE_TRIGGERS = [
    "sim", "pode mandar", "pode enviar", "pode", "manda", "mandar", "quero",
    "claro", "envia", "enviar", "mostra", "mostrar", "com certeza", "mande",
    "manda ai", "manda aí", "fiquei curiosa", "curioso", "tenho interesse", "manda aqui"
]

BOT_GREETING_TRIGGERS = [
    "agradece seu contato", "agradecemos seu contato", "agradece o contato", "agradecemos o contato",
    "como podemos ajudar", "como posso ajudar", "em que podemos ajudar", "em que posso ajudar",
    "para agilizar nosso atendimento", "para agilizar seu atendimento",
    "qual seu nome", "qual o seu nome", "seu nome",
    "seja bem-vindo", "seja bem vindo", "seja bem-vinda", "seja bem vinda",
    "atendimento automatico", "mensagem automatica", "resposta automatica",
    "nosso horario de atendimento", "fora do horario", "horario de funcionamento"
]

LGPD_OPTOUT_TRIGGERS = [
    "parar", "descadastrar", "cancelar", "nao quero", "não quero", "remover",
    "pare", "bloquear", "nao tenho interesse", "não tenho interesse"
]

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
    "992529514": {"id": "p020-mundo-acqua", "name": "Mundo Acqua Studio"}
}

def load_json_file(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_json_file(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def is_pdf_already_delivered(phone):
    data = load_json_file(DELIVERED_FILE)
    clean_phone = re.sub(r"\D", "", phone)
    for p in data:
        clean_p = re.sub(r"\D", "", p)
        if clean_p[-8:] == clean_phone[-8:]:
            return True
    return False

def record_delivered(phone, lead_name):
    data = load_json_file(DELIVERED_FILE)
    data[phone] = {"lead_name": lead_name, "delivered_at": datetime.now().isoformat()}
    save_json_file(DELIVERED_FILE, data)

def record_optout(phone, lead_name):
    data = load_json_file(OPTOUT_FILE)
    data[phone] = {"lead_name": lead_name, "optout_at": datetime.now().isoformat()}
    save_json_file(OPTOUT_FILE, data)

def is_already_bypassed(phone):
    data = load_json_file(BYPASS_FILE)
    clean_phone = re.sub(r"\D", "", phone)
    for p in data:
        clean_p = re.sub(r"\D", "", p)
        if clean_p[-8:] == clean_phone[-8:]:
            return True
    return False

def record_bypassed(phone, lead_name):
    data = load_json_file(BYPASS_FILE)
    data[phone] = {"lead_name": lead_name, "bypassed_at": datetime.now().isoformat()}
    save_json_file(BYPASS_FILE, data)

def normalize_text(text):
    if not text:
        return ""
    nfkd = unicodedata.normalize('NFKD', text)
    return "".join([c for c in nfkd if not unicodedata.combining(c)]).lower().strip()

def notify_admin(message):
    """Envia notificação via WhatsApp para o gestor da agência."""
    if not message or not ADMIN_WHATSAPP:
        return
    try:
        url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
        payload = {"number": ADMIN_WHATSAPP, "text": str(message)}
        headers = {"apikey": API_KEY, "Content-Type": "application/json"}
        requests.post(url, json=payload, headers=headers, timeout=10)
    except Exception as e:
        print(f"[!] Erro ao notificar admin ({ADMIN_WHATSAPP}): {e}")

def send_whatsapp_text(number, text):
    if not text or not str(text).strip():
        print(f"[!] Tentativa de envio de texto vazio para {number} bloqueada com sucesso.")
        return
    clean_text = str(text).strip()
    # VERIFICAÇÃO ANTI-SLOP TOTAL
    if any(bad in clean_text.lower() for bad in ["undefined", "null", "[object object]"]):
        print(f"[!] [ANTI-SLOP] Bloqueado disparo com termos corrompidos para {number}: {clean_text}")
        notify_admin(f"⚠️ *ANTI-SLOP ATIVADO:* Tentativa de envio com termo inválido ('undefined'/'null') bloqueada para {number}.")
        return
    if len(clean_text) < 5:
        print(f"[!] [ANTI-SLOP] Bloqueado disparo com texto muito curto (<5 caracteres) para {number}.")
        return
    try:
        url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
        payload = {"number": number, "text": text}
        headers = {"apikey": API_KEY, "Content-Type": "application/json"}
        requests.post(url, json=payload, headers=headers, timeout=10)
    except Exception as e:
        print(f"[!] Erro ao enviar WhatsApp para {number}: {e}")

def is_mobile_phone(phone):
    """
    Valida se um telefone brasileiro é celular móvel (apto para WhatsApp).
    Retorna True se for celular de 9 dígitos (com ou sem DDD 15).
    Retorna False para telefones fixos (8 dígitos / sem 9º dígito).
    """
    clean = re.sub(r"\D", "", str(phone or ""))
    if clean.startswith("55") and len(clean) in [12, 13]:
        clean = clean[2:]
    if len(clean) == 11 and clean[2] == '9':
        return True
    if len(clean) == 9 and clean[0] == '9':
        return True
    return False

def is_lead_strictly_virgin(phone, name):
    """
    Verificação estrita de lead virgem.
    Garante que nenhum lead anteriormente abordado (seja manualmente em setembro,
    nos CSVs das marcenarias, no Twenty CRM ou na Evolution API) seja contatado novamente.
    """
    clean_digits = re.sub(r"\D", "", str(phone))
    if not clean_digits or len(clean_digits) < 8:
        return False, "Telefone inválido"
    last8 = clean_digits[-8:]

    # 1. Checa histórico absoluto consolidado (CSVs, disparos manuais, pastas 2 Leads)
    hist_file = os.path.join(DATA_DIR, "historico_absoluto_contatados.json")
    if os.path.exists(hist_file):
        hist = load_json_file(hist_file)
        phones_hist = hist.get("phones_last8", {})
        if last8 in phones_hist:
            info = phones_hist[last8]
            return False, f"Contato prévio registrado em {info.get('file', 'histórico')}: {info.get('name', '')} ({info.get('status', '')})"
        
        names_hist = hist.get("names", {})
        clean_name = str(name).lower().strip()
        if clean_name in names_hist:
            info = names_hist[clean_name]
            return False, f"Empresa com histórico anterior em {info.get('file', 'histórico')}: {name} ({info.get('status', '')})"

    # 2. Twenty CRM & Direct Map
    if last8 in {p[-8:] for p in DIRECT_MAP.keys()}:
        return False, "Empresa já cadastrada no Twenty CRM"

    # 3. Disparos anteriores na sessão / Delivered / Optout / Bypassed
    progresso = load_json_file(os.path.join(DATA_DIR, "fila_ouro_progresso.json"))
    delivered = load_json_file(DELIVERED_FILE)
    optout = load_json_file(OPTOUT_FILE)
    bypassed = load_json_file(os.path.join(DATA_DIR, "bypassed_leads.json"))
    
    for coll in [progresso.get("sent", []), list(delivered.keys()), list(optout.keys()), list(bypassed.keys())]:
        for item in coll:
            cd = re.sub(r"\D", "", str(item))
            if len(cd) >= 8 and cd[-8:] == last8:
                return False, "Já contatado nesta instância"

    # 4. Evolution API histórico de mensagens (últimos dias)
    try:
        chk_url = f"{EVOLUTION_API_URL}/chat/findMessages/{INSTANCE_NAME}"
        chk_payload = {"where": {"key": {"remoteJid": f"{clean_digits}@s.whatsapp.net"}}}
        chk_resp = requests.post(chk_url, json=chk_payload, headers={"apikey": API_KEY, "Content-Type": "application/json"}, timeout=4)
        recs = chk_resp.json().get("messages", {}).get("records", [])
        if recs and len(recs) > 0:
            return False, f"Possui {len(recs)} mensagem(ns) no WhatsApp da Evolution API"
    except Exception:
        pass

    return True, "Virgem"

def find_lead_info(phone):
    clean_digits = re.sub(r"\D", "", phone)
    last8 = clean_digits[-8:] if len(clean_digits) >= 8 else clean_digits
    lead_data = None

    # 1. Catálogo Permanente Global (224 empresas mapeadas com nomes e endereços reais)
    cat_path = os.path.join(DATA_DIR, "leads_catalog_global.json")
    if os.path.exists(cat_path):
        catalog = load_json_file(cat_path)
        if isinstance(catalog, dict) and last8 in catalog:
            item = catalog[last8]
            lead_data = {
                "id": None,
                "name": item.get("name", f"Contato {last8[-4:]}"),
                "cat": item.get("cat", "Comércio / Serviços"),
                "bairro": item.get("bairro", "Sorocaba"),
                "addr": item.get("addr", ""),
                "presence": item.get("presence", ""),
                "oferta_nome": item.get("oferta_nome", "Vocação Start"),
                "oferta_preco": item.get("oferta_preco", 850.0),
                "person_id": None,
                "opportunity_id": None
            }
            return lead_data

    # 2. Base enriquecida dos 100 leads (Santa Rosália & Jardim Brasilândia)
    leads_100_path = os.path.join(DATA_DIR, "leads_100_santa_rosalia_brasilandia.json")
    if os.path.exists(leads_100_path):
        leads_100 = load_json_file(leads_100_path)
        for l in leads_100:
            l_clean = re.sub(r"\D", "", l.get("phone", ""))
            if l_clean and (clean_digits[-8:] == l_clean[-8:] or l_clean in clean_digits or clean_digits in l_clean):
                lead_data = {
                    "id": None,
                    "name": l["name"],
                    "cat": l.get("cat", "Comércio / Serviços"),
                    "bairro": l.get("bairro", "Sorocaba"),
                    "addr": l.get("addr", ""),
                    "presence": l.get("presence", ""),
                    "oferta_nome": l.get("oferta_nome", "Vocação Start"),
                    "oferta_preco": l.get("oferta_preco", 850.0),
                    "person_id": None,
                    "opportunity_id": None
                }
                return lead_data

    # 2. Leads ativos prioritários (Gui, Dra. Deniane, etc.)
    if "11976035867" in clean_digits:
        lead_data = {
            "name": "Gui (Indicação - Mapeamento)",
            "cat": "Indicação / Mapeamento de Negócio",
            "bairro": "Sorocaba e Região",
            "addr": "Indicação",
            "presence": "Lead por indicação em fase de descoberta e relacionamento",
            "oferta_nome": "Mapeamento Estratégico",
            "oferta_preco": 0.0,
            "id": None, "person_id": None, "opportunity_id": None,
            "is_indicacao": True
        }
    elif "15996841434" in clean_digits:
        lead_data = {
            "name": "Dra. Deniane Almeida Fisiovet",
            "cat": "Reabilitação Veterinária & Fisioterapia",
            "bairro": "Santa Rosália",
            "addr": "Av. Pereira da Silva, 68",
            "presence": "Nicho de altíssimo valor sem vitrine dedicada",
            "oferta_nome": "Combo Maps + Tour 360° GoPro Max",
            "oferta_preco": 950.0,
            "id": None, "person_id": None, "opportunity_id": None
        }
    elif "15991767971" in clean_digits:
        lead_data = {
            "name": "Clínica Paes Pilates & Fisio",
            "cat": "Pilates & Fisioterapia Especializada",
            "bairro": "Santa Rosália",
            "addr": "Av. Pereira da Silva, 164",
            "presence": "Aparelhos modernos sem fotos 360 no Maps",
            "oferta_nome": "Combo Maps + Tour 360° GoPro Max",
            "oferta_preco": 950.0,
            "id": None, "person_id": None, "opportunity_id": None
        }

    # 3. Integração com Twenty CRM (agrega IDs de company, person e opportunity)
    db_lead = find_lead_in_db(clean_digits)
    if db_lead:
        if not lead_data:
            lead_data = {
                "id": db_lead.get("company_id") or db_lead.get("id"),
                "name": db_lead.get("company_name") or db_lead.get("name"),
                "cat": "Comércio / Serviços",
                "bairro": "Sorocaba",
                "addr": "",
                "presence": "Lead sincronizado no Twenty CRM",
                "oferta_nome": "Vocação Start",
                "oferta_preco": 850.0,
                "person_id": db_lead.get("person_id"),
                "opportunity_id": db_lead.get("opportunity_id")
            }
        else:
            lead_data["id"] = db_lead.get("company_id") or db_lead.get("id")
            lead_data["person_id"] = db_lead.get("person_id")
            lead_data["opportunity_id"] = db_lead.get("opportunity_id")

    # 4. Fallback no mapa legado direto
    if not lead_data:
        for digits, lead_info in DIRECT_MAP.items():
            if digits in clean_digits:
                lead_data = {
                    "id": lead_info["id"],
                    "name": lead_info["name"],
                    "cat": "Saúde & Estética",
                    "bairro": "Campolim",
                    "addr": "Sorocaba/SP",
                    "presence": "Presença digital em qualificação",
                    "oferta_nome": "Vocação Start",
                    "oferta_preco": 850.0,
                    "person_id": None,
                    "opportunity_id": None
                }
                break

    return lead_data

def find_pdf_for_lead(lead_name):
    if not os.path.exists(LEADS_DIR):
        return None
    clean_lead = normalize_text(lead_name)
    best_folder = None
    best_score = 0
    lead_words = set(w for w in clean_lead.split() if len(w) > 2)

    for folder in os.listdir(LEADS_DIR):
        folder_path = os.path.join(LEADS_DIR, folder)
        if os.path.isdir(folder_path):
            clean_folder = normalize_text(folder)
            if clean_lead == clean_folder:
                score = 100
            elif clean_lead in clean_folder or clean_folder in clean_lead:
                score = 80
            else:
                folder_words = set(w for w in clean_folder.split() if len(w) > 2)
                score = len(lead_words.intersection(folder_words)) * 10
            if score > best_score:
                best_score = score
                best_folder = folder_path

    if best_folder and best_score >= 20:
        for f in os.listdir(best_folder):
            if f.startswith("Analise-Presenca-Digital") and f.endswith(".pdf"):
                return os.path.join(best_folder, f)
            if f.endswith("-cliente.pdf") or ("prospeccao" in f.lower() and f.endswith(".pdf")):
                return os.path.join(best_folder, f)
            if f.lower().endswith(".pdf"):
                return os.path.join(best_folder, f)
    return None

def send_pdf_lead(number, pdf_path, lead_name):
    if not pdf_path or not os.path.exists(pdf_path):
        print(f"[!] [ANTI-SLOP] PDF não localizado no disco para {lead_name} ({number}).")
        notify_admin(f"⚠️ *ANTI-SLOP:* Disparo bloqueado — PDF não localizado para {lead_name} ({number}).")
        return False
    size = os.path.getsize(pdf_path)
    if size < 50000:
        print(f"[!] [ANTI-SLOP] PDF corrompido ou vazio ({size} bytes) para {lead_name} ({number}).")
        notify_admin(f"⚠️ *ANTI-SLOP:* Disparo bloqueado — PDF muito pequeno/corrompido ({size} bytes) para {lead_name}.")
        return False

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
    headers = {"apikey": API_KEY, "Content-Type": "application/json"}
    payload = {
        "number": number,
        "mediatype": "document",
        "mimetype": "application/pdf",
        "caption": caption,
        "media": pdf_b64,
        "fileName": f"Analise-Presenca-Digital-{lead_name.replace(' ', '-')}.pdf"
    }

    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=25)
        if resp.status_code in [200, 201]:
            record_delivered(number, lead_name)
            return True
    except Exception as e:
        print(f"[!] Erro ao enviar PDF: {e}")
    return False

def handle_admin_command(text):
    norm = normalize_text(text)
    print(f"\n   [★] COMANDO DO GESTOR NO WHATSAPP: {text}")

    # Comando '1' -> Aprova a última resposta sugerida pela IA
    if text.strip() == "1":
        if "last_pending" in PENDING_APPROVALS:
            pending = PENDING_APPROVALS["last_pending"]
            target_phone = pending["phone"]
            target_name = pending["name"]
            suggested_text = (pending.get("reply") or "").strip()

            if not suggested_text or len(suggested_text) < 5:
                notify_admin("⚠️ *Aviso de Proteção:* A resposta sugerida estava em branco e foi cancelada. Nenhuma mensagem vazia foi enviada ao lead.")
                del PENDING_APPROVALS["last_pending"]
                return

            send_whatsapp_text(target_phone, suggested_text)
            append_chat_history(target_phone, "Vocação (Eduardo)", suggested_text)
            
            # Registra no CRM que a resposta manual/aprovada foi enviada
            c_id = pending.get("company_id")
            p_id = pending.get("person_id")
            o_id = pending.get("opportunity_id")
            if c_id:
                record_lead_interaction(
                    c_id, p_id, o_id,
                    "WhatsApp: Resposta do Gestor Aprovada via Celular",
                    f"**Mensagem enviada por Eduardo via aprovação '1':**\n> {suggested_text}"
                )

            del PENDING_APPROVALS["last_pending"]
            notify_admin(
                f"✅ *RESPOSTA APROVADA E DISPARADA!*\n"
                f"• *Lead:* {target_name} ({target_phone})\n"
                f"• *Texto enviado:*\n\"{suggested_text}\"\n"
                f"• *Twenty CRM:* Nota registrada no histórico."
            )
            return
        else:
            notify_admin("⚠️ *Nenhuma resposta pendente aguardando aprovação '1' no momento.*")
            return

    # Comando 'status'
    if any(w in norm for w in ["status", "resumo", "operacao", "painel"]):
        delivered = load_json_file(DELIVERED_FILE)
        optout = load_json_file(OPTOUT_FILE)
        fila_ouro = load_json_file("data/fila_ouro_progresso.json")
        ouro_sent = len(fila_ouro.get("sent", []))
        ouro_failed = len(fila_ouro.get("failed", []))
        ouro_pend = 30 - (ouro_sent + ouro_failed)
        gemini_status = "🟢 ATIVO" if os.environ.get("GEMINI_API_KEY") else "⚪ MODO REGRAS"
        msg = (
            f"📊 *PAINEL OPERACIONAL VOCAÇÃO (DOCKER + JEV):*\n\n"
            f"• *Fila 30 Leads Ouro:* {ouro_sent} disparados com sucesso | {ouro_failed} sem WhatsApp | {max(0, ouro_pend)} aguardando\n"
            f"• *Cadência Segura:* 1 disparo a cada ~4-5 minutos (anti-bloqueio Meta)\n"
            f"• *Diagnósticos PDF entregues:* {len(delivered)}\n"
            f"• *Descadastramentos (Opt-out):* {len(optout)}\n"
            f"• *Motor Jev (TypeSafe):* 🟢 CALIBRADO (Start, Update, Tour 360°)\n"
            f"• *Motor Gemini AI:* {gemini_status}\n"
            f"• *Twenty CRM:* 🟢 CONECTADO (http://192.168.15.2:3000)\n\n"
            f"Qualquer resposta de lead é qualificada pelo Jev e enviada para você aprovar digitando '1'!"
        )
        notify_admin(msg)
        return

    # Default
    reply = (
        f"🫡 *Instrução recebida, Eduardo!*\n\n"
        f"Mensagem: \"{text}\"\n\n"
        f"O motor Docker + Jev está 100% monitorado. Nenhuma ação comercial será tomada sem o seu comando."
    )
    notify_admin(reply)

QUEUE_PAUSED = True
AUTO_RESPONDER_ENABLED = False
NEXT_DISPATCH_SECONDS_LEFT = 0
LOGS_FILE = os.path.join(DATA_DIR, "dispatch_logs.json")
DISPATCH_LOGS = load_json_file(LOGS_FILE) if os.path.exists(LOGS_FILE) else []
if not isinstance(DISPATCH_LOGS, list):
    DISPATCH_LOGS = []
def remove_leads_from_bank(lead_identifiers):
    """
    Exclusão automática: remove leads dos bancos (Santa Rosália e Alto Ticket)
    quando são adicionados à live/fila ou ativados no CRM.
    """
    if not lead_identifiers:
        return
    ids_to_remove = set()
    phones_to_remove = set()
    for item in lead_identifiers:
        if isinstance(item, dict):
            if item.get("id"):
                ids_to_remove.add(str(item.get("id")))
            p = re.sub(r"\D", "", str(item.get("phone", "")))
            if len(p) >= 8:
                phones_to_remove.add(p[-8:])
        elif isinstance(item, str):
            ids_to_remove.add(item)
            p = re.sub(r"\D", "", item)
            if len(p) >= 8:
                phones_to_remove.add(p[-8:])

    # 1. Limpa Santa Rosália
    sr_path = os.path.join(DATA_DIR, "leads_100_santa_rosalia_brasilandia.json")
    if os.path.exists(sr_path):
        sr_data = load_json_file(sr_path)
        if isinstance(sr_data, list):
            orig_len = len(sr_data)
            sr_data = [
                l for l in sr_data
                if str(l.get("id", "")) not in ids_to_remove and
                re.sub(r"\D", "", str(l.get("phone", "")))[-8:] not in phones_to_remove
            ]
            if len(sr_data) != orig_len:
                save_json_file(sr_path, sr_data)
                print(f"[+] [AUTO-EXCLUSÃO] {orig_len - len(sr_data)} lead(s) removidos do banco Santa Rosália para Live.")

    # 2. Limpa Alto Ticket
    ht_path = os.path.join(DATA_DIR, "leads_alto_ticket_verificados.json")
    if os.path.exists(ht_path):
        ht_data = load_json_file(ht_path)
        if isinstance(ht_data, list):
            orig_len = len(ht_data)
            ht_data = [
                l for l in ht_data
                if str(l.get("id", "")) not in ids_to_remove and
                re.sub(r"\D", "", str(l.get("phone", "")))[-8:] not in phones_to_remove
            ]
            if len(ht_data) != orig_len:
                save_json_file(ht_path, ht_data)
                print(f"[+] [AUTO-EXCLUSÃO] {orig_len - len(ht_data)} lead(s) removidos do banco Alto Ticket para Live.")

class WebhookHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path).path
        if parsed in ["/painel", "/painel.html", "/Painel-PreSelecao-100Leads-SantaRosalia-Brasilandia.html"]:
            painel_file = os.path.join(os.path.dirname(__file__), "templates", "painel.html")
            if os.path.exists(painel_file):
                with open(painel_file, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return

        if parsed == "/api/subcrm-data":
            progresso = load_json_file(os.path.join(DATA_DIR, "fila_ouro_progresso.json"))
            leads_ouro = load_json_file(os.path.join(DATA_DIR, "leads_ouro_fila_disparo.json"))
            chats = load_json_file(os.path.join(DATA_DIR, "chat_history.json"))
            delivered = load_json_file(DELIVERED_FILE)
            optout = load_json_file(OPTOUT_FILE)

            chat_list = []
            for p, msgs in chats.items():
                if any(ex in p for ex in PERSONAL_EXCLUDED_NUMBERS):
                    continue
                lead_info = find_lead_info(p) or {}
                lead_name = lead_info.get("name") or f"Contato {p[-4:]}"
                lead_cat = lead_info.get("cat") or "Comércio Local"
                lead_bairro = lead_info.get("bairro") or "Sorocaba"
                lead_addr = lead_info.get("addr") or ""
                lead_presence = lead_info.get("presence") or ""
                lead_oferta = lead_info.get("oferta_nome") or "Vocação Start"
                lead_preco = lead_info.get("oferta_preco") or 850.0

                maps_q = urllib.parse.quote(f"{lead_name} {lead_addr} Sorocaba".strip())
                google_q = urllib.parse.quote(f"{lead_name} Sorocaba".strip())
                insta_q = urllib.parse.quote(f"site:instagram.com {lead_name} Sorocaba".strip())

                last_role = msgs[-1]["role"] if msgs else ""
                last_msg = msgs[-1]["text"] if msgs else ""
                last_msg_lower = last_msg.lower()

                is_optout = p in optout or any(w in last_msg_lower for w in ["parar", "descadastrar", "cancelar", "não tenho interesse", "nao tenho interesse"])
                if is_optout:
                    status = "optout"
                    status_label = "🛑 Opt-out / Parar"
                    needs_followup = False
                elif "Lead" in last_role:
                    status = "replied"
                    status_label = "🔥 Respondeu"
                    needs_followup = True
                elif len(msgs) > 1:
                    status = "in_dialog"
                    status_label = "💬 Em Conversa"
                    needs_followup = False
                else:
                    status = "waiting"
                    status_label = "⏳ Aguardando"
                    needs_followup = False

                chat_list.append({
                    "phone": p,
                    "name": lead_name,
                    "cat": lead_cat,
                    "bairro": lead_bairro,
                    "addr": lead_addr,
                    "presence": lead_presence,
                    "oferta_nome": lead_oferta,
                    "oferta_preco": lead_preco,
                    "maps_url": f"https://www.google.com/maps/search/?api=1&query={maps_q}",
                    "whatsapp_url": f"https://wa.me/{p}",
                    "instagram_url": f"https://www.google.com/search?q={insta_q}",
                    "search_url": f"https://www.google.com/search?q={google_q}",
                    "last_msg": last_msg,
                    "last_role": last_role,
                    "last_at": msgs[-1].get("at", "") if msgs else "",
                    "total_msgs": len(msgs),
                    "status": status,
                    "status_label": status_label,
                    "needs_followup": needs_followup,
                    "messages": msgs[-12:]
                })
            # Prioriza: primeiro quem respondeu (needs_followup), depois mais recentes
            chat_list.sort(key=lambda x: (x["needs_followup"], x["last_at"]), reverse=True)

            high_ticket = load_json_file(os.path.join(DATA_DIR, "leads_alto_ticket_verificados.json"))
            santa_rosalia = load_json_file(os.path.join(DATA_DIR, "leads_100_santa_rosalia_brasilandia.json"))
            ht_list = high_ticket if isinstance(high_ticket, list) else []
            sr_list = santa_rosalia if isinstance(santa_rosalia, list) else []
            all_leads_total = len(ht_list) + len(sr_list)

            sent_set = set(progresso.get("sent", []))
            failed_set = set(progresso.get("failed", []))
            optout_set = set(optout.keys())
            pending_queue = [
                l for l in (leads_ouro if isinstance(leads_ouro, list) else [])
                if l.get("phone") not in sent_set
                and l.get("phone") not in failed_set
                and l.get("phone") not in optout_set
            ]

            res_data = {
                "auto_responder_enabled": AUTO_RESPONDER_ENABLED,
                "high_ticket_leads": ht_list,
                "santa_rosalia_leads": sr_list,
                "queue": {
                    "is_paused": QUEUE_PAUSED,
                    "countdown_seconds": NEXT_DISPATCH_SECONDS_LEFT,
                    "total": len(pending_queue),
                    "sent": progresso.get("sent", []),
                    "failed": progresso.get("failed", []),
                    "leads": pending_queue,
                    "logs": DISPATCH_LOGS[-15:]
                },
                "chats": chat_list,
                "pending": PENDING_APPROVALS.get("last_pending"),
                "stats": {
                    "sent_count": len(progresso.get("sent", [])),
                    "failed_count": len(progresso.get("failed", [])),
                    "delivered_count": len(delivered),
                    "optout_count": len(optout),
                    "total_leads": all_leads_total if all_leads_total > 0 else 171,
                    "pipeline_val": 4850000
                }
            }
            body = json.dumps(res_data, ensure_ascii=False).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"status":"online","service":"vocacao-auto-responder-docker-jev"}')

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path).path
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len).decode('utf-8') if content_len > 0 else ""

        if parsed == "/api/trigger-next":
            FORCE_DISPATCH_EVENT.set()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "message": "Disparo forçado acionado"}).encode())
            return

        if parsed == "/api/approve":
            success = False
            msg = "Nenhuma mensagem pendente"
            if "last_pending" in PENDING_APPROVALS:
                pending = PENDING_APPROVALS["last_pending"]
                target_phone = pending["phone"]
                suggested_text = (pending.get("reply") or "").strip()
                if suggested_text and len(suggested_text) >= 5:
                    send_whatsapp_text(target_phone, suggested_text)
                    append_chat_history(target_phone, "Vocação (Eduardo)", suggested_text)
                    del PENDING_APPROVALS["last_pending"]
                    success = True
                    msg = "Resposta aprovada e disparada com sucesso!"
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": success, "message": msg}).encode())
            return

        if parsed == "/api/send-message":
            try:
                payload = json.loads(body)
                phone = payload.get("phone")
                text_to_send = payload.get("text", "").strip()
                if phone and text_to_send:
                    send_whatsapp_text(phone, text_to_send)
                    append_chat_history(phone, "Vocação (Eduardo)", text_to_send)
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": True}).encode())
                    return
            except Exception:
                pass
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": False, "error": "Invalid params"}).encode())
            return

        if parsed == "/api/leads/delete":
            try:
                req = json.loads(body) if body else {}
                lead_id = req.get("id")
                lead_phone = req.get("phone", "")
                lead_name = req.get("name", "")

                # 1. Remove de leads_100_santa_rosalia_brasilandia.json
                sr_path = os.path.join(DATA_DIR, "leads_100_santa_rosalia_brasilandia.json")
                if os.path.exists(sr_path):
                    sr_data = load_json_file(sr_path)
                    if isinstance(sr_data, list):
                        sr_data = [l for l in sr_data if l.get("id") != lead_id and l.get("phone") != lead_phone]
                        save_json_file(sr_path, sr_data)

                # 2. Remove de leads_alto_ticket_verificados.json
                ht_path = os.path.join(DATA_DIR, "leads_alto_ticket_verificados.json")
                if os.path.exists(ht_path):
                    ht_data = load_json_file(ht_path)
                    if isinstance(ht_data, list):
                        ht_data = [l for l in ht_data if l.get("id") != lead_id and l.get("phone") != lead_phone]
                        save_json_file(ht_path, ht_data)

                # 3. Remove da fila se estiver
                fila_path = os.path.join(DATA_DIR, "leads_ouro_fila_disparo.json")
                if os.path.exists(fila_path):
                    f_data = load_json_file(fila_path)
                    if isinstance(f_data, list):
                        f_data = [l for l in f_data if l.get("id") != lead_id and l.get("phone") != lead_phone]
                        save_json_file(fila_path, f_data)

                # 4. Registra na blacklist para nunca reaparecer
                hist_file = os.path.join(DATA_DIR, "historico_absoluto_contatados.json")
                if os.path.exists(hist_file):
                    hist = load_json_file(hist_file)
                    clean_p = re.sub(r"\D", "", str(lead_phone))
                    if len(clean_p) >= 8:
                        hist.setdefault("phones_last8", {})[clean_p[-8:]] = {
                            "name": lead_name,
                            "status": "Excluído pelo usuário",
                            "file": "Painel",
                            "phone": lead_phone
                        }
                    if lead_name:
                        hist.setdefault("names", {})[lead_name.lower().strip()] = {
                            "name": lead_name,
                            "status": "Excluído pelo usuário",
                            "file": "Painel",
                            "phone": lead_phone
                        }
                    save_json_file(hist_file, hist)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "message": "Lead excluído com sucesso!"}).encode())
                return
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode())
                return

        if parsed == "/api/toggle-auto-responder":
            global AUTO_RESPONDER_ENABLED
            AUTO_RESPONDER_ENABLED = not AUTO_RESPONDER_ENABLED
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "auto_responder_enabled": AUTO_RESPONDER_ENABLED}).encode())
            return

        if parsed == "/api/add-to-queue":
            try:
                payload = json.loads(body)
                p_phone = payload.get("phone", "")
                p_name = payload.get("name", "")

                if not is_mobile_phone(p_phone):
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": False, "error": f"Telefone Fixo ({p_phone}). O WhatsApp requer celular de 9 dígitos."}).encode())
                    return

                is_v, block_reason = is_lead_strictly_virgin(p_phone, p_name)
                if not is_v:
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": False, "error": f"Lead Bloqueado: {block_reason}"}).encode())
                    return

                fila_path = os.path.join(DATA_DIR, "leads_ouro_fila_disparo.json")
                cur_fila = load_json_file(fila_path) if os.path.exists(fila_path) else []
                if not isinstance(cur_fila, list): cur_fila = []
                cur_fila.append(payload)
                save_json_file(fila_path, cur_fila)
                remove_leads_from_bank([payload])
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "total": len(cur_fila)}).encode())
                return
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode())
                return

        if parsed == "/api/toggle-queue":
            global QUEUE_PAUSED
            QUEUE_PAUSED = not QUEUE_PAUSED
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "is_paused": QUEUE_PAUSED}).encode())
            return

        if parsed == "/api/clear-queue":
            fila_path = os.path.join(DATA_DIR, "leads_ouro_fila_disparo.json")
            save_json_file(fila_path, [])
            global NEXT_DISPATCH_SECONDS_LEFT
            NEXT_DISPATCH_SECONDS_LEFT = 0
            if "last_pending" in PENDING_APPROVALS:
                del PENDING_APPROVALS["last_pending"]
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "message": "Fila de disparos limpa com sucesso. 0 leads pendentes."}).encode())
            return

        if parsed == "/api/leads/requisicao-primaria":
            try:
                req = json.loads(body) if body else {}
                nicho = req.get("nicho", "all")
                bairro = req.get("bairro", "all")
                limit = int(req.get("limit", 50))

                # Agrega bases disponíveis
                candidates = []
                ht_path = os.path.join(DATA_DIR, "leads_alto_ticket_verificados.json")
                sr_path = os.path.join(DATA_DIR, "leads_100_santa_rosalia_brasilandia.json")
                if os.path.exists(ht_path):
                    ht_data = load_json_file(ht_path)
                    if isinstance(ht_data, list): candidates.extend(ht_data)
                if os.path.exists(sr_path):
                    sr_data = load_json_file(sr_path)
                    if isinstance(sr_data, list): candidates.extend(sr_data)

                # Deduplicação Rigorosa: Twenty CRM
                crm_phones = set()
                for p in DIRECT_MAP.keys():
                    crm_phones.add(p[-8:])

                # Deduplicação Rigorosa: Cooldown 45 dias Meta/Evolution
                progresso = load_json_file(os.path.join(DATA_DIR, "fila_ouro_progresso.json"))
                delivered = load_json_file(DELIVERED_FILE)
                optout = load_json_file(OPTOUT_FILE)

                cooldown_phones = set()
                for p in progresso.get("sent", []) + list(delivered.keys()) + list(optout.keys()):
                    cp = re.sub(r"\D", "", str(p))
                    if cp: cooldown_phones.add(cp[-8:])

                # Deduplicação Rigorosa: Fila atual
                cur_fila = load_json_file(os.path.join(DATA_DIR, "leads_ouro_fila_disparo.json"))
                if isinstance(cur_fila, list):
                    for f in cur_fila:
                        cp = re.sub(r"\D", "", str(f.get("phone", "")))
                        if cp: cooldown_phones.add(cp[-8:])

                only_mobile = req.get("only_mobile", True)

                virgin_leads = []
                for c in candidates:
                    c_phone = re.sub(r"\D", "", str(c.get("phone", "")))
                    c_name = c.get("name", "")
                    
                    is_v, block_reason = is_lead_strictly_virgin(c_phone, c_name)
                    if not is_v:
                        continue

                    # Filtro de celular/fixo
                    c["is_mobile"] = is_mobile_phone(c_phone)
                    if only_mobile and not c["is_mobile"]:
                        continue

                    # Filtros de nicho / bairro se especificados
                    c_bairro = (c.get("bairro") or "").lower()
                    c_seg = (c.get("segment") or c.get("category") or "").lower()
                    clean_c_name = c_name.lower()

                    if nicho != "all" and nicho.lower() not in c_seg and nicho.lower() not in clean_c_name:
                        continue
                    if bairro != "all" and bairro.lower() not in c_bairro:
                        continue

                    virgin_leads.append(c)
                    if len(virgin_leads) >= limit:
                        break

                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "success": True,
                    "nicho": nicho,
                    "bairro": bairro,
                    "total": len(virgin_leads),
                    "leads": virgin_leads
                }, ensure_ascii=False).encode('utf-8'))
                return
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode())
                return

        if parsed == "/api/leads/adicionar-lote-fila":
            try:
                req = json.loads(body) if body else {}
                new_leads = req.get("leads", [])
                fila_path = os.path.join(DATA_DIR, "leads_ouro_fila_disparo.json")
                cur_fila = load_json_file(fila_path) if os.path.exists(fila_path) else []
                if not isinstance(cur_fila, list): cur_fila = []

                existing_phones = {re.sub(r"\D", "", str(x.get("phone", "")))[-8:] for x in cur_fila}
                added_count = 0
                for l in new_leads:
                    lp = re.sub(r"\D", "", str(l.get("phone", "")))
                    l_name = l.get("name", "")
                    is_v, reason = is_lead_strictly_virgin(lp, l_name)
                    if not is_v:
                        print(f"[-] Rejeitado ao tentar adicionar lote: {l_name} ({reason})")
                        continue

                    if not is_mobile_phone(lp):
                        print(f"[-] Rejeitado lote (telefone fixo sem WhatsApp): {l_name} ({lp})")
                        continue

                    if lp and lp[-8:] not in existing_phones:
                        cur_fila.append({
                            "id": l.get("id"),
                            "name": l.get("name"),
                            "phone": l.get("phone"),
                            "bairro": l.get("bairro"),
                            "oferta_nome": l.get("jev_oferta") or l.get("oferta_nome", "Vocação Start"),
                            "hook_whatsapp": l.get("hook_a") or l.get("hook_whatsapp", "Olá! Analisei a presença digital de vocês no Google...")
                        })
                        existing_phones.add(lp[-8:])
                        added_count += 1

                save_json_file(fila_path, cur_fila)
                remove_leads_from_bank(new_leads)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "added": added_count, "total_fila": len(cur_fila)}).encode())
                return
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode())
                return

        # Webhook da Evolution API
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"status":"received"}')

        try:
            data = json.loads(body)
            self.process_payload(data)
        except Exception as e:
            print("[!] Erro ao processar payload:", e)

    def process_payload(self, data):
        msg_data = data.get("data", {})
        key = msg_data.get("key", {})
        remote_jid = key.get("remoteJid", "")
        if not remote_jid or "@g.us" in remote_jid or "status@broadcast" in remote_jid:
            return

        remote_alt = key.get("remoteJidAlt", "")
        phone = remote_alt.split("@")[0] if "@s.whatsapp.net" in remote_alt else remote_jid.split("@")[0]
        clean_phone = re.sub(r"\D", "", phone)

        message_obj = msg_data.get("message", {})
        text = (
            message_obj.get("conversation") or 
            message_obj.get("extendedTextMessage", {}).get("text") or 
            ""
        ).strip()

        if not text:
            return

        # 1. Ignora Meta Bot e números de sistemas/corporativos (>14 dígitos)
        if "1807055946" in clean_phone or len(clean_phone) > 14:
            return

        # 2. Ignora mensagens enviadas por mim mesmo
        if key.get("fromMe", False):
            return

        # 3. Se for o Gestor Eduardo no WhatsApp
        if "981512083" in clean_phone:
            handle_admin_command(text)
            return

        # 4. Ignora contatos pessoais/familiares (esposa, família)
        if any(ex in clean_phone for ex in PERSONAL_EXCLUDED_NUMBERS):
            return

        # 5. MODO WHITELIST RIGOROSO: Só processa se for lead cadastrado na base ou CRM
        lead = find_lead_info(clean_phone)
        if not lead:
            # Número desconhecido/fora da esteira comercial: silêncio absoluto
            return

        # 6. TRATAMENTO DE INDICAÇÕES: Mapeamento de negócio manual (nenhum robô responde)
        if lead.get("is_indicacao"):
            append_chat_history(clean_phone, f"Indicação ({lead['name']})", text)
            notify_admin(
                f"🤝 *MENSAGEM DE INDICAÇÃO (MAPEAMENTO):*\n"
                f"• *Contato:* {lead['name']} ({clean_phone})\n"
                f"• *Mensagem:* \"{text}\"\n"
                f"• *Ação:* Entrado na esteira de Mapeamento Manual de Negócio. Nenhum robô responderá."
            )
            return

        push_name = msg_data.get('pushName', 'Desconhecido')
        print(f"\n📩 [LEAD WHATSAPP] {clean_phone} ({push_name}): \"{text}\"")

        append_chat_history(clean_phone, f"Lead ({push_name})", text)
        history = load_chat_history(clean_phone)

        lead_name = lead["name"] if lead else push_name
        company_id = lead["id"] if lead else None
        person_id = lead.get("person_id") if lead else None
        opportunity_id = lead.get("opportunity_id") if lead else None

        # SE AUTO-RESPONDER DESATIVADO: Apenas qualifica e prepara sugestões A/B sem disparar
        if not AUTO_RESPONDER_ENABLED:
            print(f"🔒 [MODO MANUAL SEGURO] Lead {lead_name} ({clean_phone}) respondeu: '{text}'. Sugestões A/B salvas no painel.")
            sug_a = f"Opa, tudo bem? Aqui é o Eduardo, da Vocação aqui do Santa Rosália.\nA gente é especialista em modernização visual de sites e páginas no celular em 5 dias aqui na nossa região. Com quem eu costumo falar sobre a presença e o site de vocês por aí?"
            sug_b = f"Oi, tudo bem? Eduardo, da Vocação aqui do Santa Rosália.\nPreparei um comparativo visual bem rápido de 1 minuto mostrando como a apresentação de vocês no smartphone pode transmitir mais autoridade para quem pesquisa no bairro. Posso te mandar por aqui?"
            PENDING_APPROVALS["last_pending"] = {
                "phone": clean_phone,
                "name": lead_name,
                "reply": sug_a,
                "reply_b": sug_b,
                "company_id": company_id,
                "person_id": person_id,
                "opportunity_id": opportunity_id
            }
            notify_admin(
                f"📩 *NOVA RESPOSTA DE LEAD (Modo Manual):*\n"
                f"• *Lead:* {lead_name} ({clean_phone})\n"
                f"• *Mensagem:* \"{text}\"\n"
                f"• *Painel:* Sugestões A e B disponíveis em http://localhost:5680/painel"
            )
            return

        # 2. Qualificação Semântica com Jev (TypeSafe System One)
        jev_info = qualify_with_jev(lead_name, text)
        print(f"   [🧠 JEV] Oferta: {jev_info['oferta_nome']} | Urgência: {jev_info['urgencia_score']}/2 | Perda local: {jev_info['perda_conversao_local']:.0%}")

        # 3. Análise Conversacional com Gemini AI considerando o histórico
        analysis = analyze_and_generate_reply(text, lead_name, history)
        intent = analysis.get("intent", "QUALIFICATION")
        stage = analysis.get("stage", "LISTENING")
        reasoning = analysis.get("reasoning", "")
        suggested_reply = analysis.get("suggested_reply", "")

        norm = normalize_text(text)

        # Fallback de regras caso Gemini não esteja ativo
        if not intent or intent == "OTHER":
            if any(re.search(rf"\b{re.escape(w)}\b", norm) for w in LGPD_OPTOUT_TRIGGERS):
                intent = "OPTOUT"
            elif any(re.search(rf"\b{re.escape(w)}\b", norm) for w in POSITIVE_TRIGGERS):
                intent = "POSITIVE"
            elif any(trigger in norm for trigger in BOT_GREETING_TRIGGERS):
                intent = "BOT_GREETING"

        # 4. Verificação de e-mail informado
        email_match = re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
        if email_match:
            lead_email = email_match.group(0).lower()
            print(f"   [📧] E-mail informado: {lead_email}")
            pdf_path = find_pdf_for_lead(lead_name)
            if pdf_path and os.path.exists(pdf_path):
                subj = f"Apresentação & Diagnóstico Visual — {lead_name}"
                body = f"<p>Olá!</p><p>Segue anexo o diagnóstico visual da <b>{lead_name}</b>.</p><p>Atenciosamente,<br><b>Eduardo Bovoline</b><br>Vocação Comunicação & Marketing</p>"
                ok = send_email(lead_email, subj, body, pdf_path)
                wa_msg = f"Perfeito! Acabei de encaminhar o documento completo para o e-mail {lead_email}. 📄✉️ Fico à disposição!"
                send_whatsapp_text(phone, wa_msg)
                
                # Gravação no CRM
                if company_id:
                    note_body = (
                        f"**E-mail informado no WhatsApp:** `{lead_email}`\n\n"
                        f"**Status de Envio:** {'Entregue com sucesso via Zoho Mail' if ok else 'Falha no disparo'}\n\n"
                        f"**Qualificação Jev:**\n"
                        f"- Oferta recomendada: {jev_info['oferta_nome']} (R$ {jev_info['oferta_preco']:.2f})\n"
                        f"- Urgência: {jev_info['urgencia_score']}/2\n"
                        f"- Probabilidade de Perda de Clientes Locais: {jev_info['perda_conversao_local']:.0%}"
                    )
                    record_lead_interaction(company_id, person_id, opportunity_id, "WhatsApp: E-mail Captado & Diagnóstico Enviado", note_body)
                    create_followup_task(company_id, person_id, opportunity_id, f"Follow-up E-mail — {lead_name}", f"Confirmar recebimento do e-mail com {lead_email}.")

                notify_admin(f"📧 *DIAGNÓSTICO ENVIADO POR E-MAIL!*\n• *Lead:* {lead_name}\n• *E-mail:* {lead_email}\n• *Twenty CRM:* ✅ Registrado")
            else:
                notify_admin(f"⚠️ *E-mail informado ({lead_email}), mas o PDF não foi localizado em disco.*")
            return

        # 5. Execução por Intenção
        if intent == "OPTOUT":
            record_optout(phone, lead_name)
            optout_reply = (
                "Compreendido perfeitamente! Seu número foi descadastrado imediatamente da nossa base. "
                "Não enviaremos mais nenhuma mensagem. Tenha uma excelente semana! 🙏"
            )
            send_whatsapp_text(phone, optout_reply)
            
            # CRM: grava optout no histórico
            if company_id:
                record_lead_interaction(
                    company_id, person_id, opportunity_id,
                    "LGPD: Descadastramento Solicitado",
                    f"**Lead pediu opt-out no WhatsApp:** \"{text}\"\n\n*Ação:* Número descadastrado e prospecção encerrada."
                )

            notify_admin(f"🚫 *OPTOUT LGPD:* Lead '{lead_name}' ({phone}) pediu descadastramento. CRM atualizado.")
            return

        if is_pdf_already_delivered(phone):
            if company_id:
                record_lead_interaction(
                    company_id, person_id, opportunity_id,
                    "WhatsApp: Mensagem Recebida pós-Diagnóstico",
                    f"**Mensagem recebida do lead:**\n> \"{text}\"\n\n*Atendimento humano recomendado.*"
                )
                create_followup_task(company_id, person_id, opportunity_id, f"Atender Lead pós-Diagnóstico — {lead_name}", f"Lead respondeu no WhatsApp: \"{text}\".")

            notify_admin(
                f"📩 *RESPOSTA DE LEAD (Pós-diagnóstico):*\n"
                f"• *Lead:* {lead_name}\n"
                f"• *Contato:* {phone}\n"
                f"• *Mensagem:* \"{text}\"\n"
                f"• *Twenty CRM:* ✅ Nota e tarefa criadas"
            )
            return

        # TRAVA DE HUMAN TAKEOVER & DIÁLOGO ATIVO
        HUMAN_MUTED_PHONES = {
            "996683892", # Estética Stella Maris (Débora / Dra. Stella - Atendimento Humano)
            "998500008", # BodyBe Sorocaba (Em negociação ativa)
            "996409494", # Lumiè Estética Avançada (Cooldown 48h)
            "976035867", # Gui (Indicação)
        }
        is_human_muted = any(hp in clean_phone for hp in HUMAN_MUTED_PHONES) or lead_info.get("is_indicacao", False)

        if is_human_muted:
            print(f"🛑 [HUMAN TAKEOVER ATIVO] Lead {lead_name} ({phone}) está sob atendimento humano direto. Bot 100% SILENCIADO.")
            if company_id:
                record_lead_interaction(
                    company_id, person_id, opportunity_id,
                    "WhatsApp: Mensagem Recebida (Modo Humano)",
                    f"**Lead:** \"{text}\"\n\n*Observação:* Bot silenciado para preservar o diálogo humano de Eduardo."
                )
            notify_admin(
                f"👤 *ATENDIMENTO HUMANO ({lead_name}):*\n"
                f"• *Mensagem:* \"{text}\"\n"
                f"• *Ação:* Bot silenciado. Prossiga no WhatsApp Web."
            )
            return

        if intent == "BOT_GREETING":
            if not is_already_bypassed(clean_phone) and AUTO_RESPONDER_ENABLED:
                bypass_msg = (
                    "Olá, tudo bem? Sou o Eduardo, da Vocação Comunicação aqui de Sorocaba.\n\n"
                    "Sei que este WhatsApp é focado no atendimento, então serei bem breve:\n\n"
                    "Vi a estrutura de vocês no Google e achei excelente, mas quem pesquisa pelos serviços na cidade ainda não encontra uma vitrine digital que passe essa mesma confiança de primeira.\n\n"
                    "Meu trabalho aqui é justamente esse: organizar a ficha do Maps e criar uma apresentação visual profissional para empresas locais, facilitando para o cliente decidir entrar em contato.\n\n"
                    "Como é um assunto ligado à imagem da empresa, você consegue me passar o contato da coordenação/diretoria ou este número já fala direto com quem decide?"
                )
                send_whatsapp_text(clean_phone, bypass_msg)
                record_bypassed(clean_phone, lead_name)
                
                if company_id:
                    record_lead_interaction(
                        company_id, person_id, opportunity_id,
                        "WhatsApp: Robô de Recepção Detectado",
                        f"**Mensagem do Robô:**\n> \"{text}\"\n\n*Ação:* Pedido humanizado do contato do decisor com foco em valor."
                    )
                notify_admin(f"🤖 *BOT DE RECEPÇÃO:* Pedido humanizado do decisor enviado para '{lead_name}' ({clean_phone}).")
            else:
                notify_admin(f"🤖 *BOT DE RECEPÇÃO DETECTADO ({lead_name}):*\n• Mensagem: \"{text}\"\n• Modo Manual Ativo: Nenhuma mensagem enviada.")
            return

        if intent == "POSITIVE":
            pdf_path = find_pdf_for_lead(lead_name)
            if not AUTO_RESPONDER_ENABLED:
                # MODO MANUAL SEGURO: Não envia automaticamente! Cria sugestão para aprovação.
                PENDING_APPROVALS["last_pending"] = {
                    "phone": phone,
                    "name": lead_name,
                    "reply": f"Perfeito! Segue o diagnóstico visual da {lead_name}. Dê uma olhada rápida (leva 2 minutos) e me diga se faz sentido pra vocês!",
                    "company_id": company_id,
                    "person_id": person_id,
                    "opportunity_id": opportunity_id,
                    "pdf_path": pdf_path
                }
                notify_admin(
                    f"🎯 *LEAD POSITIVO ({lead_name}):*\n"
                    f"• *Mensagem:* \"{text}\"\n"
                    f"• *Modo Manual Seguro:* PDF NÃO enviado automaticamente.\n"
                    f"• *Ação:* Envie '1' para autorizar o PDF ou envie pelo painel."
                )
                return

            if pdf_path and os.path.exists(pdf_path):
                ok = send_pdf_lead(phone, pdf_path, lead_name)
                if ok:
                    # 1. Atualiza oportunidade para MEETING com o valor calculado pelo Jev
                    update_lead_opportunity(company_id, stage="MEETING", amount_micros=jev_info["oferta_micros"])
                    
                    # 2. Grava nota detalhada com metadados do Jev
                    note_content = (
                        f"**Lead autorizou o envio do diagnóstico:**\n> \"{text}\"\n\n"
                        f"**Diagnóstico de Inteligência Jev (TypeSafe):**\n"
                        f"- **Oferta Recomendada:** {jev_info['oferta_nome']} (R$ {jev_info['oferta_preco']:.2f})\n"
                        f"- **Confiança do Jev:** {jev_info['oferta_confianca']:.0%}\n"
                        f"- **Urgência Comercial:** {jev_info['urgencia_score']}/2\n"
                        f"- **Perda de Clientes no Bairro:** {jev_info['perda_conversao_local']:.0%}\n\n"
                        f"**Ação Executada:** Diagnóstico visual oficial em PDF entregue no WhatsApp."
                    )
                    record_lead_interaction(company_id, person_id, opportunity_id, "WhatsApp: Diagnóstico Visual Entregue (Jev Qualificado)", note_content)

                    # 3. Cria tarefa de follow-up para Eduardo
                    create_followup_task(
                        company_id, person_id, opportunity_id,
                        f"Follow-up Diagnóstico — {lead_name}",
                        f"Avaliar reação do lead à oferta '{jev_info['oferta_nome']}' e agendar call comercial rápida."
                    )

                    notify_admin(
                        f"🚀 *DIAGNÓSTICO ENTREGUE NO WHATSAPP!*\n"
                        f"• *Lead:* {lead_name} ({phone})\n"
                        f"• *Oferta Jev:* {jev_info['oferta_nome']} (R$ {jev_info['oferta_preco']:.2f})\n"
                        f"• *Urgência:* {jev_info['urgencia_score']}/2 | *Perda local:* {jev_info['perda_conversao_local']:.0%}\n"
                        f"• *Twenty CRM:* ✅ Oportunidade atualizada para MEETING + Tarefa criada"
                    )
            else:
                notify_admin(
                    f"⚠️ *LEAD INTERESSADO (PDF pendente):*\n"
                    f"• *Lead:* {lead_name} ({phone})\n"
                    f"• *Mensagem:* \"{text}\"\n"
                    f"• *Ação:* PDF não encontrado em /app/leads."
                )
            return

        if intent in ["QUESTION", "OBJECTION", "QUALIFICATION"] or (suggested_reply and len(str(suggested_reply).strip()) >= 5):
            if not suggested_reply or len(str(suggested_reply).strip()) < 5:
                suggested_reply = (
                    f"Muito interessante, {lead_name}! Me conta um pouco mais sobre como funciona o modelo de negócio de vocês "
                    f"e quem é o cliente principal hoje."
                )

            PENDING_APPROVALS["last_pending"] = {
                "phone": phone,
                "name": lead_name,
                "reply": suggested_reply,
                "company_id": company_id,
                "person_id": person_id,
                "opportunity_id": opportunity_id
            }

            if company_id:
                record_lead_interaction(
                    company_id, person_id, opportunity_id,
                    f"WhatsApp: Interação do Lead ({intent.title()})",
                    f"**Mensagem do Lead:**\n> \"{text}\"\n\n"
                    f"**Análise de Conversa:** {reasoning}\n\n"
                    f"**Sugestão de Resposta Formulada:**\n> {suggested_reply}\n\n"
                    f"**Qualificação Jev:** {jev_info['oferta_nome']} (Urgência {jev_info['urgencia_score']}/2)"
                )
                create_followup_task(
                    company_id, person_id, opportunity_id,
                    f"Responder Lead — {lead_name}",
                    f"Lead enviou mensagem no WhatsApp: \"{text}\"."
                )

            notify_admin(
                f"🧠 *ANÁLISE INTELIGENTE (JEV + VOCAÇÃO):*\n"
                f"• *Lead:* {lead_name} ({phone})\n"
                f"• *Mensagem:* \"{text}\"\n"
                f"• *Oferta Jev:* {jev_info['oferta_nome']} (Urgência {jev_info['urgencia_score']}/2)\n\n"
                f"💬 *Sugestão de Resposta (Escuta Ativa):*\n"
                f"\"{suggested_reply}\"\n\n"
                f"👉 *Envie '1' no WhatsApp para autorizar o disparo imediato.*\n"
                f"👉 *Twenty CRM:* ✅ Nota e tarefa sincronizadas no card."
            )
            return

        # Mensagem geral
        if company_id:
            record_lead_interaction(
                company_id, person_id, opportunity_id,
                "WhatsApp: Mensagem Recebida",
                f"**Mensagem:**\n> \"{text}\"\n\n**Qualificação Jev:** {jev_info['oferta_nome']}"
            )
        notify_admin(
            f"📩 *MENSAGEM RECEBIDA DO LEAD:*\n"
            f"• *Lead:* {lead_name} ({phone})\n"
            f"• *Mensagem:* \"{text}\""
        )

def is_within_commercial_window():
    now = datetime.now()
    if now.weekday() >= 5: # Fim de semana
        return False
    return 9 <= now.hour < 18

def background_dispatcher_worker():
    """
    Motor de Disparo Automático 100% Dockerizado.
    Executa a cadência segura de prospecção (anti-bloqueio Meta) com respeito à janela comercial.
    """
    print("🚀 [DOCKER DISPATCHER] Motor de fila interno ativado...")
    while True:
        try:
            fila_path = os.path.join(DATA_DIR, "leads_ouro_fila_disparo.json")
            progresso_path = os.path.join(DATA_DIR, "fila_ouro_progresso.json")
            
            if os.path.exists(fila_path):
                leads = load_json_file(fila_path)
                progresso = load_json_file(progresso_path)
                sent_set = set(progresso.get("sent", []))
                failed_set = set(progresso.get("failed", []))
                optout_set = set(load_json_file(OPTOUT_FILE).keys())
                
                pending = [
                    l for l in leads 
                    if l.get("phone") not in sent_set 
                    and l.get("phone") not in failed_set 
                    and l.get("phone") not in optout_set
                ]
                
                if pending and is_within_commercial_window() and not QUEUE_PAUSED:
                    target = pending[0]
                    t_phone = target["phone"]
                    t_name = target["name"]
                    t_hook = target["hook_whatsapp"]
                    
                    # TRAVA FIXO VS CELULAR (Anti-falha WhatsApp)
                    if not is_mobile_phone(t_phone):
                        print(f"☎️ [DOCKER DISPATCHER] {t_name} ({t_phone}) é telefone fixo (sem WhatsApp). Descartado.")
                        if "failed" not in progresso: progresso["failed"] = []
                        progresso["failed"].append(t_phone)
                        DISPATCH_LOGS.append({
                            "time": datetime.now().strftime("%H:%M:%S"),
                            "status": "failed",
                            "reason": "Telefone Fixo (Sem WhatsApp)",
                            "name": t_name,
                            "phone": t_phone,
                            "bairro": target.get("bairro", ""),
                            "oferta": target.get("oferta_nome", "").split("(")[0].strip()
                        })
                        save_json_file(LOGS_FILE, DISPATCH_LOGS[-100:])
                        save_json_file(progresso_path, progresso)
                        cur_leads = load_json_file(fila_path)
                        if isinstance(cur_leads, list):
                            cur_leads = [l for l in cur_leads if l.get("phone") != t_phone]
                            save_json_file(fila_path, cur_leads)
                        continue

                    # TRAVA ABSOLUTA ANTI-DUPLICAÇÃO (Histórico Geral + CSVs + CRM + Evolution)
                    is_virgin, block_reason = is_lead_strictly_virgin(t_phone, t_name)
                    if not is_virgin:
                        print(f"🛑 [TRAVA DE SEGURANÇA MÁXIMA] {t_name} ({t_phone}) BLOQUEADO: {block_reason}. Disparo CANCELADO.")
                        if "sent" not in progresso: progresso["sent"] = []
                        progresso["sent"].append(t_phone)
                        save_json_file(progresso_path, progresso)
                        continue

                    print(f"\n📦 [DOCKER DISPATCHER] Disparando para {t_name} ({t_phone})...")
                    success = False
                    try:
                        url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
                        payload = {"number": t_phone, "text": t_hook}
                        headers = {"apikey": API_KEY, "Content-Type": "application/json"}
                        r = requests.post(url, json=payload, headers=headers, timeout=15)
                        success = (r.status_code in [200, 201])
                    except Exception as e:
                        print(f"[!] Erro disparo interno Docker para {t_phone}: {e}")
                        
                    if "sent" not in progresso: progresso["sent"] = []
                    if "failed" not in progresso: progresso["failed"] = []
                    
                    if success:
                        progresso["sent"].append(t_phone)
                        append_chat_history(t_phone, "Vocação (Hook Prospecção)", t_hook)
                        print(f"   ✅ [DOCKER DISPATCHER] Entregue com sucesso para {t_name}!")
                    else:
                        progresso["failed"].append(t_phone)
                        print(f"   ❌ [DOCKER DISPATCHER] Falha no disparo para {t_name}.")
                        
                    DISPATCH_LOGS.append({
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "status": "success" if success else "failed",
                        "reason": "Entregue via WhatsApp" if success else "Sem WhatsApp ou falha na API",
                        "name": t_name,
                        "phone": t_phone,
                        "bairro": target.get("bairro", ""),
                        "oferta": target.get("oferta_nome", "").split("(")[0].strip()
                    })
                    save_json_file(LOGS_FILE, DISPATCH_LOGS[-100:])
                    save_json_file(progresso_path, progresso)

                    # Remove o lead contactado da fila ativa para desocupar a coluna imediatamente
                    cur_leads = load_json_file(fila_path)
                    if isinstance(cur_leads, list):
                        cur_leads = [l for l in cur_leads if l.get("phone") != t_phone]
                        save_json_file(fila_path, cur_leads)
                    
                    if len(pending) == 1:
                        notify_admin(
                            f"🏁 *DISPAROS DOCKER CONCLUÍDOS!*\n\n"
                            f"Todos os 30 leads da fila ouro foram processados!\n"
                            f"• Entregues: {len(progresso.get('sent', []))}\n"
                            f"• Sem WhatsApp: {len(progresso.get('failed', []))}\n\n"
                            f"O motor agora monitora e atende as respostas automaticamente!"
                        )
                    else:
                        sleep_time = random.randint(240, 360)
                        print(f"   ⏳ [DOCKER DISPATCHER] Aguardando {sleep_time}s (~{round(sleep_time/60, 1)} min) para o próximo lead...")
                        global NEXT_DISPATCH_SECONDS_LEFT
                        for sec in range(sleep_time, 0, -1):
                            NEXT_DISPATCH_SECONDS_LEFT = sec
                            if FORCE_DISPATCH_EVENT.is_set():
                                FORCE_DISPATCH_EVENT.clear()
                                print("   ⚡ [DOCKER DISPATCHER] Disparo forçado pelo gestor no Sub-CRM!")
                                break
                            while QUEUE_PAUSED:
                                NEXT_DISPATCH_SECONDS_LEFT = 0
                                time.sleep(1)
                            time.sleep(1)
                        NEXT_DISPATCH_SECONDS_LEFT = 0
                        continue
        except Exception as e:
            print(f"[!] Erro no loop do dispatcher Docker: {e}")
            
        time.sleep(30)

if __name__ == "__main__":
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, WebhookHandler)
    print(f"🚀 [VOCAÇÃO DOCKER + JEV] Auto-responder ativo na porta {PORT}...")
    print(f"   Evolution API: {EVOLUTION_API_URL}")
    print(f"   Gemini AI: {'🟢 ATIVO' if os.environ.get('GEMINI_API_KEY') else '⚪ MODO REGRAS'}")
    print(f"   Jev System One: 🟢 ATIVO (Model: jev-latest)")
    print(f"   Twenty CRM: 🟢 CONECTADO (Postgres + Targets)")
    print(f"   Painel Web: 🟢 ATIVO em /painel (Portas 5680 e 8000)")
    
    # Inicia motor de fila Docker em background
    threading.Thread(target=background_dispatcher_worker, daemon=True).start()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
