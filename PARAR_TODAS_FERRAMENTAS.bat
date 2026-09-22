@echo off
title Vocacao Digital 2027 - Parar Todas as Ferramentas
echo ========================================================
echo   PAUSANDO ECOSSISTEMA VOCACAO DIGITAL 2027
echo ========================================================
echo.

echo [1/3] Parando SerpBear...
cd /d "%~dp0serpbear"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose down

echo [2/3] Parando OpenSEO...
cd /d "%~dp0openseo"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose down

echo [3/3] Parando Twenty CRM...
cd /d "%~dp0twenty-crm"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose down

echo.
echo ========================================================
echo   TODAS AS FERRAMENTAS FORAM PAUSADAS COM SUCESSO!
echo ========================================================
pause
