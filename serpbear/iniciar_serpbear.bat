@echo off
title Vocacao Digital 2027 - SerpBear (Monitor de Posicoes no Google)
echo ========================================================
echo   INICIANDO SERPBEAR - RANK TRACKER VOCACAO 2027
echo ========================================================
cd /d "%~dp0"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose up -d
echo.
echo ========================================================
echo   SERPBEAR RODANDO!
echo   Acesse no navegador: http://localhost:5000
echo   Usuario: admin  |  Senha: vocacao2027
echo ========================================================
pause
