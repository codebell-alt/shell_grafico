import tkinter as tk
from PIL import Image, ImageTk
import subprocess

# Funciones para abrir aplicaciones del sistema
def abrir_navegador():
    subprocess.Popen(['firefox'])

def abrir_editor():
    subprocess.Popen(['gedit'])

def abrir_terminal():
    subprocess.Popen(['gnome-terminal'])

# Configuración de la ventana principal
root = tk.Tk()
root.title("Mi Escritorio")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg="white")  # Fondo blanco

# Cargar y mostrar la imagen de fondo
fondo_img = Image.open("fondo.png")
fondo_img = fondo_img.resize((600, 500), Image.LANCZOS)
fondo_photo = ImageTk.PhotoImage(fondo_img)
fondo_label = tk.Label(root, image=fondo_photo, borderwidth=0, highlightthickness=0)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Función para mostrar un título con sombra
def titulo_con_sombra(parent, texto, font, color_texto, color_sombra, x, y):
    # Sombra (ligeramente desplazada)
    sombra = tk.Label(
        parent,
        text=texto,
        font=font,
        fg=color_sombra,
        bg="white"
    )
    sombra.place(relx=0.5, y=y+2, anchor="center")
    # Título principal
    titulo = tk.Label(
        parent,
        text=texto,
        font=font,
        fg=color_texto,
        bg="white"
    )
    titulo.place(relx=0.5, y=y, anchor="center")

# Mostrar el título principal con sombra
titulo_con_sombra(
    root,
    "Bienvenido a tu Escritorio",
    ("Segoe UI", 22, "bold"),
    "#ffb347",      # Color principal (dorado suave)
    "#888888",      # Color sombra (gris oscuro)
    0.5,
    50
)

# Función para cargar y redimensionar iconos PNG
def cargar_icono(nombre_archivo):
    img = Image.open(nombre_archivo)
    img = img.resize((64, 64), Image.LANCZOS)
    return ImageTk.PhotoImage(img)

# Cargar los iconos de las aplicaciones
icono_nav = cargar_icono("icono_navegador.png")
icono_edit = cargar_icono("icono_editor.png")
icono_term = cargar_icono("icono_terminal.png")

# Función para crear un icono con texto y sombra
def crear_icono(parent, imagen, texto, comando, color):
    frame = tk.Frame(parent, borderwidth=0, highlightthickness=0, bg="white")
    # Botón con el icono
    btn = tk.Button(
        frame,
        image=imagen,
        command=comando,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        cursor="hand2",
        bg="white",
        activebackground="white"
    )
    btn.pack()
    # Sombra para el texto del icono
    sombra = tk.Label(
        frame,
        text=texto,
        font=("Segoe UI", 13, "bold"),
        fg="#888888",
        bg="white"
    )
    sombra.pack(pady=(5, 0))
    sombra.place(x=2, y=btn.winfo_reqheight()+7)  # Ajusta la sombra
    # Texto principal del icono
    lbl = tk.Label(
        frame,
        text=texto,
        font=("Segoe UI", 13, "bold"),
        fg=color,
        bg="white"
    )
    lbl.pack(pady=(5, 0))
    return frame

# Frame para centrar los iconos en la ventana
iconos_frame = tk.Frame(root, borderwidth=0, highlightthickness=0, bg="white")
iconos_frame.place(relx=0.5, rely=0.55, anchor="center")

# Crear los iconos de las aplicaciones
icono1 = crear_icono(iconos_frame, icono_nav, "Navegador Web", abrir_navegador, "#ff7043")
icono2 = crear_icono(iconos_frame, icono_edit, "Editor de Texto", abrir_editor, "#43a047")
icono3 = crear_icono(iconos_frame, icono_term, "Terminal", abrir_terminal, "#42a5f5")

# Distribuir los iconos horizontalmente
icono1.pack(side="left", padx=35, pady=10)
icono2.pack(side="left", padx=35, pady=10)
icono3.pack(side="left", padx=35, pady=10)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()