# Obtener la ruta del script y cambiar al directorio del script
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $SCRIPT_DIR

# Configuración
$VENV_DIR = ".venv"    # Ruta al entorno virtual
$UI_DIR = "ui"        # Directorio donde están los archivos .ui
# $OUT_DIR = "generated_ui"    # Directorio de salida para los archivos .py

# Verificar si el entorno virtual existe
if (Test-Path "$VENV_DIR/Scripts/Activate.ps1") {
    Write-Host "✅ Activando entorno virtual..."
    & "$VENV_DIR/Scripts/Activate.ps1"
} else {
    Write-Host "❌ Error: No se encontró el entorno virtual '$VENV_DIR'"
    exit 1
}

# # Crear el directorio de salida si no existe
# if (!(Test-Path $OUT_DIR)) {
#     New-Item -ItemType Directory -Path $OUT_DIR | Out-Null
# }

# Buscar y convertir archivos .ui
Get-ChildItem -Path $UI_DIR -Filter "*.ui" | ForEach-Object {
    $ui_file = $_.FullName
    $output_file = "$UI_DIR\$($_.BaseName)_ui.py"
    Write-Host "🔄 Convirtiendo: $ui_file → $output_file"
    pyside6-uic $ui_file -o $output_file
}