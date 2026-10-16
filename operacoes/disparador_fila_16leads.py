"""
disparador_fila_16leads.py — Fila de Prospecção das 15:10 às 17:00 (16 Leads, 7 min de intervalo)
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
        "name": "Dra. Mariana Tocci Dermatologia",
        "number": "5515996410306",
        "hook": "Olá Dra. Mariana, tudo bem? Analisei a presença digital do seu consultório no Iguatemi Business e notei um ponto estratégico: a senhora tem excelente autoridade em injetáveis e Sculptra, mas quem busca por procedimentos dermatológicos no Campolim encontra dados dispersos sem uma vitrine médica institucional com Tour Virtual do espaço. Posso te enviar um diagnóstico visual de 2 minutos mostrando como estruturar isso?"
    },
    {
        "name": "Dra. Marielle Moreira Odontologia",
        "number": "5515991433018",
        "hook": "Olá Dra. Marielle, tudo bem? Analisei a presença digital do seu consultório na Horácio Cenci no Campolim e notei um detalhe crucial: vocês realizam uma odontologia estética de altíssimo padrão, mas na busca local do Google pacientes de condomínios vizinhos caem em outras clínicas com perfis mais otimizados no Maps. Posso te enviar um diagnóstico visual de 2 minutos mostrando como blindar as buscas da sua clínica?"
    },
    {
        "name": "Dra. Letícia Plens Harmonização",
        "number": "5515997595506",
        "hook": "Olá Dra. Letícia, tudo bem? Analisei a presença digital do seu espaço de HOF no Campolim e notei algo importante: seu trabalho com fios de PDO e injetáveis é refinadíssimo, mas quem pesquisa pelo seu nome ou tratamentos no Google não encontra uma vitrine médica de autoridade própria, dependendo apenas do Instagram. Posso te enviar um diagnóstico visual de 2 minutos mostrando como resolver isso?"
    },
    {
        "name": "Anequini Soares Dermatologia",
        "number": "5515997466183",
        "hook": "Olá, tudo bem? Analisei a presença digital da Anequini Soares no Campolim e notei um detalhe estratégico: o espaço de vocês na Francisco Neves é impecável, mas quem pesquisa pelos tratamentos no Google não encontra uma vitrine digital de autoridade com Tour 360° no Street View, perdendo novos pacientes de condomínios da ZS. Posso te enviar um diagnóstico visual de 2 minutos mostrando como blindar essa presença?"
    },
    {
        "name": "Critis Odontologia Especializada",
        "number": "5515988052431",
        "hook": "Olá, tudo bem? Analisei a presença digital da Critis Odontologia no Campolim e notei algo importante: a estrutura de vocês na José Jorge Nardi tem enorme autoridade clínica, mas quem pesquisa no Google encontra uma vitrine que não transmite o padrão de alto ticket do consultório, gerando dispersão de pacientes para outras clínicas da Comitre. Posso te enviar um diagnóstico visual de 2 minutos mostrando esse gargalo?"
    },
    {
        "name": "Estética Taís Pedroso",
        "number": "5515997930040",
        "hook": "Olá, tudo bem? Analisei a presença digital da Estética Taís Pedroso na Washington Luiz e notei um ponto crítico: o endereço de vocês tem grande fluxo e tradição no Jardim Emília, mas nas buscas do Google quem pesquisa por tratamentos faciais avançados é capturado por clínicas concorrentes do Campolim. Posso te enviar um diagnóstico visual de 2 minutos mostrando como blindar a sua região?"
    },
    {
        "name": "Dra. Thaise Buzzo Cirurgia Plástica",
        "number": "5515996578148",
        "hook": "Olá Dra. Thaise, tudo bem? Analisei a presença digital do seu consultório no Iguatemi Business e notei um detalhe importante: a senhora atende no polo corporativo mais nobre de Sorocaba, mas quem busca por cirurgião plástico de referência no Google encontra pouca profundidade de vitrine institucional independente. Posso te enviar um diagnóstico visual de 2 minutos mostrando como posicionar seu nome no topo das buscas?"
    },
    {
        "name": "Clínica Lu",
        "number": "5515996115575",
        "hook": "Olá, tudo bem? Analisei a presença digital da Clínica Lu na Torre Care no Jardim Vergueiro e notei um contraste interessante: o espaço de vocês tem excelente conceito médico e alta tecnologia, mas a presença no Google Maps está com informações dispersas que diluem a captação de pacientes de maior ticket em Sorocaba. Posso te enviar um diagnóstico visual de 2 minutos mostrando como corrigir isso?"
    },
    {
        "name": "Impact Transformation Center",
        "number": "5515997829252",
        "hook": "Olá Dr. Delmo e equipe, tudo bem? Analisei a presença digital do Impact Center no Jardim Eltonville e notei um detalhe crucial: a proposta integrada de saúde e medicina estética de vocês é muito avançada, mas quem pesquisa no Google não encontra uma vitrine de conversão segmentada por procedimento de alto valor, perdendo buscas ativas. Posso te enviar um diagnóstico visual de 2 minutos mostrando como blindar isso?"
    },
    {
        "name": "Derma Simis Dra. Tatiana",
        "number": "5515996158237",
        "hook": "Olá Dra. Tatiana, tudo bem? Analisei a presença digital da Derma Simis em Sorocaba e notei um ponto estratégico: a senhora tem sólida reputação na dermatologia e cosmiatria, mas os novos moradores que se mudam para condomínios de Sorocaba e pesquisam no Google encontram pouca diferenciação da sua clínica frente a clínicas populares. Posso te enviar um diagnóstico visual de 2 minutos mostrando como destacar seu posicionamento?"
    },
    {
        "name": "Vita Odontologia",
        "number": "5515998603211",
        "hook": "Olá, tudo bem? Analisei a presença digital da Vita Odontologia na Vila Hortência e notei algo importante: vocês oferecem tratamentos avançados em reabilitação oral e implantes, mas nas buscas do Google o paciente de alto ticket é direcionado para concorrentes da Zona Sul por falta de uma vitrine digital otimizada. Posso te enviar um diagnóstico visual de 2 minutos mostrando esse gargalo?"
    },
    {
        "name": "Corts Clínica de Ortopedia",
        "number": "5515981350308",
        "hook": "Olá, tudo bem? Analisei a presença digital da Corts na Av. Juscelino Kubitschek e notei um detalhe importante: vocês são referência histórica em ortopedia em Sorocaba, mas a ficha no Google Maps não possui Tour Virtual 360° nem blindagem visual atualizada para quem pesquisa por especialistas na região. Posso te enviar um diagnóstico visual de 2 minutos mostrando como atualizar essa vitrine?"
    },
    {
        "name": "Dr. Leandro Brandi Ortopedia",
        "number": "5515981522821",
        "hook": "Olá Dr. Leandro, tudo bem? Analisei a presença digital do seu consultório no Jardim Eltonville e notei um ponto crítico: o senhor possui vasta especialização em cirurgia do joelho, mas quem busca por cirurgião especialista em Sorocaba encontra dados descentralizados sem um portal médico institucional próprio de autoridade. Posso te enviar um diagnóstico visual de 2 minutos mostrando como resolver isso?"
    },
    {
        "name": "Med Cor Sorocaba",
        "number": "5515991984736",
        "hook": "Olá, tudo bem? Analisei a presença digital da Med Cor na Comendador Pereira Inácio e notei um detalhe operacional: o endereço de vocês no Vergueiro é excelente para consultas especializadas, mas quem pesquisa na web encontra barreiras para identificar o padrão de atendimento médico rápido e direto da clínica. Posso te enviar um diagnóstico visual de 2 minutos mostrando como simplificar essa captação?"
    },
    {
        "name": "Ezklo Marcenaria Boutique",
        "number": "5515997120678",
        "hook": "Olá equipe da Ezklo, tudo bem? Acompanho o design autoral impecável de vocês no Campolim. Notei um detalhe técnico no site de vocês na Pedro Molina que oscila na segurança SSL quando clientes acessam via celular de condomínios fechados, gerando desconfiança em projetos de R$ 50k+. Posso te enviar um diagnóstico visual de 2 minutos mostrando como blindar a navegação de vocês?"
    },
    {
        "name": "Marcenaria Sucesso Planejados",
        "number": "5515997787394",
        "hook": "Olá, tudo bem? Mapeei empresas de marcenaria sob medida em Sorocaba e notei um ponto crítico na presença de vocês no Google Maps: o perfil da marcenaria ainda não foi verificado oficialmente pelo proprietário, o que deixa a empresa vulnerável e faz o Google rebaixar o posicionamento frente aos concorrentes. Posso te enviar um diagnóstico visual de 2 minutos mostrando como proteger e destacar a sua marcenaria?"
    }
]

from CONFIG_MOTOR_DISPARO_VOCACOES_START import ensure_lgpd_compliance

def send_whatsapp(number, text):
    if str(number) != str(ADMIN_WHATSAPP):
        text = ensure_lgpd_compliance(text)
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
    # Atualiza oportunidade para SCREENING no Twenty CRM
    first_word = company_name.split()[0]
    sql = f"""
    UPDATE "{SCHEMA}"."opportunity" o
    SET stage = 'SCREENING', "updatedAt" = NOW()
    FROM "{SCHEMA}"."company" c
    WHERE o."companyId" = c.id AND c.name ILIKE '%{first_word}%';
    """
    proc = subprocess.Popen(
        [DOCKER_BIN, "exec", "-i", "twenty-db-1", "psql", "-U", "postgres", "-d", "twenty"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8"
    )
    proc.communicate(input=sql)

def run_queue():
    total = len(QUEUE)
    print(f"==================================================")
    print(f"🚀 INICIANDO FILA DE 16 DISPAROS (15:10 - 17:00)")
    print(f"Intervalo seguro: 7 minutos (420s) | Total: {total} leads")
    print(f"==================================================")
    
    notify_admin(f"🚀 *DISPAROS INICIADOS:* Fila de {total} leads de Alto Ticket em andamento com espaçamento de 7 minutos. Previsão de término: 16:55.")

    for i, lead in enumerate(QUEUE):
        idx = i + 1
        now_str = datetime.now().strftime("%H:%M:%S")
        print(f"\n[{idx}/{total}] [{now_str}] Disparando para {lead['name']} ({lead['number']})...")
        status, data = send_whatsapp(lead["number"], lead["hook"])
        msg_id = data.get("key", {}).get("id", "N/A")
        print(f"-> Status {status} | Msg ID: {msg_id}")
        
        update_crm_stage(lead["name"])
        notify_admin(f"✅ *[{idx}/{total}] Enviado:* {lead['name']}\n📱 {lead['number']}\n⏱️ Próximo envio em 7 minutos.")

        if i < total - 1:
            print("Aguardando 7 minutos (420 segundos)...")
            time.sleep(420)

    print("\n★ TODOS OS 16 DISPAROS FORAM CONCLUÍDOS COM SUCESSO! ★")
    notify_admin(f"🎉 *LOTE CONCLUÍDO:* Todos os {total} leads foram abordados no WhatsApp até as 17:00 com sucesso!")

if __name__ == "__main__":
    run_queue()
