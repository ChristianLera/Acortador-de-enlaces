# Script para ejecutar Shortify en PowerShell
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "   SHORTIFY - Acortador de Enlaces" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Iniciando la aplicacion..." -ForegroundColor Yellow
Write-Host ""

try {
    python AcortadorDeEnlaces.py
}
catch {
    Write-Host ""
    Write-Host "[ERROR] No se pudo ejecutar el programa." -ForegroundColor Red
    Write-Host "Asegurate de tener Python instalado." -ForegroundColor Red
    Write-Host ""
    Read-Host "Presiona Enter para salir"
}