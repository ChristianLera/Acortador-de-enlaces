@echo off
title Shortify - Acortador de Enlaces
echo ======================================
echo    SHORTIFY - Acortador de Enlaces
echo ======================================
echo.
echo Iniciando la aplicacion...
echo.

python AcortadorDeEnlaces.py

if errorlevel 1 (
    echo.
    echo [ERROR] No se pudo ejecutar el programa.
    echo Asegurate de tener Python instalado.
    echo.
    pause
)