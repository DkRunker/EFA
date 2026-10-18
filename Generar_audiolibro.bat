@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8

rem Genera el audiolibro por bloques con VoiceStudio (debe estar abierto).
rem Uso: doble clic = bloque de 120 minutos.  O bien:  Generar_audiolibro.bat 60   (minutos)
rem      Generar_audiolibro.bat 90 m3          (solo el módulo 3)
rem Lo generado se guarda al momento: puedes cerrar la ventana cuando quieras y continuar otro día.

set MINUTOS=%1
if "%MINUTOS%"=="" set MINUTOS=120

echo.
echo === Audiolibro EFA: bloque de %MINUTOS% minutos ===
echo.
python audiolibro\sintetizar.py %2 %3 %4 --max-minutos %MINUTOS%
echo.
echo === Uniendo los modulos que esten completos (.m4b con capitulos) ===
python audiolibro\juntar.py
echo.
echo === Estado ===
python audiolibro\sintetizar.py --estado | findstr /C:"dulo" /C:"Queda"
echo.
pause
