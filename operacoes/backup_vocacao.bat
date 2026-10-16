@echo off
chcp 65001 >nul
echo ===================================================
echo   INICIANDO BACKUP CONSOLIDADO - VOCAÇÃO 2027
echo ===================================================
powershell -ExecutionPolicy Bypass -File "%~dp0backup_vocacao.ps1"
echo.
python "%~dp0backup_sistema_completo.py"
echo.
pause
