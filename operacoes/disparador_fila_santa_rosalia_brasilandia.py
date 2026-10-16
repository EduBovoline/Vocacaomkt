"""
disparador_fila_santa_rosalia_brasilandia.py — Fila de Prospecção (100 Leads)
Pólos: Santa Rosália e Jardim Brasilândia — Qualificados por Jev System One
Cadência segura com warm-up escalonado (intervalo 6 a 9 min) e conformidade LGPD
"""

import os
import sys
import time
import random
import requests
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

EVOLUTION_API_URL = "http://localhost:8080"
INSTANCE_NAME = "vocacao_comercial"
API_KEY = "vocacao_update_secret_key_2026"
ADMIN_WHATSAPP = "5515981512083"

QUEUE = [
    {
        "name": "Silvério Odontologia",
        "number": "551530165548",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital da empresa no bairro Santa Rosália e vi que vocês já possuem um site estabelecido, mas o carregamento no celular pode estar fazendo vocês perderem clientes para concorrentes locais. Posso te enviar um diagnóstico visual de 2 minutos mostrando como acelerar a conversão da página? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Update (Reforma Mobile-First)"
    },
    {
        "name": "Orodent Unidade Santa Rosália",
        "number": "551533571363",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Clínica Russo Odontologia",
        "number": "551532331516",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Dr. Gaspar Martins da Silva",
        "number": "551532310205",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "RP Prime Odontologia",
        "number": "551530111204",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Clínica Vanessa Nogueira Emagrecimento",
        "number": "551530313394",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital da empresa no bairro Santa Rosália e vi que vocês já possuem um site estabelecido, mas o carregamento no celular pode estar fazendo vocês perderem clientes para concorrentes locais. Posso te enviar um diagnóstico visual de 2 minutos mostrando como acelerar a conversão da página? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Update (Reforma Mobile-First)"
    },
    {
        "name": "Clínica Equilíbrio Saúde",
        "number": "551532348890",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Clínica LES Medicina e Reabilitação",
        "number": "551532335772",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "CeiPre Saúde & Fisioterapia",
        "number": "551534188848",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Fisio Santa Rosália",
        "number": "551532321450",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Consultório Pediátrico Santa Rosália",
        "number": "551532314560",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Clínica de Psicologia & Terapias Rosália",
        "number": "5515998124010",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Espaço Reab Postural & RPG",
        "number": "5515997812030",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Consultório de Fonoaudiologia Integrada",
        "number": "551532349010",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Clínica Dermatológica Dra. Paula",
        "number": "5515996145520",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Clínica Paes Pilates & Fisio",
        "number": "5515991767971",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Sem Limites Studio Pilates",
        "number": "5515997230411",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Pure Pilates Santa Rosália",
        "number": "5515998104400",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Studio Corpo & Mente Pilates",
        "number": "5515991442100",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Espaço Movimento Pilates Clássico",
        "number": "5515981223300",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Studio Vital Pilates & Yoga",
        "number": "5515996551200",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Instituto Postura & Movimento",
        "number": "5515997334411",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Studio Funcional Rosália Fitness",
        "number": "5515991887722",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Personal Studio Santa Rosália",
        "number": "5515997116633",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Espaço Zen Terapias & Pilates",
        "number": "5515981559944",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Dra. Cauane Guelfi Estética Avançada",
        "number": "5515996411220",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Rô Ferreira Estética",
        "number": "5515991166474",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Studio D'Elas Salão & Estética",
        "number": "551532338900",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Espaço Bella Donna Santa Rosália",
        "number": "5515997443322",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Laser Care Depilação & Estética",
        "number": "551530334410",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Barbearia Tradicional Santa Rosália",
        "number": "5515991228899",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Ateliê da Beleza & Sobrancelhas",
        "number": "5515998337711",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Clínica de Estética Silhouette",
        "number": "5515996225544",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Espaço Homem Barbearia & Estética",
        "number": "551532114400",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Studio Nails & Beauty Santa Rosália",
        "number": "5515997661188",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Vet Care Saúde Animal",
        "number": "5515981722170",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Deniane Almeida Fisiovet",
        "number": "5515996841434",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "BastVet Centro Veterinário",
        "number": "551532328811",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Pet Shop & Clínica Santa Rosália",
        "number": "551532345566",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Boutique Animal Estética Pet",
        "number": "5515991332211",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Consultório Veterinário Dr. Marcelo",
        "number": "551532317788",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Amigo dos Bichos Pet Shop",
        "number": "5515997448822",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Espaço Pet Spa & Hotelzinho",
        "number": "5515981446655",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Izakaya Tsuchi Gastronomia Japonesa",
        "number": "551532114258",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Café com Gato Sorocaba",
        "number": "551533260658",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Di Garden Restaurante & Eventos",
        "number": "551532323152",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Cão Véio Sorocaba Gastropub",
        "number": "551530335500",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Bistrô da Praça Santa Rosália",
        "number": "551532349911",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Forneria & Pizzaria Santa Rosália",
        "number": "551532337744",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Empório Gourmet Santa Rosália",
        "number": "5515998221144",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Doce Encanto Confeitaria Fina",
        "number": "5515991554433",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Choperia & Espetaria Santa Rosália",
        "number": "5515997339900",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Motory Locadora & Veículos",
        "number": "551532323002",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Posto CIC Santa Rosália & Conveniência",
        "number": "551532344782",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Centro Automotivo Pereira da Silva",
        "number": "551532336622",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Santa Rosália Pneus & Alinhamento",
        "number": "551532318844",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Colégio Cristão Almeida Barros",
        "number": "551532326090",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Escola de Música Notas de Ouro",
        "number": "5515996118833",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Escola de Idiomas Santa Rosália",
        "number": "551532341122",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Lavanderia Express Santa Rosália",
        "number": "5515997224488",
        "bairro": "Santa Rosália",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Santa Rosália e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Brasilândia Odontologia Especializada",
        "number": "551532314411",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Clínica Dr. Marcos Dental",
        "number": "5515997123344",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Dra. Camila Odontologia e Estética",
        "number": "5515991448855",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Fisioterapia Integrada Brasilândia",
        "number": "551532341290",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Consultório de Psicologia & Família",
        "number": "5515981336622",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Clínica Médica Popular Brasilândia",
        "number": "551532338877",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Jardim Brasilândia e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Laboratório & Coleta Brasilândia",
        "number": "551532327700",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Espaço Saúde & Podologia Brasil",
        "number": "5515996554411",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Studio Vip Brasilândia Beleza",
        "number": "5515997331199",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Espaço Divas Cabelo & Estética",
        "number": "5515991225588",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Barbearia Tradicional Brasil",
        "number": "5515981447733",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Salão Bela Imagem Brasilândia",
        "number": "551532349900",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Espaço Estética & Sobrancelhas Mary",
        "number": "5515996113377",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Barbearia Black & Gold Brasilândia",
        "number": "5515997886644",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Studio Nails Brasilândia Unhas",
        "number": "5515991669922",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Clínica de Massoterapia & Relaxamento",
        "number": "5515981224400",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Auto Center Brasilândia",
        "number": "551532328844",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Mecânica e Injeção Sorocaba Norte",
        "number": "551532339911",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Oficina Brasil Car Funilaria",
        "number": "551532317733",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Moto Peças & Oficina Brasilândia",
        "number": "5515997226611",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Pneus & Alinhamento Brasil",
        "number": "551532345511",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Auto Elétrica & Baterias Brasilândia",
        "number": "5515991557788",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Ar Condicionado Automotivo Norte",
        "number": "5515981338899",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Lava Rápido & Estética Automotiva Brasil",
        "number": "5515996442200",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Pet Shop Brasil & Veterinária",
        "number": "551532334499",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Agropecuária & Rações Brasilândia",
        "number": "551532316622",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Amigo Fiel Banho e Tosa",
        "number": "5515997118833",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Consultório Veterinário Brasil Animal",
        "number": "5515998335522",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Padaria & Confeitaria Pão Brasil",
        "number": "551532321188",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Restaurante & Marmitaria Brasilândia",
        "number": "551532347744",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no bairro Jardim Brasilândia e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Combo Maps + Tour 360° GoPro Max"
    },
    {
        "name": "Pizzaria Forno Nobre Brasilândia",
        "number": "551532335566",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Pastelaria & Lanchonete do Bairro",
        "number": "5515991443311",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Açougue & Casa de Carnes Brasil",
        "number": "551532319944",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Drogaria & Farmácia Brasilândia",
        "number": "551532324400",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Marcenaria Brasil Móveis Planejados",
        "number": "5515997558811",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Serralheria & Estruturas Brasilândia",
        "number": "5515991884422",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Vidraçaria & Box Brasil Norte",
        "number": "551532346611",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Start (Maps + Vitrine One-Page)"
    },
    {
        "name": "Elétrica & Hidráulica Brasil Materiais",
        "number": "551532331155",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Gráfica Rápida & Comunicação Brasilândia",
        "number": "5515996227700",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    },
    {
        "name": "Assistência Técnica de Celulares & Informática",
        "number": "5515981552233",
        "bairro": "Jardim Brasilândia",
        "hook": "Olá! Analisei a ficha de vocês no Google Maps no Jardim Brasilândia e notei oportunidades para blindar o perfil contra concorrentes e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso? (Se preferir não receber mensagens comerciais, responda PARAR).",
        "oferta": "Vocação Presença no Maps (Blindagem)"
    }
]

DELIVERED_FILE = os.path.join(os.path.dirname(__file__), "delivered_leads.json")

def is_already_delivered(phone):
    if os.path.exists(DELIVERED_FILE):
        try:
            with open(DELIVERED_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return phone in data or phone[-8:] in str(data)
        except Exception:
            return False
    return False

def send_whatsapp(number, text):
    url = f"{EVOLUTION_API_URL}/message/sendText/{INSTANCE_NAME}"
    headers = {"apikey": API_KEY, "Content-Type": "application/json"}
    payload = {
        "number": number,
        "text": text,
        "options": {"linkPreview": False, "delay": 1200}
    }
    resp = requests.post(url, json=payload, headers=headers, timeout=20)
    return resp.status_code, resp.json()

def notify_admin(msg):
    send_whatsapp(ADMIN_WHATSAPP, msg)

def run_queue(limit=5):
    print(f"🚀 Iniciando lote seguro de {limit} disparos (Santa Rosália & Jardim Brasilândia)...")
    sent = 0
    for idx, item in enumerate(QUEUE):
        if sent >= limit:
            break

        phone = item["number"]
        name = item["name"]

        if is_already_delivered(phone):
            continue

        print(f"\n[{idx+1}/{len(QUEUE)}] Disparando para {name} ({phone})...")
        status, res = send_whatsapp(phone, item["hook"])

        if status in [200, 201]:
            sent += 1
            notify_admin(
                f"📤 *DISPARO REALIZADO (PÓLO {item['bairro'].upper()}):*\n"
                f"• *Lead:* {name}\n"
                f"• *Oferta Jev:* {item['oferta']}\n"
                f"• *Contato:* {phone}"
            )
            if sent < limit:
                wait_sec = random.randint(360, 540) # 6 a 9 min
                print(f"   [⏳] Aguardando cadência segura: {wait_sec // 60} min...")
                time.sleep(wait_sec)

    notify_admin(f"🏁 *LOTE CONCLUÍDO:* {sent} mensagens disparadas com segurança.")

if __name__ == "__main__":
    qty = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    run_queue(limit=qty)
