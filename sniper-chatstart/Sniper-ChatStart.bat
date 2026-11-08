@echo off
chcp 65001 >nul
title Sniper ChatStart - Vocação Digital

echo ==============================================================
echo   🚀 SNIPER CHATSTART — VOCAÇÃO COMUNICAÇÃO & MARKETING
echo ==============================================================
echo.
echo [1/2] Verificando ambiente Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python não foi encontrado no seu computador!
    echo Por favor, instale o Python em https://www.python.org/
    pause
    exit /b
)

echo [2/2] Criando atalho oficial com o ícone da Vocação...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%~dp0Sniper-ChatStart.lnk'); $s.TargetPath = '%~dp0Sniper-ChatStart.bat'; $s.IconLocation = '%~dp0app.ico, 0'; $s.Save()" >nul 2>&1

echo.
echo ✅ Tudo pronto! Abrindo o painel no seu navegador...
echo    Painel: http://localhost:7860
echo.
echo [DICA] Mantenha esta janela aberta enquanto estiver usando.
echo ==============================================================
echo.

python "%~dp0app.py"
pause
