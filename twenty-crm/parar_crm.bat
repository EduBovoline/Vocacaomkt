@echo off
title Vocacao Digital 2027 - Parar Twenty CRM
cd /d "%~dp0"
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose down
echo.
echo ========================================================
echo   TWENTY CRM PAUSADO COM SUCESSO!
echo ========================================================
pause
