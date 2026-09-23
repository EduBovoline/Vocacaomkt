"""
disparador_fila_7min.py — Disparador em fila com espaçamento seguro de 7 minutos
Vocação Comunicação & Marketing
"""

import os
import sys
import time
import requests
import subprocess
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

EVOLUTION_API_URL = "http://localhost:8080"
INSTANCE_NAME = "vocacao_comercial"
API_KEY = "vocacao_update_secret_key_2026"
ADMIN_WHATSAPP = "5515981512083"
DOCKER_BIN = r"C:\Program Files\Docker\Docker\resources\bin\docker.exe"
SCHEMA = "workspace_2xmx8hech9nybwidia3404k2z"

QUEUE = [
    {
        "name": "Lumiè Estética Avançada",
        "number": "5515996409494",
        "hook": "Olá, tudo bem? Analisei a presença digital da Lumiè no Campolim e notei um ponto crítico: o espaço de vocês na José Maria Hanickel tem excelente estrutura para estética avançada, mas quem busca pelos seus procedimentos no Google encontra informações dispersas sem um Tour Virtual 360° no Street View nem autoridade institucional alinhada ao padrão de alto ticket da clínica. Posso te enviar um diagnóstico visual de 2 minutos mostrando como corrigir isso?"
    },
    {
        "name": "BodyBe Sorocaba",
        "number": "5515998500008",
        "hook": "Olá, tudo bem? Analisei a presença digital da BodyBe no Jardim Faculdade e notei um detalhe estratégico: vocês oferecem uma proposta tecnológica inovadora de estética integrada, mas na bio e no Google o paciente de Sorocaba cai em um Linktree genérico em vez de uma vitrine digital de autoridade com a sofisticação da marca. Posso te enviar um diagnóstico visual de 2 minutos mostrando como resolver esse gargalo?"
    },
    {
        "name": "Estética Stella Maris",
        "number": "5515996683892",
        "hook": "Olá, tudo bem? Analisei a presença digital da Stella Maris no Jardim Emília e notei algo importante: o espaço de vocês na Washington Luiz é super conceituado, mas quem pesquisa pelos tratamentos no Google não encontra uma vitrine institucional com domínio próprio, caindo em links secundários de redes sociais. Isso faz vocês perderem pacientes de alto ticket para clínicas vizinhas do Campolim. Posso te enviar um diagnóstico visual de 2 minutos mostrando como corrigir isso?"
    },
    {
        "name": "Aliane Carmo Harmonização Facial",
        "number": "5515996201252",
        "hook": "Olá Dra. Aliane, tudo bem? Analisei a presença digital do seu consultório no Campolim e notei um detalhe crucial: vocês realizam procedimentos de altíssimo nível em injetáveis e HOF, mas nas buscas do Google os pacientes encontram apenas o perfil do aplicativo Fresha e não uma vitrine médica institucional com a autoridade que o endereço de vocês na João Dias de Souza merece. Posso te enviar um diagnóstico visual de 2 minutos mostrando como blindar as buscas da sua clínica?"
    },
    {
        "name": "Clínica Dra. Audrey Naufal",
        "number": "5515988331983",
        "hook": "Olá Dra. Audrey, tudo bem? Analisei a presença digital da sua clínica em Sorocaba e notei um contraste importante: a senhora tem uma autoridade gigante ministrando cursos e atendendo em HOF avançada, mas quem pesquisa pelo seu consultório no Google não encontra um portal institucional de referência para procedimentos clínicos, caindo em plataformas de agendamento genéricas. Posso te enviar um diagnóstico visual de 2 minutos mostrando como estruturar essa vitrine de autoridade?"
    }
]

def send_whatsapp(number, text):
    url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
    headers = {
        "apikey": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "number": number,
        "text": text,
        "options": {
            "linkPreview": False,
            "delay": 1200
        }
    }
    resp = requests.post(url, json=payload, headers=headers, timeout=20)
    return resp.status_code, resp.json()

def notify_admin(msg):
    send_whatsapp(ADMIN_WHATSAPP, msg)

def update_crm_stage(company_name):
    sql = f"""
    UPDATE "{SCHEMA}"."opportunity" o
    SET stage = 'CONTACTED', "updatedAt" = NOW()
    FROM "{SCHEMA}"."company" c
    WHERE o."companyId" = c.id AND c.name ILIKE '%{company_name}%';
    """
    proc = subprocess.Popen(
        [DOCKER_BIN, "exec", "-i", "twenty-db-1", "psql", "-U", "postgres", "-d", "twenty"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8"
    )
    proc.communicate(input=sql)

def run_queue():
    total = len(QUEUE)
    print(f"==================================================")
    print(f"Iniciando fila de {total} disparos (intervalo: 7 min)")
    print(f"==================================================")
    
    notify_admin(f"🚀 *DISPAROS INICIADOS:* Aprovado! Fila de {total} leads em andamento com espaçamento de 7 minutos.")

    for i, lead in enumerate(QUEUE):
        idx = i + 1
        print(f"\n[{idx}/{total}] Disparando para {lead['name']} ({lead['number']})...")
        status, data = send_whatsapp(lead["number"], lead["hook"])
        msg_id = data.get("key", {}).get("id", "N/A")
        print(f"-> Status {status} | Msg ID: {msg_id}")
        
        update_crm_stage(lead["name"])
        notify_admin(f"✅ *[{idx}/{total}] Enviado:* {lead['name']}\n📱 {lead['number']}\n⏱️ Próximo envio em 7 minutos.")

        if i < total - 1:
            print("Aguardando 7 minutos (420 segundos)...")
            time.sleep(420)

    print("\n★ TODOS OS 5 DISPAROS FORAM CONCLUÍDOS COM SUCESSO! ★")
    notify_admin(f"🎉 *LOTE CONCLUÍDO:* Todos os {total} leads de Sorocaba foram abordados no WhatsApp. Aguardando respostas para disparo automático dos diagnósticos!")

if __name__ == "__main__":
    run_queue()
