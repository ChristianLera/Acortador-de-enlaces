# 🔗 Shortify - Acortador de Enlaces

**Shortify** es una aplicación de escritorio con interfaz gráfica que te permite convertir URLs largas y complicadas en códigos cortos y fáciles de compartir. Incluye sistema de ayuda integrado, estadísticas y seguimiento de clics.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)

---

## ✨ Características

- ✅ **Acortar URLs** largas en códigos de 6 caracteres
- 🎨 **Códigos personalizados** (elige tu propio código)
- 👆 **Contador de clics** (sabe cuántas veces se usó cada enlace)
- 📊 **Estadísticas completas** (total enlaces, clics, más visitado)
- 🗑️ **Eliminar enlaces** que ya no necesites
- 💾 **Persistencia de datos** (los enlaces se guardan en JSON)
- ❓ **Sistema de ayuda integrado** con explicaciones paso a paso
- 📅 **Fecha de creación** de cada enlace

---

## 📋 Requisitos

- **Python 3.6 o superior**
- Módulos estándar de Python (no requieren instalación adicional):
  - `tkinter` (interfaz gráfica)
  - `json` (almacenamiento de datos)
  - `datetime` (manejo de fechas)
  - `urllib.parse` (validación de URLs)

> **Nota**: En algunas distribuciones de Linux, `tkinter` puede necesitar instalación por separado:
> ```bash
> sudo apt-get install python3-tk   # Debian/Ubuntu
> ```

---

## 🚀 Instalación y Ejecución

### Opción 1: Ejecutar directamente (Windows)

1. Descarga todos los archivos en una carpeta
2. Haz doble clic en `ejecutar.bat`
3. También puedes usar PowerShell con `ejecutar.ps1`

### Opción 2: Desde terminal

```bash
python AcortadorDeEnlaces.py
Opción 3: Especificar Python 3 explícitamente
bash
python3 AcortadorDeEnlaces.py
🖥️ Cómo usar Shortify
Paso 1: Acortar una URL
Escribe una URL larga (ej: https://www.google.com/muchas/cosas)

Opcional: escribe un código personalizado (ej: google2024)

Haz clic en "ACORTAR URL"

El nuevo enlace aparece en la tabla

Paso 2: Ver una URL original
Selecciona un enlace de la tabla (haz clic en la fila)

Haz clic en "VER URL ORIGINAL"

Se mostrará la URL completa y aumentará el contador de clics

Paso 3: Eliminar un enlace
Selecciona un enlace de la tabla

Haz clic en "ELIMINAR SELECCIONADO"

Confirma la eliminación

Paso 4: Ver estadísticas
Haz clic en "VER ESTADÍSTICAS"

Muestra: total de enlaces, clics totales, más visitado, etc.

Paso 5: Ayuda
Haz clic en "AYUDA" para ver explicaciones detalladas de cada función

📁 Estructura de archivos
text
📂 AcortadorDeEnlaces/
├── AcortadorDeEnlaces.py   # Programa principal
├── urls.json               # Base de datos (se crea automáticamente)
├── README.md               # Este archivo
├── ejecutar.bat            # Script para Windows (CMD)
├── ejecutar.ps1            # Script para Windows (PowerShell)
└── requirements.txt        # Dependencias (solo documentación)
📊 Formato de datos (urls.json)
json
{
  "aB3x9K": {
    "original_url": "https://www.ejemplo.com/url/larga",
    "clicks": 5,
    "created_at": "2024-01-15 14:30:22"
  }
}
🛠️ Solución de problemas
Problema	Solución
ModuleNotFoundError: No module named 'tkinter'	Instalar tkinter: sudo apt-get install python3-tk
Error de permisos al guardar	Ejecutar el programa en una carpeta con permisos de escritura
La URL no se acorta	Asegúrate de que empiece con http:// o https://
El código ya existe	Usa otro código o déjalo vacío para que se genere automático
👨‍💻 Autor
Christian Lera

📜 Licencia
Este proyecto es de uso libre para fines educativos y personales.

🤝 Contribuciones
Las contribuciones son bienvenidas. Puedes:

Reportar bugs

Sugerir nuevas funcionalidades

Mejorar la documentación

🙏 Agradecimientos
Inspirado en acortadores de URLs como Bitly y TinyURL

Interfaz construida con Tkinter de Python

📞 Contacto
Para consultas o sugerencias, abre un issue en el repositorio del proyecto.