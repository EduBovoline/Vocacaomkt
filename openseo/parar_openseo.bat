@echo off
title Vocacao Digital 2027 - Parar OpenSEO
cd /d "%~dp0"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose down
echo.
echo ========================================================
echo   OPENSEO PAUSADO COM SUCESSO!
echo ========================================================
pause
