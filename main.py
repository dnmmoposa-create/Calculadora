from tkinter import *
from tkinter import messagebox

# ---------------- Colores Estilo Neumorfismo / Minimalista ----------------
COLOR_FONDO = "#7ebebe"      # Fondo principal ultra oscuro
COLOR_PANTALLA = "#2e4141"   # Fondo de la pantalla
COLOR_TEXTO = "#ffffff"      # Texto blanco
COLOR_NUMEROS = "#2d3838"    # Gris oscuro para números
COLOR_OPERADORES = "#f39c12" # Naranja para operaciones
COLOR_IGUAL = "#27ae60"      # Verde para el resultado
COLOR_HOVER = "#3e4f4f"      # Color al pasar el mouse por encima

# ---------------- Ventana ----------------
ventana = Tk()
ventana.title("Calculadora ")
ventana.geometry("350x520")
ventana.resizable(False, False)
ventana.configure(bg=COLOR_FONDO)

# ---------------- Pantalla ----------------
pantalla = Entry(
    ventana,
    font=("Helvetica", 28),
    bd=0,
    bg=COLOR_PANTALLA,
    fg=COLOR_TEXTO,
    justify="right",
    insertbackground="white" 
)
pantalla.pack(fill=X, padx=20, pady=(30, 15), ipady=10)

def escribir(valor):
    pantalla.insert(END, valor)

def limpiar():
    pantalla.delete(0, END)

def calcular():
    try:
        resultado = eval(pantalla.get())
        # Evitar decimales innecesarios (ej. 5.0 -> 5)
        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)
        pantalla.delete(0, END)
        pantalla.insert(END, str(resultado))
    except:
        messagebox.showerror("Error", "Operación no válida")
        limpiar()

def on_enter(e):
    if e.widget['bg'] != COLOR_OPERADORES and e.widget['bg'] != COLOR_IGUAL:
        e.widget['bg'] = COLOR_HOVER

def on_leave(e, color_original):
    if e.widget['bg'] != COLOR_OPERADORES and e.widget['bg'] != COLOR_IGUAL:
        e.widget['bg'] = color_original

# ---------------- Distribución de Botones ----------------
marco = Frame(ventana, bg=COLOR_FONDO)
marco.pack(pady=10)

botones = [
    ("C", 0, 0), ("/", 0, 1), ("*", 0, 2), ("-", 0, 3),
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("=", 2, 3), # '=' ocupará dos filas verticalmente
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("0", 4, 0), (".", 4, 1)
]

for (texto, fila, columna) in botones:
    if texto in ["/", "*", "-", "+", "C"]:
        bg_color = COLOR_OPERADORES if texto != "C" else "#c0392b" # Rojo suave para limpiar
        fg_color = "white"
    elif texto == "=":
        bg_color = COLOR_IGUAL
        fg_color = "white"
    else:
        bg_color = COLOR_NUMEROS
        fg_color = COLOR_TEXTO

    if texto == "=":
        comando = calcular
    elif texto == "C":
        comando = limpiar
    else:
        comando = lambda t=texto: escribir(t)

    btn = Button(
        marco,
        text=texto,
        width=5,
        height=2,
        font=("Helvetica", 14, "bold"),
        bg=bg_color,
        fg=fg_color,
        bd=0,
        activebackground=COLOR_HOVER,
        activeforeground="white",
        cursor="hand2",
        command=comando
    )
    
    if texto == "=":
        btn.grid(row=fila, column=columna, rowspan=3, sticky="nsew", padx=5, pady=5)
    elif texto == "0":
        btn.grid(row=fila, column=columna, columnspan=1, padx=5, pady=5)
    else:
        btn.grid(row=fila, column=columna, padx=5, pady=5)

    if bg_color == COLOR_NUMEROS:
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", lambda e, bg=bg_color: on_leave(e, bg))

ventana.mainloop()