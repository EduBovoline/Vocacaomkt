@echo off
setlocal EnableExtensions
title Vocacao Digital 2027 - Iniciar Todas as Ferramentas
echo ========================================================
echo   INICIANDO ECOSSISTEMA COMPLETO VOCACAO DIGITAL 2027
echo ========================================================
echo.

rem ------------------------------------------------------------------
rem  P1 (auditoria): este .bat vive na pasta operacoes, portanto a raiz
rem  do repositorio e "%~dp0..". Os caminhos antigos ("%~dp0twenty-crm",
rem  "%~dp0openseo", "%~dp0serpbear") apontavam para dentro de operacoes.
rem  A stack da Evolution API fica fora do repo e e localizada pelo nome,
rem  sem acento no script, para evitar problema de codepage.
rem ------------------------------------------------------------------
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

if not exist "%DOCKER%" if /i not "%DOCKER%"=="docker" (
    echo [ERRO] Docker nao encontrado. Abra o Docker Desktop e rode novamente.
    goto :falha
)

echo [1/5] Subindo Twenty CRM ^(Porta 3000^)...
pushd "%ROOT%\twenty-crm"
"%DOCKER%" compose up -d
if errorlevel 1 echo [AVISO] Falha ao subir o Twenty CRM.
popd

echo.
echo [2/5] Subindo WhatsApp e n8n ^(Evolution API + Redis + Postgres + n8n^)...
if exist "%LOCAL_STACK%\docker-compose.yml" (
    pushd "%LOCAL_STACK%"
    "%DOCKER%" compose up -d
    if errorlevel 1 echo [AVISO] Falha ao subir a stack local em "%LOCAL_STACK%".
    popd
) else (
    echo [AVISO] Stack nao encontrada. Defina VOCACAO_LOCAL_STACK com o caminho correto.
    echo         A Evolution API nao sera iniciada; o Auto-Responder sobe sem ela.
)

echo.
echo [3/5] Subindo OpenSEO ^(Porta 3001^) e SerpBear ^(Porta 5000^)...
pushd "%ROOT%\openseo"
"%DOCKER%" compose up -d
if errorlevel 1 echo [AVISO] Falha ao subir o OpenSEO.
popd
pushd "%ROOT%\serpbear"
"%DOCKER%" compose up -d
if errorlevel 1 echo [AVISO] Falha ao subir o SerpBear.
popd

echo.
echo [4/5] Subindo Auto-Responder Inteligente ^(Porta 5680^)...
if not exist "%ROOT%\2 Leads" (
    echo [ERRO] Pasta de leads nao encontrada: "%ROOT%\2 Leads"
    echo        O bind mount do container depende dela. Etapa ignorada.
    goto :resumo
)
pushd "%ROOT%\operacoes\auto_responder_docker"
"%DOCKER%" compose up -d --build
if errorlevel 1 (
    echo [AVISO] Falha ao subir o container vocacao-auto-responder.
    echo         Rode "docker compose logs vocacao-auto-responder" para ver o motivo.
)
popd

:resumo
echo.
echo [5/5] Status resumido dos containers do projeto...
"%DOCKER%" ps --filter "name=vocacao" --filter "name=twenty" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo.
echo ========================================================
echo   TUDO PRONTO E RODANDO 100%!
echo.
echo   1. Twenty CRM:     http://localhost:3000
echo   2. Evolution API:  http://localhost:8080
echo   3. n8n Automacao:  http://localhost:5678
echo   4. Auto-Responder: http://localhost:5680/painel
echo   5. OpenSEO:        http://localhost:3001
echo   6. SerpBear:       http://localhost:5000 (admin / vocacao2027)
echo ========================================================
pause
exit /b 0

:falha
echo.
echo Inicializacao interrompida.
pause
exit /b 1
