"""
disparador_fila_15_curta.py
Disparador Oficial Vocação — 15 Leads (5 da pasta 3 Leads + 10 Novos de Santa Rosália)
Abordagem Curta, Direta e 100% Honesta (Sem bajulação, sem mentiras, sem 'faz sentido')
"""

import os
import sys
import time
import json
import random
import requests
from datetime import datetime

# P3 (auditoria): saída sempre em UTF-8, inclusive no console cp1252 do Windows.
import vocacao_seguranca  # noqa: F401  — o import já chama forcar_utf8()

EVOLUTION_API_URL = "http://localhost:8080"
INSTANCE_NAME     = "vocacao_comercial"
API_KEY           = "vocacao_update_secret_key_2026"
ADMIN_WHATSAPP    = "5515981512083"

BASE_DIR       = os.path.dirname(__file__)
DELIVERED_FILE = os.path.join(BASE_DIR, "delivered_leads.json")

QUEUE = [
    # 5 Leads da pasta 3 Leads (não contatados ainda)
    {
        "name": "Matt the Barber",
        "number": "5515991006264",
        "text": "Oi, tudo bem? Aqui é o Eduardo, de Sorocaba.\nVi a ficha de vocês no Google Maps no São Vicente da Lacerda e notei que o link do site está em HTTP simples, acusando página não segura.\nA gente monta vitrines próprias e rápidas para comércios daqui da cidade em 7 dias, sem mensalidade.\nPosso mandar um exemplo visual rápido por aqui para vocês verem?"
    },
    {
        "name": "Iara Artes",
        "number": "5515991082385",
        "text": "Oi, tudo bem? Aqui é o Eduardo, de Sorocaba.\nVi a ficha de vocês no Google Maps no Jardim Brasilândia e reparei que a foto principal é o portão fechado da rua, sem o catálogo dos kits de festa.\nA gente arruma a presença no Google Maps e monta catálogo rápido para quem trabalha com festas aqui na cidade.\nPosso te mandar um exemplo visual por aqui?"
    },
    {
        "name": "Damme Esmalteria Express JJ Lacerda",
        "number": "5515997627518",
        "text": "Oi, tudo bem? Aqui é o Eduardo, de Sorocaba.\nVi a ficha de vocês no Google Maps na JJ Lacerda e notei que o botão de site joga para o portal geral da rede em vez de abrir o WhatsApp da unidade de vocês.\nA gente organiza a ficha no Google para quem tem loja física aqui na cidade receber pedidos diretos no WhatsApp.\nPosso mandar um exemplo visual por aqui?"
    },
    {
        "name": "Studio Geisa Santos Spa & Nails",
        "number": "5515998196481",
        "text": "Oi, tudo bem? Aqui é o Eduardo, de Sorocaba.\nVi o perfil de vocês no Google Maps na Rua Júlio Ribeiro e notei que vocês ainda estão sem um site ou catálogo próprio cadastrado.\nA gente monta páginas rápidas para profissionais daqui da cidade em até 7 dias, sem mensalidade.\nPosso mandar um exemplo visual por aqui para você ver?"
    },
    {
        "name": "Di Piero Distribuidora",
        "number": "5515991517595",
        "text": "Oi, tudo bem? Aqui é o Eduardo, de Sorocaba.\nEstava pesquisando fornecedores de marmoraria na região e vi o site de vocês. Notei que a página atual é pesada no celular e a cotação é de 1 item por vez.\nA gente moderniza sites de distribuidoras aqui da cidade com cotação direta em lote no WhatsApp.\nPosso mandar um exemplo visual por aqui para vocês verem?"
    },
    # 10 Leads Novos de Santa Rosália (nunca contatados)
    {
        "name": "Clínica de Psicologia & Terapias Rosália",
        "number": "5515998124010",
        "text": "Oi, tudo bem? Aqui é o Eduardo, de Sorocaba.\nVi a clínica de vocês no Google Maps no Santa Rosália e notei que quem pesquisa pelos seus serviços encontra pouca informação institucional antes de chamar no WhatsApp.\nA gente monta páginas rápidas e profissionais para clínicas daqui da cidade em até 7 dias, sem mensalidade.\nPosso te mandar um exemplo visual rápido por aqui?"
    },
    {
        "name": "Espaço Reab Postural & RPG",
        "number": "5515997812030",
        "text": "Oi, tudo bem? Aqui é o Eduardo, de Sorocaba.\nVi a ficha de vocês no Google Maps na Av. Pereira da Silva e reparei que vocês não têm uma vitrine digital própria conectada ao perfil.\nA gente monta páginas rápidas para consultórios e estúdios daqui da cidade em até 7 dias, sem mensalidade.\nPosso te mandar um exemplo visual por aqui?"
    },
    {
        "name": "Clínica Paes Pilates & Fisio",
        "number": "5515991767971",
        "text": "Oi, tudo bem? Aqui é o Eduardo, de Sorocaba.\nEstava mapeando os estúdios de pilates do Santa Rosália e separei uma análise de 2 minutos sobre como quem procura aula no bairro encontra o seu espaço no Google Maps.\nA gente organiza a presença local e monta páginas rápidas para negócios daqui em até 7 dias.\nPosso te mandar o exemplo por aqui?"
    },
    {
        "name": "Sem Limites Studio Pilates",
        "number": "5515997230411",
        "text": "Oi, tudo bem? Aqui é o Eduardo, de Sorocaba.\nVi o perfil de vocês no Google Maps no Santa Rosália e reparei que vocês estão sem uma página própria apresentando os planos e horários.\nA gente monta páginas rápidas para estúdios daqui da cidade em até 7 dias, sem mensalidade.\nPosso te mandar um exemplo visual por aqui?"
    },
    {
        "name": "Pure Pilates Santa Rosália",
        "number": "5515998104400",
        "text": "Oi, tudo bem? Aqui é o Eduardo, de Sorocaba.\nMontei um retrato de como a sua unidade aparece na busca do Google Maps no Santa Rosália e onde o contato se perde entre a ficha e o WhatsApp.\nA gente organiza essa presença para comércios e estúdios daqui receberem contato direto.\nPosso te mandar a análise de 2 minutos por aqui?"
    },
    {
        "name": "Studio Corpo & Mente Pilates",
        "number": "5515991442100",
        "text": "Oi, tudo bem? Aqui é o Eduardo, de Sorocaba.\nVi a ficha de vocês no Google Maps no Santa Rosália e notei que vocês ainda não têm um site próprio com as turmas e modalidades.\nA gente monta páginas rápidas para estúdios daqui da cidade em até 7 dias, sem mensalidade.\nPosso te mandar um exemplo visual rápida por aqui?"
    },
    {
        "name": "Espaço Movimento Pilates Clássico",
        "number": "5515981223300",
        "text": "Oi, tudo bem? Aqui é o Eduardo, de Sorocaba.\nVi o estúdio de vocês no Google Maps no Santa Rosália e notei a ausência de uma vitrine web própria para apresentar os métodos e valores.\nA gente monta páginas rápidas para profissionais daqui da cidade em até 7 dias, sem mensalidade.\nPosso te mandar um exemplo visual por aqui?"
    },
    {
        "name": "Studio Vital Pilates & Yoga",
        "number": "5515996551200",
        "text": "Oi, tudo bem? Aqui é o Eduardo, de Sorocaba.\nVi a ficha de vocês no Google Maps no Santa Rosália e notei que vocês estão sem uma página própria apresentando as aulas e horários.\nA gente monta páginas rápidas para estúdios e espaços de bem-estar daqui da cidade em até 7 dias.\nPosso te mandar um exemplo visual por aqui?"
    },
    {
        "name": "Instituto Postura & Movimento",
        "number": "5515997334411",
        "text": "Oi, tudo bem? Aqui é o Eduardo, de Sorocaba.\nVi o espaço de vocês no Google Maps no Santa Rosália e notei que o perfil está sem uma vitrine própria cadastrada para quem pesquisa pelo bairro.\nA gente monta páginas rápidas para clínicas e profissionais daqui da cidade em até 7 dias, sem mensalidade.\nPosso te mandar um exemplo visual por aqui?"
    },
    {
        "name": "Espaço Zen Terapias & Pilates",
        "number": "5515981559944",
        "text": "Oi, tudo bem? Aqui é o Eduardo, de Sorocaba.\nVi a ficha de vocês no Google Maps no Santa Rosália e notei que vocês ainda não têm um site próprio com a grade de atendimentos e terapias.\nA gente monta páginas rápidas para espaços de saúde e bem-estar daqui da cidade em até 7 dias.\nPosso te mandar um exemplo visual por aqui?"
    }
]

def load_delivered():
    if os.path.exists(DELIVERED_FILE):
        try:
            with open(DELIVERED_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def mark_delivered(number, lead_name):
    delivered = load_delivered()
    delivered[number] = {
        "lead_name": lead_name,
        "delivered_at": datetime.now().isoformat()
    }
    with open(DELIVERED_FILE, "w", encoding="utf-8") as f:
        json.dump(delivered, f, indent=2, ensure_ascii=False)

def send_whatsapp(number, text):
    # P4 (auditoria): só celular válido, texto íntegro e dentro da Janela de Ouro.
    from vocacao_seguranca import pode_disparar_whatsapp

    _ok, _motivo = pode_disparar_whatsapp(
        number, text, verificar_janela=str(number) != str(ADMIN_WHATSAPP)
    )
    if not _ok:
        print(f"[SKIP] {number}: {_motivo}")
        return 0, {"erro": _motivo}

    url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
    headers = {"apikey": API_KEY, "Content-Type": "application/json"}
    payload = {
        "number": number,
        "text": text,
        "options": {"linkPreview": False, "delay": 1500}
    }
    resp = requests.post(url, json=payload, headers=headers, timeout=20)
    return resp.status_code, resp.text

def main():
    delivered = load_delivered()
    to_send = [item for item in QUEUE if item["number"] not in delivered]
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando Fila Curta e Direta Vocacao: {len(to_send)} disparos pendentes.")
    
    sent_count = 0
    for idx, item in enumerate(to_send, 1):
        num = item["number"]
        name = item["name"]
        text = item["text"]
        
        print(f"\n({idx}/{len(to_send)}) Enviando para: {name} ({num})...")
        try:
            status, resp = send_whatsapp(num, text)
            if status in (200, 201):
                mark_delivered(num, name)
                sent_count += 1
                print(f"  [OK] Entregue com sucesso! Status {status}")
            else:
                print(f"  [FALHA] Status {status}: {resp[:120]}")
        except Exception as e:
            print(f"  [ERRO] {e}")
        
        # Intervalo seguro humanizado entre mensagens (70 a 110 segundos) se houver próximo
        if idx < len(to_send):
            wait_sec = random.randint(70, 110)
            print(f"  [Intervalo de Seguranca] Aguardando {wait_sec}s antes do proximo lead...")
            time.sleep(wait_sec)

    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Fila concluida! Total enviados: {sent_count}/{len(to_send)}")
    # Notifica o admin
    try:
        send_whatsapp(ADMIN_WHATSAPP, f"🚀 [Vocação Disparo Concluído] Fila de {sent_count} leads curtos/honestos enviada com sucesso na Janela de Ouro!")
    except Exception:
        pass

if __name__ == "__main__":
    main()
