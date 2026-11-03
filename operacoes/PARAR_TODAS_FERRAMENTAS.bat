@echo off
setlocal EnableExtensions
title Vocacao Digital 2027 - Parar Todas as Ferramentas
echo ========================================================
echo   PAUSANDO ECOSSISTEMA VOCACAO DIGITAL 2027
echo ========================================================
echo.

rem P1 (auditoria): raiz do repositorio = "%~dp0.." (este .bat fica em operacoes).
set "ROOT=%~dp0.."
set "LOCAL_STACK=%VOCACAO_LOCAL_STACK%"
if "%LOCAL_STACK%"=="" (
    for /d %%D in ("D:\Funnel vendas obje*") do (
        if exist "%%~fD\local_stack\docker-compose.yml" set "LOCAL_STACK=%%~fD\local_stack"
    )
)

set "DOCKER=docker"
where docker >nul 2>&1
if errorlevel 1 set "DOCKER=C:\Program Files\Docker\Docker\resources\bin\docker.exe"

echo [1/5] Finalizando Auto-Responder em container...
pushd "%ROOT%\operacoes\auto_responder_docker"
"%DOCKER%" compose down
popd

echo.
echo [2/5] Finalizando Auto-Responder em modo host ^(se estiver rodando^)...
taskkill /f /fi "WINDOWTITLE eq AutoResponder-Vocacao*" >nul 2>&1

echo.
echo [3/5] Parando WhatsApp e n8n Stack...
if exist "%LOCAL_STACK%\docker-compose.yml" (
    pushd "%LOCAL_STACK%"
    "%DOCKER%" compose down
    popd
) else (
    echo [AVISO] Stack nao encontrada. Nada a parar.
)

echo.
echo [4/5] Parando SerpBear e OpenSEO...
pushd "%ROOT%\serpbear"
"%DOCKER%" compose down
popd
pushd "%ROOT%\openseo"
"%DOCKER%" compose down
popd

echo.
echo [5/5] Parando Twenty CRM...
pushd "%ROOT%\twenty-crm"
"%DOCKER%" compose down
popd

echo.
echo ========================================================
echo   TODAS AS FERRAMENTAS FORAM PAUSADAS COM SUCESSO!
echo ========================================================
pause
exit /b 0
