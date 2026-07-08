@echo off
REM ============================================================
REM   Genera un EJECUTABLE PORTABLE (.exe) que NO requiere
REM   tener Python instalado en la maquina destino.
REM   Resultado: dist\EFA_Prep\EFA_Prep.exe  (copiar la carpeta
REM   dist\EFA_Prep completa; pesa ~140 MB).
REM ============================================================
setlocal
cd /d "%~dp0"
title Crear ejecutable EFA

where python >nul 2>nul || (echo [ERROR] Python no encontrado en el PATH. & pause & exit /b 1)

echo [1/3] Compilando el frontend (requiere Node.js/npm)...
pushd frontend
call npm install
call npm run build
popd
if errorlevel 1 (echo [ERROR] Fallo al compilar el frontend. & pause & exit /b 1)

echo [2/3] Instalando PyInstaller y dependencias...
python -m pip install --disable-pip-version-check -q pyinstaller -r requirements-portable.txt

echo [3/3] Empaquetando el ejecutable...
python -m PyInstaller --noconfirm --clean --name EFA_Prep ^
  --add-data "frontend/dist;frontend_dist" ^
  --collect-all uvicorn ^
  --collect-submodules backend ^
  --exclude-module google --exclude-module pytest ^
  run_portable.py
if errorlevel 1 (echo [ERROR] Fallo al generar el ejecutable. & pause & exit /b 1)

echo.
echo ============================================================
echo   Ejecutable creado: dist\EFA_Prep\EFA_Prep.exe
echo   Copia la carpeta "dist\EFA_Prep" a cualquier PC Windows y
echo   haz doble clic en EFA_Prep.exe (no necesita Python).
echo ============================================================
pause
endlocal
