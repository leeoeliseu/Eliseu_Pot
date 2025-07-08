@echo off
title Eliseu Pot - Executar como Administrador

echo ========================================
echo    ELISEU POT - RAGNAROK HELPER
echo ========================================
echo.

REM Verifica se está executando como admin
net session >nul 2>&1
if %errorLevel% == 0 (
    echo [OK] Executando como administrador
    echo.
    echo Iniciando aplicacao...
    python main.py
) else (
    echo [AVISO] Nao esta executando como administrador
    echo.
    echo Tentando elevar privilegios...
    echo.
    REM Tenta executar como admin
    powershell -Command "Start-Process python -ArgumentList 'main.py' -Verb RunAs"
)

if %errorLevel% neq 0 (
    echo.
    echo [ERRO] Falha ao executar como administrador
    echo.
    echo Como executar manualmente:
    echo 1. Clique com botao direito neste arquivo
    echo 2. Selecione "Executar como administrador"
    echo.
    echo Ou:
    echo 1. Abra o Prompt de Comando como administrador
    echo 2. Navegue ate esta pasta
    echo 3. Execute: python main.py
    echo.
    pause
)

REM Se chegou aqui e nao houve erro, a aplicacao foi executada
echo.
echo Aplicacao finalizada.
pause