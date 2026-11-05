#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Notificação e Submissão Instantânea para IndexNow e Motores de IA
(Bing, Perplexity, Copilot, Seznam, Naver)
"""

import urllib.request
import json
import ssl
import sys

INDEXNOW_KEY = "b63a2948c2674e7bb414169dc20689fa"
HOST = "vocacao.digital"
KEY_LOCATION = f"https://{HOST}/{INDEXNOW_KEY}.txt"

URLS_TO_INDEX = [
    f"https://{HOST}/",
    f"https://{HOST}/vocacao-update.html",
    f"https://{HOST}/en/5-day-website-polish.html",
    f"https://{HOST}/llms.txt",
    f"https://{HOST}/llms-full.txt",
    f"https://{HOST}/portfolio.html",
    f"https://{HOST}/presenca-local.html",
]

def submit_indexnow():
    endpoint = "https://api.indexnow.org/indexnow"
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": URLS_TO_INDEX
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "Vocacao-Index-Engine/1.0"}
    )
    
    ctx = ssl.create_default_context()
    print(f"[*] Disparando submissao IndexNow para {len(URLS_TO_INDEX)} URLs...")
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
            status = res.getcode()
            print(f"[+] IndexNow respondeu com status {status} (200/202 = Sucesso!)")
    except urllib.error.HTTPError as e:
        print(f"[!] Resposta HTTP do IndexNow: {e.code} ({e.reason})")
    except Exception as e:
        print(f"[-] Erro de conexao IndexNow: {e}")

def ping_sitemaps():
    print("[*] Submissao via IndexNow cobre Bing, Copilot, Seznam, Naver e parceiros automaticamente.")

if __name__ == "__main__":
    submit_indexnow()
    ping_sitemaps()
    print("[*] Ciclo de submissao e notificacao aos crawlers concluido!")
