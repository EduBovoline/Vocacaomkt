"""
CONFIG_MOTOR_DISPARO_VOCACOES_START.py
Módulo Central de Regras, Janelas Estratégicas e Compliance LGPD para Disparos da Vocação
Atualizado: 28/09/2026
"""

import os
import re
import json
import random
from datetime import datetime, time

# Configurações de API & Instância
EVOLUTION_API_URL = "http://localhost:8080"
INSTANCE_NAME     = "vocacao_comercial"
API_KEY           = "vocacao_update_secret_key_2026"
ADMIN_WHATSAPP    = "5515981512083"

# Limites e Cadência Segura WhatsApp (Meta Rate Limit & Anti-Ban)
WHATSAPP_LIMITS = {
    "MAX_DAILY_SENDS": 15,            # Teto diário de segurança por chip
    "MIN_INTERVAL_SECONDS": 360,       # 6 minutos mínimo entre envios
    "MAX_INTERVAL_SECONDS": 720,       # 12 minutos máximo entre envios
    "BLOCK_SIZE": 4,                   # Pausa obrigatória a cada 4 envios
    "BLOCK_PAUSE_MIN_SECONDS": 1500,   # 25 minutos de respiro
    "BLOCK_PAUSE_MAX_SECONDS": 2100,   # 35 minutos de respiro
}

# Limites E-mail B2B
EMAIL_LIMITS = {
    "MAX_DAILY_SENDS": 40,
    "MIN_INTERVAL_SECONDS": 60,
    "MAX_INTERVAL_SECONDS": 180,
}

# Janelas Estratégicas de Máxima Conversão (Horários de Ouro)
# Janela 1: 10h00 às 11h45 (após abertura da manhã, antes do almoço)
# Janela 2: 14h15 às 16h45 (após almoço, decisões da tarde)
GOLDEN_WINDOWS = [
    (time(10, 0), time(11, 45)),
    (time(14, 15), time(16, 45))
]

def is_in_golden_window(dt=None):
    """
    Verifica se o momento atual está dentro das Janelas de Ouro de conversão.
    Retorna: (bool_permitido, str_motivo)
    """
    if dt is None:
        dt = datetime.now()
    
    # Bloqueio em finais de semana (0=Segunda, 6=Domingo)
    if dt.weekday() >= 5:
        return False, "Fim de semana: disparos comerciais congelados para evitar denúncias de spam."
    
    current_time = dt.time()
    
    for start, end in GOLDEN_WINDOWS:
        if start <= current_time <= end:
            return True, f"Dentro da Janela de Ouro ({start.strftime('%H:%M')} às {end.strftime('%H:%M')})."
    
    if current_time < time(10, 0):
        return False, "Antes das 10h00: horário inconveniente de abertura de loja. Próxima janela: 10h00."
    elif time(11, 45) < current_time < time(14, 15):
        return False, "Horário de Almoço (11h45 - 14h15): pico de balcão e ausência de decisores. Próxima janela: 14h15."
    else:
        return False, "Após as 16h45: fechamento de caixa e encerramento. Próxima janela: amanhã às 10h00."

def generate_compliant_hook(lead_name, segment="seu segmento", neighborhood="na sua região", contact_name=""):
    """
    Gera a copy oficial humanizada Vocação Start com opt-out LGPD rigoroso.
    Sem bajulação de 'espaço excelente' e sem links no primeiro toque.
    """
    greeting = f"Opa {contact_name}, tudo bem?" if contact_name else "Olá, tudo bem?"
    
    text = (
        f"{greeting} Edu aqui da Vocação Comunicação & Marketing em Sorocaba.\n\n"
        f"Estava pesquisando as empresas de {segment} no {neighborhood} e encontrei o contato da {lead_name}.\n\n"
        f"Vi que vocês têm um trabalho sério na região, mas a apresentação da empresa no Google ainda não reflete isso — "
        f"faltam fotos atualizadas e um canal direto para o WhatsApp de atendimento.\n\n"
        f"Eu montei um resumo rápido mostrando como organizar a presença digital de vocês para quem pesquisar no bairro já abrir conversa direto no seu atendimento.\n\n"
        f"Se fizer sentido, te mando aqui pra você dar uma olhada (leva nem 2 minutos). Abraço!\n\n"
        f"_Contato comercial via dados públicos do Google Maps. Se não desejar receber mensagens, basta responder 'PARAR'._"
    )
    return text

def generate_compliant_followup_hook(lead_name, contact_name=""):
    """
    Gera copy de follow-up humanizada, sóbria e com opt-out LGPD rigoroso.
    Sem bajulação, sem pressão e com saída limpa.
    """
    greeting = f"Opa {contact_name}, tudo bem?" if contact_name else "Olá, tudo bem?"
    text = (
        f"{greeting} Edu aqui da Vocação.\n\n"
        f"Passando apenas para checar se você conseguiu ver minha mensagem anterior sobre a presença digital da {lead_name} no Google.\n\n"
        f"Como comentei, montei um resumo visual de 2 minutos com os principais gargalos e oportunidades que identifiquei no perfil de vocês.\n\n"
        f"Se fizer sentido dar uma olhada rápida, me avisa por aqui que te encaminho. Abraço!\n\n"
        f"_Para não receber mais mensagens, basta responder 'PARAR'._"
    )
    return text

def ensure_lgpd_compliance(message_text):
    """
    Garante que qualquer mensagem comercial tenha a cláusula de opt-out LGPD.
    Se não tiver, anexa automaticamente.
    """
    if "PARAR" not in message_text:
        message_text = message_text.strip() + "\n\n_Para não receber mais mensagens, responda 'PARAR'._"
    return message_text


def is_blacklisted(phone_or_email, blacklist_path="optout_blacklist.json"):
    """Verifica se o lead solicitou descadastro previamente."""
    if not os.path.exists(blacklist_path):
        return False
    try:
        with open(blacklist_path, "r", encoding="utf-8") as f:
            b_list = json.load(f)
            clean = re.sub(r"\D", "", str(phone_or_email))
            return clean in b_list or str(phone_or_email).lower() in b_list
    except Exception:
        return False
