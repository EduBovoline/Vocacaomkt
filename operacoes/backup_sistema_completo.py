"""
backup_sistema_completo.py — Backup Integral do Sistema Vocação 2027
Exporta:
1. Dump Completo do Banco PostgreSQL (Twenty CRM com todas as empresas, oportunidades e notas)
2. Variáveis de ambiente e chaves (.env Twenty CRM e Evolution API)
3. Scripts de automação do motor de prospecção (disparador_fila_7min, auto_responder, sincronizadores)
4. Diagnósticos e dossiês de leads (PDFs de 3 páginas, HTMLs e relatórios)
5. Gera arquivo ZIP único e consolidado em C:\Vocação 2027\Backups
"""

import os
import sys
import shutil
import zipfile
import subprocess
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M")
BACKUP_ROOT = r"C:\Vocação 2027\Backups"
TEMP_DIR = os.path.join(BACKUP_ROOT, f"temp_sistema_{TIMESTAMP}")
ZIP_DEST = os.path.join(BACKUP_ROOT, f"Backup_Completo_Vocacao_{TIMESTAMP}.zip")

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(BACKUP_ROOT, exist_ok=True)

print(f"==================================================")
print(f"📦 INICIANDO BACKUP INTEGRAL DO SISTEMA VOCAÇÃO 2027")
print(f"Timestamp: {TIMESTAMP}")
print(f"==================================================")

# 1. DUMP DO BANCO DE DADOS POSTGRESQL (Twenty CRM)
sql_dump_file = os.path.join(TEMP_DIR, "twenty_crm_dump_completo.sql")
print("\n[1/4] Extraindo Dump completo do PostgreSQL (Twenty CRM)...")
try:
    with open(sql_dump_file, "w", encoding="utf-8") as f:
        proc = subprocess.Popen(
            ["docker", "exec", "-i", "twenty-db-1", "pg_dump", "-U", "postgres", "-d", "twenty"],
            stdout=f, stderr=subprocess.PIPE, text=True
        )
        _, err = proc.communicate()
    size_mb = os.path.getsize(sql_dump_file) / (1024 * 1024)
    print(f"   ✓ Dump gerado com sucesso: {size_mb:.2f} MB")
except Exception as e:
    print(f"   ! Erro ao extrair dump: {e}")

# 2. SCRIPTS DE AUTOMAÇÃO E MOTORES
print("\n[2/4] Copiando scripts de automação e motores...")
scripts_dir = os.path.join(TEMP_DIR, "scripts_automacao")
os.makedirs(scripts_dir, exist_ok=True)

scripts_to_copy = [
    r"C:\Vocação 2027\QG Vocação 2027 do zero\disparador_fila_7min.py",
    r"C:\Vocação 2027\QG Vocação 2027 do zero\auto_responder.py",
    r"C:\Vocação 2027\QG Vocação 2027 do zero\enriquecer_leads_twenty.py",
    r"C:\Vocação 2027\QG Vocação 2027 do zero\importar_leads_twenty.py",
    r"C:\Vocação 2027\QG Vocação 2027 do zero\sincronizar_leads_crm_completos.py",
    r"C:\Vocação 2027\QG Vocação 2027 do zero\INICIAR_TODAS_FERRAMENTAS.bat",
    r"C:\Vocação 2027\QG Vocação 2027 do zero\PARAR_TODAS_FERRAMENTAS.bat",
]

for s in scripts_to_copy:
    if os.path.exists(s):
        shutil.copy2(s, scripts_dir)
        print(f"   ✓ Script copiado: {os.path.basename(s)}")

# 3. CONFIGURAÇÕES E CHAVES (.env)
print("\n[3/4] Salvaguardando configurações de infraestrutura e .env...")
config_dir = os.path.join(TEMP_DIR, "configuracoes")
os.makedirs(config_dir, exist_ok=True)

env_files = [
    r"C:\Vocação 2027\QG Vocação 2027 do zero\twenty-crm\.env",
    r"C:\Vocação 2027\QG Vocação 2027 do zero\twenty-crm\docker-compose.yml",
    r"D:\Funnel vendas objeção\local_stack\docker-compose.yml",
    r"D:\Funnel vendas objeção\local_stack\evolution_instances\vocacao_comercial.json"
]

for ef in env_files:
    if os.path.exists(ef):
        shutil.copy2(ef, config_dir)
        print(f"   ✓ Configuração copiada: {os.path.basename(ef)}")

# 4. LEADS AUDITADOS, DOSSIÊS E PDFs
print("\n[4/4] Copiando dossiês, diagnósticos em PDF e relatórios...")
leads_src = r"C:\Vocação 2027\QG Vocação 2027 do zero\2 Leads"
leads_dest = os.path.join(TEMP_DIR, "2 Leads")
if os.path.exists(leads_src):
    shutil.copytree(leads_src, leads_dest, dirs_exist_ok=True)
    count_pdfs = sum(len([f for f in files if f.endswith(".pdf")]) for _, _, files in os.walk(leads_dest))
    print(f"   ✓ Pasta '2 Leads' compactada com {count_pdfs} PDFs gerados.")

# 5. COMPACTAÇÃO EM ARQUIVO ZIP ÚNICO
print(f"\n📦 Compactando tudo no arquivo final: {ZIP_DEST}...")
with zipfile.ZipFile(ZIP_DEST, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(TEMP_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, TEMP_DIR)
            zipf.write(full_path, rel_path)

# Limpa temporários
shutil.rmtree(TEMP_DIR, ignore_errors=True)
final_size_mb = os.path.getsize(ZIP_DEST) / (1024 * 1024)

print(f"\n==================================================")
print(f"🎉 BACKUP CONCLUÍDO COM SUCESSO!")
print(f"Local: {ZIP_DEST}")
print(f"Tamanho total: {final_size_mb:.2f} MB")
print(f"==================================================")
