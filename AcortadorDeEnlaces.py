#!/usr/bin/env python3
"""
URL Shortener - Con sistema de ayuda y explicaciones
Cada función tiene su descripción para entender qué se está haciendo
"""

import json
import os
import random
import string
from datetime import datetime
from urllib.parse import urlparse
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkfont

# ========== CONFIGURACIÓN ==========
DATA_FILE = "urls.json"
CODE_LENGTH = 6

# ========== MANEJO DE DATOS ==========
def load_urls():
    """Carga los enlaces guardados desde el archivo JSON"""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_urls(urls):
    """Guarda los enlaces en el archivo JSON para que no se pierdan al cerrar el programa"""
    with open(DATA_FILE, 'w') as f:
        json.dump(urls, f, indent=2)

def generate_code():
    """Genera un código aleatorio de 6 caracteres (letras mayúsculas, minúsculas y números)"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(CODE_LENGTH))

def is_valid_url(url):
    """Verifica si una URL tiene el formato correcto (ej: https://google.com)"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

# ========== APLICACIÓN PRINCIPAL ==========
class URLShortenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shortify - Acortador de Enlaces con Ayuda")
        self.root.geometry("1200x1000")
        self.root.configure(bg='#f0f0f0')
        
        self.setup_ui()
        self.refresh_table()
        self.show_welcome_message()
    
    def show_welcome_message(self):
        """Mensaje de bienvenida explicando qué hace el programa"""
        mensaje = """
🔗 BIENVENIDO A SHORTIFY

¿QUÉ ES ESTE PROGRAMA?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Este programa convierte URLs largas y complicadas en códigos cortos y fáciles de compartir.

¿PARA QUÉ SIRVE?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Compartir enlaces en redes sociales (Twitter, WhatsApp, Instagram)
• Enviar URLs por SMS o email (ocupan menos espacio)
• Crear códigos QR más simples
• Hacer seguimiento de cuántas personas hacen clic en tus enlaces

¿CÓMO FUNCIONA?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Ingresas una URL larga (ej: https://www.google.com/muchas/cosas/largas)
2. El programa genera un código único (ej: aB3x9K)
3. Guarda la relación URL ←→ código en un archivo JSON
4. Cuando alguien quiere ver la URL original, solo necesita el código
5. El programa cuenta cuántas veces se ha consultado cada enlace

¿QUÉ PUEDES HACER?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ ACORTAR: Convierte URLs largas en códigos cortos
🔍 VER URL: Muestra la URL original y cuenta un clic
🗑️ ELIMINAR: Borra enlaces que ya no necesitas
📊 ESTADÍSTICAS: Muestra cuántos enlaces y clics tienes
🔄 REFRESCAR: Actualiza la tabla con los últimos datos

💾 LOS DATOS SE GUARDAN AUTOMÁTICAMENTE
Al cerrar y volver a abrir, tus enlaces siguen ahí.
        """
        messagebox.showinfo("Bienvenido a Shortify", mensaje)
    
    def setup_ui(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título con descripción
        title_frame = tk.Frame(main_frame, bg='#f0f0f0')
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        title = tk.Label(title_frame, text="🔗 SHORTIFY", font=("Arial", 28, "bold"), 
                        bg='#f0f0f0', fg='#333')
        title.pack()
        
        subtitle = tk.Label(title_frame, 
                           text="Convierte URLs largas en códigos cortos y fáciles de compartir",
                           bg='#f0f0f0', fg='#666', font=("Arial", 10))
        subtitle.pack()
        
        # ===== SECCIÓN PARA ACORTAR =====
        add_frame = tk.LabelFrame(main_frame, text="✂️ PASO 1: Acortar una URL", 
                                  bg='white', font=("Arial", 12, "bold"))
        add_frame.pack(fill=tk.X, pady=(0, 20), padx=10)
        
        # Explicación de esta sección
        tk.Label(add_frame, text="📌 ¿Qué hago aquí? Ingreso la URL larga que quiero acortar",
                bg='white', fg='#2196F3', font=("Arial", 9, "italic")).pack(pady=(5,0))
        
        # URL larga
        tk.Label(add_frame, text="URL larga (la que quieres acortar):", 
                bg='white', font=("Arial", 10)).pack(pady=(10,0))
        
        # Tooltip en el entry
        self.url_entry = tk.Entry(add_frame, width=80, font=("Arial", 10))
        self.url_entry.pack(pady=5, padx=10, fill=tk.X)
        self.create_tooltip(self.url_entry, "Ejemplo: https://www.google.com/muchas/cosas/largas")
        
        # Código personalizado
        tk.Label(add_frame, text="Código personalizado (opcional):", 
                bg='white', font=("Arial", 10)).pack(pady=(10,0))
        
        self.code_entry = tk.Entry(add_frame, width=30, font=("Arial", 10))
        self.code_entry.pack(pady=5)
        self.create_tooltip(self.code_entry, "Si lo dejas vacío, se genera uno automático. Ejemplo: 'mi-enlace'")
        
        tk.Label(add_frame, text="💡 Si pones un código personalizado, será más fácil de recordar (ej: 'promo20')",
                bg='white', fg='#666', font=("Arial", 8, "italic")).pack()
        
        # Botón acortar con explicación
        btn_frame = tk.Frame(add_frame, bg='white')
        btn_frame.pack(pady=10)
        
        self.shorten_btn = tk.Button(btn_frame, text="✨ ACORTAR URL", command=self.shorten_url,
                                     bg='#4CAF50', fg='white', font=("Arial", 11, "bold"),
                                     padx=30, pady=8)
        self.shorten_btn.pack(side=tk.LEFT)
        self.create_tooltip(self.shorten_btn, "Haz clic aquí para generar un código corto para la URL que ingresaste")
        
        # Explicación del resultado
        tk.Label(add_frame, text="✅ Después de acortar, el nuevo enlace aparecerá en la tabla de abajo",
                bg='white', fg='#4CAF50', font=("Arial", 9, "italic")).pack(pady=(5,10))
        
        # ===== SECCIÓN DE LISTA DE ENLACES =====
        list_frame = tk.LabelFrame(main_frame, text="📋 PASO 2: Mis enlaces acortados", 
                                   bg='#f0f0f0', font=("Arial", 12, "bold"))
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        
        # Explicación de la tabla
        tk.Label(list_frame, text="📌 Aquí aparecen todos los enlaces que has acortado. Selecciona uno para verlo o eliminarlo.",
                bg='#f0f0f0', fg='#2196F3', font=("Arial", 9, "italic")).pack(anchor=tk.W, pady=(5,5))
        
        # Tabla
        columns = ("Código", "URL Original", "Clics", "Creado")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=10)
        
        self.tree.heading("Código", text="🔑 Código corto")
        self.tree.heading("URL Original", text="🌐 URL original (la larga)")
        self.tree.heading("Clics", text="👆 Veces usado")
        self.tree.heading("Creado", text="📅 Fecha de creación")
        
        self.tree.column("Código", width=120, anchor=tk.CENTER)
        self.tree.column("URL Original", width=500, anchor=tk.W)
        self.tree.column("Clics", width=100, anchor=tk.CENTER)
        self.tree.column("Creado", width=150, anchor=tk.CENTER)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=5)
        
        self.create_tooltip(self.tree, "Haz clic en cualquier fila para seleccionar un enlace, luego usa los botones de abajo")
        
        # ===== BOTONES DE ACCIÓN =====
        btn_frame = tk.LabelFrame(main_frame, text="PASO 3: Acciones sobre el enlace seleccionado", 
                                  bg='#f0f0f0', font=("Arial", 12, "bold"))
        btn_frame.pack(fill=tk.X, pady=15, padx=10)
        
        # Explicación
        tk.Label(btn_frame, text="📌 Primero selecciona un enlace de la tabla (haz clic en él), luego elige una acción:",
                bg='#f0f0f0', fg='#2196F3', font=("Arial", 9, "italic")).pack(anchor=tk.W, pady=(5,10))
        
        # Botones
        buttons_frame = tk.Frame(btn_frame, bg='#f0f0f0')
        buttons_frame.pack(fill=tk.X, pady=5)
        
        # Botón Ver URL
        btn_ver = tk.Button(buttons_frame, text="🔍 VER URL ORIGINAL", 
                           command=self.view_url,
                           bg='#2196F3', fg='white', 
                           font=("Arial", 10, "bold"),
                           padx=20, pady=8)
        btn_ver.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        self.create_tooltip(btn_ver, "Muestra la URL original y cuenta 1 clic (útil para saber quién lo ha usado)")
        
        # Botón Eliminar
        btn_eliminar = tk.Button(buttons_frame, text="🗑️ ELIMINAR SELECCIONADO", 
                                command=self.delete_url,
                                bg='#f44336', fg='white', 
                                font=("Arial", 10, "bold"),
                                padx=20, pady=8)
        btn_eliminar.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        self.create_tooltip(btn_eliminar, "Borra el enlace permanentemente. No se puede recuperar.")
        
        # Botón Estadísticas
        btn_stats = tk.Button(buttons_frame, text="📊 VER ESTADÍSTICAS", 
                             command=self.show_stats,
                             bg='#FF9800', fg='white', 
                             font=("Arial", 10, "bold"),
                             padx=20, pady=8)
        btn_stats.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        self.create_tooltip(btn_stats, "Muestra resumen: total de enlaces, clics totales, más visitado")
        
        # Botón Refrescar
        btn_refresh = tk.Button(buttons_frame, text="🔄 REFRESCAR TABLA", 
                               command=self.refresh_table,
                               bg='#9E9E9E', fg='white', 
                               font=("Arial", 10, "bold"),
                               padx=20, pady=8)
        btn_refresh.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        self.create_tooltip(btn_refresh, "Actualiza la tabla por si alguien más modificó los datos")
        
        # Botón Ayuda
        btn_help = tk.Button(buttons_frame, text="❓ AYUDA", 
                            command=self.show_help,
                            bg='#9C27B0', fg='white', 
                            font=("Arial", 10, "bold"),
                            padx=20, pady=8)
        btn_help.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        self.create_tooltip(btn_help, "Muestra explicación detallada de cada función del programa")
        
        # Barra de estado (muestra información en tiempo real)
        self.status_var = tk.StringVar()
        status_bar = tk.Label(self.root, textvariable=self.status_var, 
                              bg='#333', fg='white', 
                              anchor=tk.W, padx=10, font=("Arial", 9))
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Actualizar estado inicial
        self.update_status("Listo. Ingresa una URL y haz clic en 'Acortar URL'")
    
    def create_tooltip(self, widget, text):
        """Crea un tooltip que aparece al pasar el mouse sobre un elemento"""
        def enter(event):
            self.tooltip = tk.Toplevel()
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            label = tk.Label(self.tooltip, text=text, bg='#ffffcc', fg='#333',
                           font=("Arial", 9), relief=tk.SOLID, borderwidth=1,
                           padx=5, pady=2)
            label.pack()
        
        def leave(event):
            if hasattr(self, 'tooltip'):
                self.tooltip.destroy()
        
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)
    
    def update_status(self, message):
        """Actualiza la barra de estado con información útil"""
        self.status_var.set(f"💡 {message}")
    
    def shorten_url(self):
        """Acorta una URL - explica qué está haciendo"""
        url = self.url_entry.get().strip()
        custom = self.code_entry.get().strip()
        
        self.update_status("Verificando la URL ingresada...")
        
        if not url:
            messagebox.showwarning("Error", "No ingresaste ninguna URL.\n\nEscribe algo como: https://www.google.com")
            self.update_status("Esperando URL para acortar")
            return
        
        if not is_valid_url(url):
            messagebox.showerror("Error", 
                               "La URL no es válida.\n\n"
                               "Asegúrate de que comience con http:// o https://\n"
                               "Ejemplo correcto: https://www.google.com")
            self.update_status("URL inválida, corrige el formato")
            return
        
        urls = load_urls()
        
        # Verificar si ya existe
        for code, info in urls.items():
            if info['original_url'] == url:
                messagebox.showinfo("Info", 
                                   f"Esta URL ya está acortada como: {code}\n\n"
                                   f"Usa ese código en lugar de crear uno nuevo.")
                self.update_status(f"La URL ya existe como '{code}'")
                return
        
        # Generar código
        code = custom if custom else generate_code()
        
        if code in urls:
            messagebox.showerror("Error", 
                               f"El código '{code}' ya está siendo usado por otra URL.\n\n"
                               f"Usa otro código personalizado o deja que el programa genere uno automático.")
            self.update_status("Código ya existe, prueba otro")
            return
        
        self.update_status(f"Guardando la relación: {code} → {url[:50]}...")
        
        # Guardar
        urls[code] = {
            'original_url': url,
            'clicks': 0,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        save_urls(urls)
        
        self.url_entry.delete(0, tk.END)
        self.code_entry.delete(0, tk.END)
        self.refresh_table()
        
        messagebox.showinfo("Éxito", 
                           f"✅ URL ACORTADA EXITOSAMENTE!\n\n"
                           f"📌 Código: {code}\n\n"
                           f"🔗 Ahora puedes compartir este código en lugar de la URL larga.\n\n"
                           f"💡 Cuando alguien quiera ver la URL original, selecciona este enlace en la tabla y haz clic en 'Ver URL original'.")
        
        self.update_status(f"Enlace acortado exitosamente con código '{code}'")
    
    def view_url(self):
        """Muestra la URL original - explica qué está pasando"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Advertencia", 
                                 "No has seleccionado ningún enlace.\n\n"
                                 "PASOS:\n"
                                 "1. Haz clic en un enlace de la tabla (se resaltará en azul)\n"
                                 "2. Luego haz clic en 'Ver URL original'")
            self.update_status("Primero selecciona un enlace de la tabla")
            return
        
        code = self.tree.item(selected[0])['values'][0]
        urls = load_urls()
        
        if code in urls:
            # Incrementar clics
            urls[code]['clicks'] += 1
            save_urls(urls)
            
            messagebox.showinfo("URL Original", 
                               f"📌 CÓDIGO: {code}\n\n"
                               f"🔗 URL ORIGINAL:\n{urls[code]['original_url']}\n\n"
                               f"👆 ESTE ENLACE HA SIDO USADO {urls[code]['clicks']} VECES\n\n"
                               f"💡 Cada vez que alguien consulta la URL original, los clics aumentan. "
                               f"¡Así sabes cuánta gente está usando tu enlace!")
            
            self.refresh_table()
            self.update_status(f"Se consultó '{code}' - ahora tiene {urls[code]['clicks']} clics")
        else:
            messagebox.showerror("Error", "El enlace seleccionado ya no existe en la base de datos")
            self.refresh_table()
    
    def delete_url(self):
        """Elimina un enlace - advierte de lo que hace"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Advertencia", 
                                 "No has seleccionado ningún enlace.\n\n"
                                 "PASOS:\n"
                                 "1. Haz clic en un enlace de la tabla\n"
                                 "2. Luego haz clic en 'Eliminar seleccionado'")
            self.update_status("Primero selecciona un enlace para eliminar")
            return
        
        code = self.tree.item(selected[0])['values'][0]
        
        if messagebox.askyesno("Confirmar eliminación", 
                              f"⚠️ ¿ESTÁS SEGURO DE ELIMINAR '{code}'?\n\n"
                              f"📌 Código: {code}\n\n"
                              f"🚨 ADVERTENCIA:\n"
                              f"• El enlace se borrará permanentemente\n"
                              f"• No podrás recuperar este enlace después\n"
                              f"• Las estadísticas de este enlace se perderán\n\n"
                              f"¿Deseas continuar?"):
            
            urls = load_urls()
            if code in urls:
                url_original = urls[code]['original_url']
                del urls[code]
                save_urls(urls)
                self.refresh_table()
                
                messagebox.showinfo("Eliminado", 
                                  f"✅ Enlace ELIMINADO correctamente\n\n"
                                  f"📌 Código eliminado: {code}\n"
                                  f"🔗 URL que fue eliminada: {url_original[:80]}...\n\n"
                                  f"💡 Si necesitas este enlace de nuevo, tendrás que acortarlo otra vez.")
                
                self.update_status(f"Enlace '{code}' eliminado permanentemente")
    
    def show_stats(self):
        """Muestra estadísticas - explica qué significan los números"""
        urls = load_urls()
        
        if not urls:
            messagebox.showinfo("Estadísticas", 
                              "No hay enlaces guardados todavía.\n\n"
                              "Para ver estadísticas, primero crea algunos enlaces usando 'Acortar URL'.")
            self.update_status("No hay enlaces para mostrar estadísticas")
            return
        
        total = len(urls)
        total_clicks = sum(info['clicks'] for info in urls.values())
        avg_clicks = total_clicks / total if total > 0 else 0
        
        # Encontrar el más visitado
        mas_visitado = max(urls.items(), key=lambda x: x[1]['clicks']) if urls else None
        
        # Encontrar el más reciente
        mas_reciente = max(urls.items(), key=lambda x: x[1]['created_at']) if urls else None
        
        # Encontrar el menos usado
        menos_usado = min(urls.items(), key=lambda x: x[1]['clicks']) if urls else None
        
        stats_text = f"""
╔══════════════════════════════════════════════════════════════╗
║                      📊 ESTADÍSTICAS                         ║
╚══════════════════════════════════════════════════════════════╝

📌 ¿QUÉ SIGNIFICAN ESTOS NÚMEROS?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Total enlaces: Cuántos enlaces has acortado
• Total clics: Cuántas veces se han consultado todos tus enlaces
• Promedio: En promedio, cuántos clics tiene cada enlace

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📈 TUS NÚMEROS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 TOTAL DE ENLACES ACORTADOS: {total}
👆 TOTAL DE CLICS RECIBIDOS: {total_clicks}
📈 PROMEDIO DE CLICS POR ENLACE: {avg_clicks:.1f}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏆 RÉCORDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 MÁS VISITADO (más clics):
   → Código: {mas_visitado[0]}
   → Clics: {mas_visitado[1]['clicks']}
   → URL: {mas_visitado[1]['original_url'][:60]}...

🆕 MÁS RECIENTE (creado hace menos tiempo):
   → Código: {mas_reciente[0]}
   → Fecha: {mas_reciente[1]['created_at']}

💤 MENOS USADO (0 clics o el mínimo):
   → Código: {menos_usado[0]}
   → Clics: {menos_usado[1]['clicks']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 ¿CÓMO USAR ESTA INFORMACIÓN?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Si un enlace tiene muchos clics → Está siendo útil, compártelo más
• Si un enlace tiene 0 clics → Nadie lo está usando, revisa si lo compartiste bien
• Puedes eliminar enlaces que no se usan para mantener ordenado

📁 ARCHIVO DE DATOS: {DATA_FILE}
💾 Los datos se guardan automáticamente aquí
        """
        
        messagebox.showinfo("Estadísticas detalladas", stats_text)
        self.update_status(f"Estadísticas: {total} enlaces, {total_clicks} clics totales")
    
    def show_help(self):
        """Muestra ayuda completa del programa"""
        help_text = """
❓ GUÍA COMPLETA DE SHORTIFY

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
¿QUÉ ES UN ACORTADOR DE ENLACES?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Un acortador de enlaces toma una URL larga como:
https://www.ejemplo.com/carpeta/subcarpeta/articulo?parametro=valor

Y la convierte en algo corto como: aB3x9K

El programa guarda esta relación para que cuando alguien use el código,
pueda recuperar la URL original.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
¿POR QUÉ ES ÚTIL?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📱 REDES SOCIALES: Twitter, Instagram tienen límite de caracteres
💬 WHATSAPP: Enlaces más limpios para enviar
📧 EMAILS: Se ven más profesionales
📊 MARKETING: Sabes cuántos clics tiene cada campaña
🔗 COMPARTIR: Más fácil de decir "usa el código promo20"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
¿CÓMO USAR EL PROGRAMA?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PASO 1: Acortar una URL
→ Escribe una URL larga (ej: https://www.google.com)
→ Opcional: escribe un código personalizado (ej: 'google')
→ Haz clic en "Acortar URL"
→ El nuevo enlace aparecerá en la tabla

PASO 2: Ver un enlace
→ Haz clic en cualquier fila de la tabla (se resalta)
→ Haz clic en "Ver URL original"
→ Se muestra la URL y cuenta un clic

PASO 3: Eliminar un enlace
→ Selecciona un enlace de la tabla
→ Haz clic en "Eliminar seleccionado"
→ Confirma la eliminación

PASO 4: Ver estadísticas
→ Haz clic en "Estadísticas"
→ Muestra total de enlaces, clics, récords

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DATOS TÉCNICOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 Los enlaces se guardan en: {DATA_FILE}
🔑 Los códigos tienen {CODE_LENGTH} caracteres
💾 Los datos persisten al cerrar y abrir el programa
        """
        
        messagebox.showinfo("Ayuda de Shortify", help_text)
        self.update_status("Ayuda mostrada. Revisa la explicación completa.")
    
    def refresh_table(self):
        """Actualiza la tabla con los datos más recientes"""
        self.update_status("Actualizando la tabla de enlaces...")
        
        # Limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        urls = load_urls()
        
        # Insertar datos (ordenados por fecha, más reciente primero)
        sorted_urls = sorted(urls.items(), key=lambda x: x[1]['created_at'], reverse=True)
        
        for code, info in sorted_urls:
            # Acortar URL si es muy larga
            url_display = info['original_url']
            if len(url_display) > 80:
                url_display = url_display[:77] + "..."
            
            self.tree.insert("", tk.END, values=(
                code,
                url_display,
                info['clicks'],
                info['created_at']
            ))
        
        # Actualizar barra de estado
        total = len(urls)
        total_clicks = sum(info['clicks'] for info in urls.values())
        self.update_status(f"Tabla actualizada: {total} enlaces, {total_clicks} clics totales. Selecciona un enlace para verlo o eliminarlo.")

# ========== EJECUTAR ==========
if __name__ == "__main__":
    root = tk.Tk()
    app = URLShortenerApp(root)
    root.mainloop()
