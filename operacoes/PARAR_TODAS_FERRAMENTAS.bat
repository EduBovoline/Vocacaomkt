@echo off
title Vocacao Digital 2027 - Parar Todas as Ferramentas
echo ========================================================
echo   PAUSANDO ECOSSISTEMA VOCACAO DIGITAL 2027
echo ========================================================
echo.

echo [1/4] Finalizando Auto-Responder...
taskkill /f /fi "WINDOWTITLE eq AutoResponder-Vocacao*" >nul 2>&1

echo [2/4] Parando WhatsApp & n8n Stack...
cd /d "D:\Funnel vendas objeção\local_stack"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose down

echo [3/4] Parando SerpBear e OpenSEO...
cd /d "%~dp0serpbear"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose down
cd /d "%~dp0openseo"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose down

echo [4/4] Parando Twenty CRM...
cd /d "%~dp0twenty-crm"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose down

echo.
echo ========================================================
echo   TODAS AS FERRAMENTAS FORAM PAUSADAS COM SUCESSO!
echo ========================================================
pause
