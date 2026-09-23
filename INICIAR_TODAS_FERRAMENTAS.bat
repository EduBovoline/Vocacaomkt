@echo off
title Vocacao Digital 2027 - Iniciar Todas as Ferramentas
echo ========================================================
echo   INICIANDO ECOSSISTEMA COMPLETO VOCACAO DIGITAL 2027
echo ========================================================
echo.

echo [1/4] Subindo Twenty CRM (Porta 3000)...
cd /d "%~dp0twenty-crm"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose up -d

echo [2/4] Subindo WhatsApp & n8n Stack (Evolution API + Redis + Postgres + n8n)...
cd /d "D:\Funnel vendas objeção\local_stack"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose up -d

echo [3/4] Subindo OpenSEO (Porta 3001) e SerpBear (Porta 5000)...
cd /d "%~dp0openseo"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose up -d
cd /d "%~dp0serpbear"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose up -d

echo [4/4] Iniciando Auto-Responder Inteligente (Porta 5680)...
cd /d "%~dp0"
start /min "AutoResponder-Vocacao" python auto_responder.py

echo.
echo ========================================================
echo   TUDO PRONTO E RODANDO 100%!
echo.
echo   1. Twenty CRM:     http://localhost:3000
echo   2. Evolution API:  http://localhost:8080
echo   3. n8n Automação:  http://localhost:5678
echo   4. Auto-Responder: Ativo (Porta 5680)
echo   5. OpenSEO:        http://localhost:3001
echo   6. SerpBear:       http://localhost:5000 (admin / vocacao2027)
echo ========================================================
pause

