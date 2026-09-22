@echo off
title Vocacao Digital 2027 - Iniciar Todas as Ferramentas
echo ========================================================
echo   INICIANDO ECOSSISTEMA COMPLETO VOCACAO DIGITAL 2027
echo ========================================================
echo.

echo [1/3] Subindo Twenty CRM (Porta 3000)...
cd /d "%~dp0twenty-crm"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose up -d

echo [2/3] Subindo OpenSEO (Porta 3001)...
cd /d "%~dp0openseo"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose up -d

echo [3/3] Subindo SerpBear (Porta 5000)...
cd /d "%~dp0serpbear"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose up -d

echo.
echo ========================================================
echo   TUDO PRONTO E RODANDO!
echo.
echo   1. Twenty CRM: http://localhost:3000
echo   2. OpenSEO:    http://localhost:3001
echo   3. SerpBear:   http://localhost:5000 (admin / vocacao2027)
echo ========================================================
pause
