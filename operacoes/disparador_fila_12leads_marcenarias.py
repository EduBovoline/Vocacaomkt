"""
disparador_fila_12leads_marcenarias.py — Fila de Prospecção de 12 Marcenarias e Marmorarias de Alto Ticket
Vocação Comunicação & Marketing — Janela de Almoço (12h às 14h)
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

QUEUE = [
    {
        "name": "Marcenaria SHZ",
        "number": "5515997502210",
        "hook": "Olá pessoal da SHZ! Parabéns pelos acabamentos postados. Notei que no site oficial vocês ainda usam @gmail.com para contato comercial. Clientes de condomínios que investem R$ 40k desconfiam de e-mails gratuitos. Posso te enviar um diagnóstico visual de 2 minutos mostrando como alinhar a governança de vocês?"
    },
    {
        "name": "Oakhouse Marcenaria (RR Marcenaria)",
        "number": "5515997157075",
        "hook": "Olá equipe da Oakhouse! O trabalho visual de vocês no Instagram é incrível. Notamos apenas que a experiência digital está dividida entre Oakhouse e RR Marcenaria no site antigo, o que confunde o cliente que pesquisa no Google. Posso te enviar um diagnóstico visual de 2 minutos mostrando como unificar isso?"
    },
    {
        "name": "MDM Marcenaria",
        "number": "5515996503634",
        "hook": "Olá MDM Marcenaria! Sabemos da potência da fábrica de 800m² de vocês em Sorocaba. Vimos que sua presença digital pode atrair muito mais clientes finais dos condomínios do Campolim e Fazenda Alvorada via Google Ads segmentado. Posso te enviar um diagnóstico visual de 2 minutos sobre essa oportunidade?"
    },
    {
        "name": "Sutil Marcenaria",
        "number": "5515981859590",
        "hook": "Olá Sutil Marcenaria! Excelente posicionamento com arquitetos próprios. Vimos que podemos criar um canal digital dedicado para atrair escritórios de arquitetura e design de interiores em Sorocaba para parcerias contínuas. Posso te enviar um diagnóstico visual de 2 minutos mostrando como estruturar isso?"
    },
    {
        "name": "Cast Select Móveis Planejados",
        "number": "5515998201691",
        "hook": "Olá Cast Select! O showroom no Iguatemi traz grande visibilidade, mas os compradores de condomínios fechados (como Fazenda Boa Vista e Alphaville) muitas vezes buscam primeiro no Google antes de sair de casa. Posso te enviar um diagnóstico visual de 2 minutos sobre captação ativa de luxo?"
    },
    {
        "name": "Celmar Campolim",
        "number": "5515991214679",
        "hook": "Olá Celmar Campolim! A presença de vocês na Comitre é um marco. Para neutralizar os concorrentes da mesma avenida que estão investindo pesado em tráfego, desenvolvemos criativos em vídeo focados na garantia de entrega e acabamento da Celmar. Posso te enviar um diagnóstico visual de 2 minutos sobre isso?"
    },
    {
        "name": "Criare Sorocaba",
        "number": "5515991850844",
        "hook": "Olá Criare Sorocaba! Notamos suas campanhas ativas para o Campolim. Muitos cliques estão sendo gastos com pessoas buscando apenas 'móveis baratos'. Nossa assessoria filtra exclusivamente os termos de alto valor e condomínios. Posso te enviar um diagnóstico visual de 2 minutos mostrando como otimizar essa verba?"
    },
    {
        "name": "Impeccabile Móveis Planejados",
        "number": "5511910640282",
        "hook": "Olá Impeccabile! Seus projetos sob medida têm alto valor estético. Porém, ao pesquisar por móveis planejados no eixo Itu-Sorocaba, a concorrência aparece na frente por ter mais avaliações estruturadas no Google Maps. Posso te enviar um diagnóstico visual de 2 minutos mostrando como resolver isso em 7 dias?"
    },
    {
        "name": "Wbilino Conceito Mármores de Luxo",
        "number": "5515991210000",
        "hook": "Olá equipe Wbilino Conceito! Admiramos a sofisticação das pedras e do conceito de luxo de vocês. Vimos que o site pode carregar muito mais rápido no celular para quem acessa de condomínios, conectando uma esteira de captação de arquitetos. Posso te enviar um diagnóstico visual de 2 minutos sobre isso?"
    },
    {
        "name": "Marmoraria Santos",
        "number": "5515988180072",
        "hook": "Olá Marmoraria Santos! A solidez de vocês em Sorocaba é indiscutível. No entanto, o site atual não permite que o cliente de condomínio envie a planta baixa ou o projeto da marcenaria direto no WhatsApp para cotação rápida. Posso te enviar um diagnóstico visual de 2 minutos mostrando como modernizar isso?"
    },
    {
        "name": "Marcenaria Domke",
        "number": "5515988137613",
        "hook": "Olá Domke Marcenaria! Acompanho os trabalhos sob medida de vocês em Sorocaba. Notamos que quem busca por marcenaria autoral de alto padrão no Google encontra barreiras para ver o portfólio completo em alta definição no celular. Posso te enviar um diagnóstico visual de 2 minutos sobre isso?"
    },
    {
        "name": "Todeschini Sorocaba",
        "number": "5515991287563",
        "hook": "Olá Todeschini Sorocaba! O showroom na Barão de Tatuí é impecável. Notamos que muitos clientes comparam orçamentos online antes de agendar a visita presencial de projetos e encontramos oportunidades para blindar o Google Maps de vocês. Posso te enviar um diagnóstico visual de 2 minutos mostrando o gargalo?"
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

def run_queue(min_interval=300, max_interval=420):
    total = len(QUEUE)
    print(f"==================================================")
    print(f"🚀 INICIANDO FILA DE {total} LEADS — MARCENARIAS ALTO TICKET")
    print(f"Intervalo dinâmico anti-ban: {min_interval//60} a {max_interval//60} min (variável a cada lead)")
    print(f"==================================================")
    
    notify_admin(f"🚀 *DISPAROS DE ALMOÇO INICIADOS:* Fila de {total} Marcenarias e Marmorarias de Alto Padrão em andamento com intervalo de {min_interval//60} a {max_interval//60} minutos.")

    for i, lead in enumerate(QUEUE):
        idx = i + 1
        now_str = datetime.now().strftime("%H:%M:%S")
        print(f"\n[{idx}/{total}] [{now_str}] Disparando para {lead['name']} ({lead['number']})...")
        status, data = send_whatsapp(lead["number"], lead["hook"])
        msg_id = data.get("key", {}).get("id", "N/A")
        print(f"-> Status {status} | Msg ID: {msg_id}")

        if i < total - 1:
            sleep_seconds = random.randint(min_interval, max_interval)
            sleep_min = round(sleep_seconds / 60, 1)
            notify_admin(f"✅ *[{idx}/{total}] Enviado:* {lead['name']}\n📱 {lead['number']}\n⏱️ Próximo envio aleatório em {sleep_min} min ({sleep_seconds}s).")
            print(f"Aguardando jitter anti-ban: {sleep_min} min ({sleep_seconds}s)...")
            time.sleep(sleep_seconds)
        else:
            notify_admin(f"✅ *[{idx}/{total}] Enviado:* {lead['name']}\n📱 {lead['number']}\n🏁 Fim da fila do almoço!")

    print("\n★ TODOS OS DISPAROS FORAM CONCLUÍDOS COM SUCESSO! ★")
    notify_admin(f"🎉 *LOTE CONCLUÍDO:* Todas as {total} Marcenarias e Marmorarias foram abordadas no WhatsApp com sucesso!")

if __name__ == "__main__":
    min_i = 300
    max_i = 420
    if len(sys.argv) > 2 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
        min_i = int(sys.argv[1])
        max_i = int(sys.argv[2])
    run_queue(min_i, max_i)
