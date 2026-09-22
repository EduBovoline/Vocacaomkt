@echo off
title Vocacao Digital 2027 - OpenSEO (Semrush Open-Source)
echo ========================================================
echo   INICIANDO OPENSEO - SUITE DE SEO VOCACAO 2027
echo ========================================================
cd /d "%~dp0"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose up -d
echo.
echo ========================================================
echo   OPENSEO RODANDO!
echo   Acesse no navegador: http://localhost:3001
echo ========================================================
pause
