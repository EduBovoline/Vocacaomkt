"""
disparador_fila_20leads_pilates.py — Fila de Prospecção de 20 Leads de Pilates, Terapias e Treino
Vocação Comunicação & Marketing
"""

import os
import sys
import time
import random
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
        "name": "Revitae Pilates e Fisioterapia",
        "number": "5515992733623",
        "hook": "Olá, tudo bem? Analisei a presença digital da Revitae no Jardim Faculdade e notei um detalhe estratégico: a metodologia e os aparelhos de vocês são impecáveis, mas quem pesquisa por studio de pilates premium em Sorocaba no Google encontra pouca diferenciação visual sem um Tour Virtual 360° do espaço no Street View. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o studio nas buscas?"
    },
    {
        "name": "Microvita Pilates Sorocaba",
        "number": "5515998070877",
        "hook": "Olá, tudo bem? Analisei a presença digital da Microvita no Jardim Emília e notei algo importante: o studio tem excelente conceito de cuidado individualizado, mas nas buscas do Google novos moradores de condomínios da região acabam caindo em academias convencionais por falta de uma vitrine digital de autoridade focada no Pilates. Posso te enviar um diagnóstico visual de 2 minutos mostrando esse gargalo?"
    },
    {
        "name": "SUB. Studio de Pilates",
        "number": "5515997153583",
        "hook": "Olá, tudo bem? Analisei a presença digital do SUB. Studio no Campolim e notei um ponto crítico: vocês estão no bairro mais nobre da cidade com uma proposta moderna, mas quem pesquisa no Google encontra informações dispersas sem um Tour 360° imersivo que comprove a sofisticação da estrutura antes do agendamento. Posso te enviar um diagnóstico visual de 2 minutos mostrando como corrigir isso?"
    },
    {
        "name": "Inspirevida Fisioterapia e Pilates",
        "number": "5515998104597",
        "hook": "Olá, tudo bem? Analisei a presença digital da Inspirevida no Campolim e notei um detalhe crucial: vocês combinam fisioterapia e pilates clínico de alto nível, mas quem pesquisa na web por reabilitação de coluna cai em perfis genéricos de redes sociais em vez de um portal de autoridade médica e postural. Posso te enviar um diagnóstico visual de 2 minutos mostrando como blindar a sua captação?"
    },
    {
        "name": "Instituto Krion Fisioterapia e Pilates",
        "number": "5515996270927",
        "hook": "Olá, tudo bem? Analisei a presença digital do Instituto Krion na Mario Campolim e notei um contraste interessante: a autoridade de vocês em alta performance e reabilitação é reconhecida, mas o perfil no Google Maps está subaproveitado para atrair pacientes particulares de maior ticket da Zona Sul. Posso te enviar um diagnóstico visual de 2 minutos mostrando como destravar essa busca ativa?"
    },
    {
        "name": "Karina Fiel Fisioterapia e Pilates",
        "number": "5515981158086",
        "hook": "Olá Dra. Karina, tudo bem? Analisei a presença digital do seu espaço no Campolim e notei algo estratégico: a senhora oferece tratamentos refinados em RPG, osteopatia e pilates clínico, mas pacientes de condomínios que pesquisam no Google encontram pouca profundidade de vitrine independente de autoridade. Posso te enviar um diagnóstico visual de 2 minutos mostrando como estruturar isso?"
    },
    {
        "name": "Dr. João Gabriel Quiropraxia",
        "number": "5515997935990",
        "hook": "Olá Dr. João Gabriel, tudo bem? Analisei a presença digital do seu consultório na Mario Campolim e notei um ponto importante: a quiropraxia e reabilitação articular têm enorme demanda em Sorocaba, mas quem busca por especialista em coluna no Google encontra barreiras para conhecer o seu trabalho por falta de um portal próprio de autoridade. Posso te enviar um diagnóstico visual de 2 minutos mostrando como resolver isso?"
    },
    {
        "name": "Vivá Terapias Integrativas",
        "number": "5515998161692",
        "hook": "Olá, tudo bem? Analisei a presença digital da Vivá em Sorocaba e notei um detalhe relevante: a abordagem integrativa e ortomolecular de vocês atrai um público qualificado, mas a presença nas buscas locais do Google ainda não reflete o posicionamento premium da clínica. Posso te enviar um diagnóstico visual de 2 minutos mostrando como destacar o espaço de vocês?"
    },
    {
        "name": "Giancarlo Marçal Osteopatia",
        "number": "5515991176788",
        "hook": "Olá Dr. Giancarlo, tudo bem? Analisei sua presença digital em Sorocaba e notei uma oportunidade clara: a osteopatia e a quiropraxia têm alto valor agregado, mas novos moradores da cidade que pesquisam no Google por alívio rápido de dores acabam caindo em clínicas generalistas por falta de uma vitrine clínica de autoridade. Posso te enviar um diagnóstico visual de 2 minutos sobre isso?"
    },
    {
        "name": "Prof. Dr. Danilo Armbrust",
        "number": "5515991051888",
        "hook": "Olá Dr. Danilo, tudo bem? Analisei sua autoridade acadêmica e clínica em osteopatia e quiropraxia em Sorocaba. O senhor tem grande renome profissional, mas quem pesquisa pelo seu atendimento no Google não encontra uma vitrine digital médica dedicada que centralize os agendamentos particulares. Posso te enviar um diagnóstico visual de 2 minutos mostrando como alinhar essa presença?"
    },
    {
        "name": "Quiro&Cia Centro de Quiropraxia",
        "number": "5515981778421",
        "hook": "Olá equipe da Quiro&Cia, tudo bem? Analisei a presença digital do centro de vocês em Sorocaba e notei um ponto estratégico: o espaço é especializado na coluna vertebral, mas a ficha no Google Maps não conta com Tour Virtual 360° nem integração ágil com vitrine mobile de agendamento. Posso te enviar um diagnóstico visual de 2 minutos mostrando como blindar a sua captação?"
    },
    {
        "name": "Amalio Júnior Quiropraxia",
        "number": "5515991483785",
        "hook": "Olá Dr. Amalio, tudo bem? Analisei a presença digital do seu consultório de quiropraxia em Sorocaba e notei algo importante: seu trabalho postural é excelente, mas quem busca por alinhamento e alívio de dores no Google encontra dados dispersos sem uma página profissional de apresentação. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o seu atendimento?"
    },
    {
        "name": "Pure Pilates Campolim",
        "number": "5515997760345",
        "hook": "Olá, tudo bem? Analisei a presença digital da unidade Pure Pilates no Campolim e notei um detalhe operacional: a marca tem grande força nacional, mas na busca local do Google pacientes de Sorocaba hesitam quando não encontram fotos panorâmicas do studio e um canal direto com os instrutores da unidade local. Posso te enviar um diagnóstico visual de 2 minutos mostrando como resolver isso?"
    },
    {
        "name": "Classic Pilates e Fisioterapia",
        "number": "5515991315847",
        "hook": "Olá, tudo bem? Analisei a presença digital da Classic Pilates no Central Parque e notei um ponto de melhoria: o espaço tem tradição e ótimo atendimento, mas nas buscas do Google da região oeste a visibilidade do studio fica rebaixada em relação a academias que anunciam online. Posso te enviar um diagnóstico visual de 2 minutos mostrando como posicionar seu studio no topo?"
    },
    {
        "name": "Flávia Fernandes Pilates Studio",
        "number": "5515988119242",
        "hook": "Olá Flávia, tudo bem? Analisei a presença digital do seu studio na Vila Jardini e notei um ponto estratégico: o ambiente é muito acolhedor e técnico, mas quem pesquisa por pilates no bairro não encontra uma vitrine digital com Tour 360° no Street View, perdendo novos alunos de condomínios da ZS. Posso te enviar um diagnóstico visual de 2 minutos mostrando como blindar seu espaço?"
    },
    {
        "name": "Pilates Mova-se",
        "number": "5515997539318",
        "hook": "Olá equipe Mova-se, tudo bem? Analisei a presença digital do studio de vocês na Vila Carvalho e notei algo importante: a proposta de movimento consciente é incrível, mas na web os novos moradores de Sorocaba encontram pouca informação sobre os planos e benefícios antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como simplificar essa conversão?"
    },
    {
        "name": "Vida Mais Pilates Clássico",
        "number": "5515981140366",
        "hook": "Olá, tudo bem? Analisei a presença digital do Vida Mais Pilates na Boa Vista e notei um ponto relevante: o método clássico é um grande diferencial competitivo, mas quem pesquisa por studios tradicionais no Google não encontra uma vitrine de autoridade que destaque esse padrão frente aos concorrentes comuns. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar sua marca?"
    },
    {
        "name": "Pilates Mamy Baby",
        "number": "5515998049147",
        "hook": "Olá, tudo bem? Analisei a presença digital do Pilates Mamy Baby em Sorocaba e achei o nicho de gestantes e mães extraordinário. Porém, quem pesquisa por pilates gestacional no Google encontra pouca facilidade para entender o método e agendar uma aula experimental de forma imediata. Posso te enviar um diagnóstico visual de 2 minutos mostrando como potencializar essa captação?"
    },
    {
        "name": "Francisco Furio Treinamento Funcional",
        "number": "5515991492719",
        "hook": "Olá Francisco, tudo bem? Analisei seu trabalho de treinamento funcional e personal em Sorocaba e notei um ponto estratégico: você tem excelente entrega técnica, mas quem busca por consultoria personalizada de alto ticket no Google encontra canais dispersos sem uma vitrine oficial com cases e depoimentos em vídeo. Posso te enviar um diagnóstico visual de 2 minutos mostrando como estruturar isso?"
    },
    {
        "name": "Mundo Acqua Studio",
        "number": "5515992529514",
        "hook": "Olá equipe Mundo Acqua, tudo bem? Analisei a presença digital do studio de vocês no Jardim Simus e notei um detalhe crucial: a proposta de treinamento personalizado e emagrecimento é muito forte, mas a captação no Google Maps pode ser triplicada com um Tour Virtual 360° e uma vitrine digital otimizada para quem pesquisa no celular. Posso te enviar um diagnóstico visual de 2 minutos mostrando como corrigir isso?"
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

def run_queue(min_interval=300, max_interval=420):
    total = len(QUEUE)
    print(f"==================================================")
    print(f"🚀 INICIANDO FILA DE 20 LEADS — PILATES & TERAPIAS")
    print(f"Intervalo dinâmico anti-ban: {min_interval//60} a {max_interval//60} min (variável a cada lead) | Total: {total} leads")
    print(f"==================================================")
    
    notify_admin(f"🚀 *DISPAROS INICIADOS:* Fila de {total} leads de Pilates & Terapias em andamento com intervalo variável de {min_interval//60} a {max_interval//60} minutos para proteção contra padrões.")

    for i, lead in enumerate(QUEUE):
        idx = i + 1
        now_str = datetime.now().strftime("%H:%M:%S")
        print(f"\n[{idx}/{total}] [{now_str}] Disparando para {lead['name']} ({lead['number']})...")
        status, data = send_whatsapp(lead["number"], lead["hook"])
        msg_id = data.get("key", {}).get("id", "N/A")
        print(f"-> Status {status} | Msg ID: {msg_id}")
        
        update_crm_stage(lead["name"])

        if i < total - 1:
            sleep_seconds = random.randint(min_interval, max_interval)
            sleep_min = round(sleep_seconds / 60, 1)
            notify_admin(f"✅ *[{idx}/{total}] Enviado:* {lead['name']}\n📱 {lead['number']}\n⏱️ Próximo envio aleatório em {sleep_min} min ({sleep_seconds}s).")
            print(f"Aguardando jitter anti-ban: {sleep_min} min ({sleep_seconds}s)...")
            time.sleep(sleep_seconds)
        else:
            notify_admin(f"✅ *[{idx}/{total}] Enviado:* {lead['name']}\n📱 {lead['number']}\n🏁 Fim da fila!")

    print("\n★ TODOS OS 20 DISPAROS FORAM CONCLUÍDOS COM SUCESSO! ★")
    notify_admin(f"🎉 *LOTE CONCLUÍDO:* Todos os {total} leads de Pilates e Terapias foram abordados no WhatsApp com sucesso!")

if __name__ == "__main__":
    min_i = 300
    max_i = 420
    if len(sys.argv) > 2 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
        min_i = int(sys.argv[1])
        max_i = int(sys.argv[2])
    run_queue(min_i, max_i)
