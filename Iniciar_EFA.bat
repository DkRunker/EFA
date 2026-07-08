@echo off
REM ============================================================
REM   Plataforma EFA - Lanzador portable (Windows)
REM   Arranca el servidor local y abre la app en el navegador.
REM ============================================================
setlocal
cd /d "%~dp0"
title Plataforma EFA

REM 1) Localizar Python (py launcher o python en PATH)
set "PYEXE="
where py >nul 2>nul && set "PYEXE=py"
if not defined PYEXE (
    where python >nul 2>nul && set "PYEXE=python"
)
if not defined PYEXE (
    echo [ERROR] No se ha encontrado Python en el sistema.
    echo Instala Python 3.11 o superior desde https://www.python.org/downloads/
    echo y marca la casilla "Add Python to PATH" durante la instalacion.
    pause
    exit /b 1
)

REM 2) Comprobar dependencias; instalarlas si faltan
%PYEXE% -c "import fastapi, uvicorn, pydantic, dotenv" >nul 2>nul
if errorlevel 1 (
    echo Instalando dependencias necesarias por primera vez...
    %PYEXE% -m pip install --disable-pip-version-check -q -r requirements-portable.txt
    if errorlevel 1 (
        echo [ERROR] No se pudieron instalar las dependencias.
        echo Revisa tu conexion a internet e intentalo de nuevo.
        pause
        exit /b 1
    )
)

REM 3) Arrancar la plataforma (abre el navegador automaticamente)
echo Iniciando la Plataforma EFA...
%PYEXE% run_portable.py

pause
endlocal
