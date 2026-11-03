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

# P3 (auditoria): saída sempre em UTF-8, inclusive no console cp1252 do Windows.
import vocacao_seguranca  # noqa: F401  — o import já chama forcar_utf8()

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
    Copy oficial do primeiro toque (P2 da auditoria).

    Regra de ouro: NÃO afirmar nada sobre o lead que não tenha sido confirmado
    no diagnóstico gerado (fotos, site, WhatsApp, e-mail). A abordagem vende a
    análise, não uma acusação. Sem bajulação, sem link e com opt-out LGPD.
    """
    greeting = f"Opa {contact_name}, tudo bem?" if contact_name else "Olá, tudo bem?"

    text = (
        f"{greeting} Edu aqui da Vocação, de Sorocaba.\n\n"
        f"Estava mapeando {segment} aqui na região do {neighborhood} e separei uma análise rápida "
        f"de 2 minutos sobre como quem mora no bairro encontra e escolhe a {lead_name} pelo Google Maps no celular.\n\n"
        f"É um retrato de como a empresa aparece hoje na busca — feito com dados públicos, sem achismo.\n\n"
        f"Posso te mandar por aqui para você dar uma olhada? Abraço!\n\n"
        f"_Contato comercial via dados públicos do Google Maps. Se não desejar receber mensagens, basta responder 'PARAR'._"
    )
    return text

def generate_compliant_followup_hook(lead_name, contact_name=""):
    """
    Follow-up humanizado, sóbrio e com opt-out LGPD rigoroso.
    Não repete acusações técnicas e não usa o jargão "se fizer sentido".
    """
    greeting = f"Opa {contact_name}, tudo bem?" if contact_name else "Olá, tudo bem?"
    text = (
        f"{greeting} Edu aqui da Vocação.\n\n"
        f"Passando para saber se você chegou a ver minha mensagem sobre como a {lead_name} aparece nas buscas do Google no bairro.\n\n"
        f"Se quiser, envio o resumo de 2 minutos que montei — é só responder 'quero ver'.\n\n"
        f"Se preferir não receber mais nada, responde 'PARAR' que eu encerro o contato na hora.\n\n"
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
