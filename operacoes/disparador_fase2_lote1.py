"""
disparador_fase2_lote1.py — Fila de Retomada (Fase 2) — Vocação Comunicação & Marketing

PLANO ANTI-BAN REFORÇADO:
  • Máximo 15 disparos por sessão
  • Intervalo entre mensagens: 8 a 14 minutos (aleatório)
  • Checagem automática de delivered_leads.json (não queima leads já abordados)
  • Leads: 5 Marcenarias pendentes + 4 Pilates sem resposta (prioridade)
"""

import os
import re
import sys
import time
import json
import random
import requests
import subprocess
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

EVOLUTION_API_URL = "http://localhost:8080"
INSTANCE_NAME     = "vocacao_comercial"
API_KEY           = "vocacao_update_secret_key_2026"
ADMIN_WHATSAPP    = "5515981512083"
DOCKER_BIN        = r"C:\Program Files\Docker\Docker\resources\bin\docker.exe"
SCHEMA            = "workspace_2xmx8hech9nybwidia3404k2z"
BASE_DIR          = os.path.dirname(__file__)
DELIVERED_FILE    = os.path.join(BASE_DIR, "delivered_leads.json")

# Cache de chats ativos (carregado uma vez no início da fila para economizar chamadas)
_active_chats_cache = None

def load_active_chats():
    """
    Busca todos os chats abertos na Evolution API.
    Retorna um set com os últimos 8 dígitos de cada número que já tem histórico.
    Cache válido por toda a sessão de disparos.
    """
    global _active_chats_cache
    if _active_chats_cache is not None:
        return _active_chats_cache

    try:
        url = f"{EVOLUTION_API_URL}/chat/findChats/{INSTANCE_NAME}"
        resp = requests.get(url, headers={"apikey": API_KEY}, timeout=15)
        if resp.status_code == 200:
            chats = resp.json()
            # Extrai os números de todos os chats individuais (ignora grupos @g.us)
            numbers = set()
            for chat in chats:
                jid = chat.get("id", "") or chat.get("remoteJid", "")
                if "@s.whatsapp.net" in jid:
                    digits = re.sub(r"\D", "", jid.split("@")[0])
                    if digits:
                        numbers.add(digits[-8:])  # últimos 8 dígitos para matching flexível
            _active_chats_cache = numbers
            print(f"[✓] Histórico carregado: {len(numbers)} chats ativos conhecidos.")
            return numbers
        else:
            print(f"[!] Não foi possível carregar histórico de chats: {resp.status_code}")
            return set()
    except Exception as e:
        print(f"[!] Erro ao carregar chats ativos: {e}")
        return set()

def has_existing_chat(number):
    """
    Retorna True se o número já tem conversa aberta na nossa conta WA.
    Usa os últimos 8 dígitos para matching flexível (ignora DDI/DDD variações).
    """
    active = load_active_chats()
    last8 = re.sub(r"\D", "", number)[-8:]
    return last8 in active



# ────────────────────────────────────────────────
# LOTE DA FASE 2 — máximo 15 leads (anti-ban)
# Ordem: pendentes com prioridade > marcenarias novas
# ────────────────────────────────────────────────
QUEUE = [
    # ── 5 Marcenarias que não foram enviadas (WA estava suspenso) ──
    {
        "name": "Wbilino Conceito Mármores de Luxo",
        "number": "5515991210000",
        "hook": (
            "Olá, tudo bem? Analisei a presença digital da Wbilino no segmento de mármores e superfícies de luxo em Sorocaba "
            "e notei algo estratégico: a qualidade dos projetos é excepcional, mas quem pesquisa por mármore premium no Google "
            "na Zona Sul encontra pouca diferenciação visual do espaço de vocês antes do orçamento. "
            "Posso te enviar um diagnóstico visual de 2 minutos mostrando como posicionar a Wbilino como referência?"
        )
    },
    {
        "name": "Marmoraria Santos",
        "number": "5515988180072",
        "hook": (
            "Olá, tudo bem? Analisei a presença digital da Marmoraria Santos em Sorocaba e notei um ponto estratégico: "
            "vocês têm tradição e entrega de qualidade reconhecida, mas quem pesquisa por bancada em mármore ou granito no Google "
            "ainda encontra dificuldade para ver o portfólio antes de pedir orçamento. "
            "Posso te enviar um diagnóstico visual de 2 minutos mostrando como resolver isso?"
        )
    },
    {
        "name": "Marcenaria Domke",
        "number": "5515988137613",
        "hook": (
            "Olá, tudo bem? Analisei a presença digital da Marcenaria Domke em Sorocaba e notei um detalhe relevante: "
            "o trabalho de vocês em móveis planejados tem ótima reputação, mas nas buscas do Google clientes que pesquisam "
            "por marcenaria planejada no Campolim e ZS encontram poucos elementos visuais antes de chamar no WhatsApp. "
            "Posso te enviar um diagnóstico rápido mostrando como triplicar essa captação online?"
        )
    },
    {
        "name": "Todeschini Sorocaba",
        "number": "5515991287563",
        "hook": (
            "Olá equipe Todeschini Sorocaba, tudo bem? Analisei a presença digital da loja e notei um ponto de alavancagem: "
            "a marca nacional tem grande força, mas o perfil local da unidade no Google Maps ainda não traduz o padrão premium "
            "da loja para quem pesquisa por cozinha planejada de alto padrão em Sorocaba. "
            "Posso te enviar um diagnóstico visual de 2 minutos sobre como fortalecer o posicionamento local?"
        )
    },
    {
        "name": "Impeccabile Móveis Planejados",
        "number": "5515910640282",
        "hook": (
            "Olá, tudo bem? Analisei a presença digital da Impeccabile em Sorocaba e notei um contraste interessante: "
            "o nome e o conceito transmitem alto padrão, mas quem busca por marcenaria de luxo no Google na Zona Sul "
            "encontra pouca profundidade na vitrine digital antes de visitar a loja. "
            "Posso te enviar um diagnóstico visual de 2 minutos mostrando como alinhar o posicionamento online ao nível do espaço?"
        )
    },
    # ── 4 Pilates sem resposta registrada (follow-up mais suave) ──
    {
        "name": "Classic Pilates e Fisioterapia",
        "number": "5515991315847",
        "hook": (
            "Olá, tudo bem? Passei por aqui novamente porque analisei mais a fundo a presença digital da Classic Pilates "
            "no Central Parque e encontrei uma oportunidade clara de posicionamento que achei válido compartilhar. "
            "Te envio um diagnóstico visual rápido (2 páginas) sem compromisso — quer dar uma olhada?"
        )
    },
    {
        "name": "Flávia Fernandes Pilates Studio",
        "number": "5515988119242",
        "hook": (
            "Olá Flávia, tudo bem? Gostaria de compartilhar o diagnóstico visual que preparei sobre a presença digital "
            "do seu studio na Vila Jardini. São 2 páginas objetivas com o gargalo principal que identifiquei — "
            "posso encaminhar?"
        )
    },
    {
        "name": "Pilates Movy-se",
        "number": "5515997539318",
        "hook": (
            "Olá equipe Mova-se, tudo bem? Preparei um diagnóstico visual rápido sobre a presença digital do studio "
            "e encontrei um ponto de melhoria relevante para a captação de alunos da região. "
            "Posso te enviar? São 2 minutos de leitura."
        )
    },
    {
        "name": "Pilates Mamy Baby",
        "number": "5515998049147",
        "hook": (
            "Olá, tudo bem? Finalizei o diagnóstico visual do Pilates Mamy Baby e o ponto crítico que detectei "
            "no perfil de vocês merece atenção antes que o concorrente corrija primeiro. "
            "Posso te enviar? São 2 páginas rápidas."
        )
    },
]

# ────────────────────────────────────────────────
# Helpers
# ────────────────────────────────────────────────

def load_delivered():
    if os.path.exists(DELIVERED_FILE):
        try:
            with open(DELIVERED_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def is_already_delivered(number):
    """Protege contra reenvio para quem já recebeu o diagnóstico."""
    data = load_delivered()
    clean_num = number[-8:]
    for k in data:
        if k[-8:] == clean_num:
            return True
    return False

from CONFIG_MOTOR_DISPARO_VOCACOES_START import ensure_lgpd_compliance

def send_whatsapp(number, text):
    if str(number) != str(ADMIN_WHATSAPP):
        text = ensure_lgpd_compliance(text)
    url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
    headers = {"apikey": API_KEY, "Content-Type": "application/json"}
    payload = {
        "number": number,
        "text": text,
        "options": {"linkPreview": False, "delay": 1500}
    }
    resp = requests.post(url, json=payload, headers=headers, timeout=20)
    return resp.status_code, resp.json()

def notify_admin(msg):
    send_whatsapp(ADMIN_WHATSAPP, msg)

def update_crm_stage(company_name):
    first_word = company_name.split()[0]
    sql = f"""
    UPDATE "{SCHEMA}"."opportunity" o
    SET stage = 'SCREENING', "updatedAt" = NOW()
    FROM "{SCHEMA}"."company" c
    WHERE o."companyId" = c.id AND c.name ILIKE '%{first_word}%';
    """
    proc = subprocess.Popen(
        [DOCKER_BIN, "exec", "-i", "twenty-db-1", "psql", "-U", "postgres", "-d", "twenty"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        text=True, encoding="utf-8"
    )
    proc.communicate(input=sql)

# ────────────────────────────────────────────────
# Runner principal
# ────────────────────────────────────────────────

def run_queue(min_interval=480, max_interval=840):
    """
    min_interval=480  → 8 minutos mínimo
    max_interval=840  → 14 minutos máximo
    """
    # Filtra leads já entregues antes de iniciar
    queue_filtered = [l for l in QUEUE if not is_already_delivered(l["number"])]
    skipped = len(QUEUE) - len(queue_filtered)

    total = len(queue_filtered)
    print("=" * 54)
    print(f"🚀 DISPARADOR FASE 2 — LOTE 1 — ANTI-BAN REFORÇADO")
    print(f"   Total de leads na fila: {total}  |  Pulados (já entregues): {skipped}")
    print(f"   Intervalo: {min_interval//60}–{max_interval//60} min entre mensagens")
    print("=" * 54)

    if total == 0:
        print("Nenhum lead novo para disparar. Encerrando.")
        return

    notify_admin(
        f"🚀 *FASE 2 INICIADA*\n"
        f"• Lote: {total} leads (pulados: {skipped} já entregues)\n"
        f"• Intervalo anti-ban: {min_interval//60}–{max_interval//60} min\n"
        f"• Previsão de conclusão: ~{round(total * (min_interval + max_interval) / 2 / 60)} min"
    )

    for i, lead in enumerate(queue_filtered):
        idx = i + 1
        now_str = datetime.now().strftime("%H:%M:%S")
        print(f"\n[{idx}/{total}] [{now_str}] → {lead['name']} ({lead['number']})")

        # Checagem de segurança na hora do disparo
        if is_already_delivered(lead["number"]):
            print(f"   [SKIP] Já entregue. Pulando.")
            continue

        # Checagem de histórico — não interromper quem já nos conhece com mensagem automática
        if has_existing_chat(lead["number"]):
            print(f"   [⚠️ HISTÓRICO] {lead['name']} já tem conversa aberta. Pulando disparo automático.")
            notify_admin(
                f"⚠️ *HISTÓRICO DETECTADO — AÇÃO MANUAL:*\n"
                f"• *Lead:* {lead['name']}\n"
                f"• *Número:* {lead['number']}\n"
                f"• Já tem conversa aberta no WA. Aborde manualmente para não parecer robô."
            )
            continue

        status, data = send_whatsapp(lead["number"], lead["hook"])
        msg_id = data.get("key", {}).get("id", "N/A")
        print(f"   Status {status} | Msg ID: {msg_id}")

        update_crm_stage(lead["name"])

        if i < total - 1:
            sleep_seconds = random.randint(min_interval, max_interval)
            sleep_min = round(sleep_seconds / 60, 1)
            notify_admin(
                f"✅ *[{idx}/{total}] Enviado:* {lead['name']}\n"
                f"📱 {lead['number']}\n"
                f"⏱️ Próximo disparo em {sleep_min} min ({sleep_seconds}s)"
            )
            print(f"   Aguardando {sleep_min} min anti-ban...")
            time.sleep(sleep_seconds)
        else:
            notify_admin(
                f"✅ *[{idx}/{total}] Enviado:* {lead['name']}\n"
                f"📱 {lead['number']}\n"
                f"🏁 Lote 1 da Fase 2 concluído!"
            )

    print("\n★ FASE 2 — LOTE 1 CONCLUÍDO! ★")
    notify_admin(f"🎉 *FASE 2 LOTE 1 FINALIZADO!* {total} leads abordados com intervalo anti-ban reforçado.")

if __name__ == "__main__":
    min_i = 480   # 8 min padrão
    max_i = 840   # 14 min padrão
    if len(sys.argv) > 2 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
        min_i = int(sys.argv[1])
        max_i = int(sys.argv[2])
    run_queue(min_i, max_i)
