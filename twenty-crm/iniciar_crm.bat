@echo off
title Vocacao Digital 2027 - Twenty CRM
echo ========================================================
echo   INICIANDO TWENTY CRM - VOCACAO DIGITAL 2027
echo ========================================================
cd /d "%~dp0"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose up -d
echo.
echo ========================================================
echo   TWENTY CRM RODANDO!
echo   Acesse no seu navegador: http://localhost:3000
echo ========================================================
pause
