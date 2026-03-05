import tkinter as tk
from tkinter import ttk
import math

# ---------------- CONFIGURACIÓN DE COLORES ----------------
BG_PRINCIPAL = "#1e1e1e"      # Fondo general oscuro
BG_SECUNDARIO = "#2a2a2a"     # Fondo intermedio
BG_ENTRADA = "#333333"        # Fondo de entradas
COLOR_TEXTO = "#ECDDDD"       # Blanco suave
COLOR_ZEBRA_1 = "#2f2f2f"
COLOR_ZEBRA_2 = "#3a3a3a"

historial_contador = 0

# ---------------- FUNCIONES PRINCIPALES ----------------
def limpiar():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    label_result.config(text="Resultado:")

def borrar_historial():
    for item in historial_tabla.get_children():
        historial_tabla.delete(item)

def formatear_numero(n):
    if isinstance(n, float):
        return round(n, 4)
    return n

def actualizar_historial(op, a, b, resultado):
    global historial_contador

    tag = "par" if historial_contador % 2 == 0 else "impar"

    historial_tabla.insert(
        "",
        "end",
        values=(op, formatear_numero(a), formatear_numero(b), formatear_numero(resultado)),
        tags=(tag,)
    )

    historial_contador += 1

def ejecutar_operacion(event=None):
    opcion = combo.get()

    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        operaciones = {
            "Suma": lambda a,b: a+b,
            "Resta": lambda a,b: a-b,
            "Multiplicación": lambda a,b: a*b,
            "División": lambda a,b: a/b,
            "Potencia": lambda a,b: a**b,
            "Modulo": lambda a,b: a%b,
            "Promedio": lambda a,b: (a+b)/2,
            "Máximo": lambda a,b: max(a,b),
            "Mínimo": lambda a,b: min(a,b),
            "Porcentaje (A de B)": lambda a,b: (a*b)/100,
        }

        operaciones_unarias = {
            "Raíz de A": lambda a: math.sqrt(a),
            "Valor absoluto A": lambda a: abs(a),
            "Redondear A": lambda a: round(a),
            "A²": lambda a: a**2,
            "Log(A)": lambda a: math.log(a),
            "Log10(A)": lambda a: math.log10(a),
            "Seno(A)": lambda a: math.sin(math.radians(a)),
            "Coseno(A)": lambda a: math.cos(math.radians(a)),
            "Tangente(A)": lambda a: math.tan(math.radians(a)),
            "Factorial(A)": lambda a: math.factorial(int(a)),
            "Exp(A)": lambda a: math.exp(a),
        }

        if opcion in operaciones:
            resultado = operaciones[opcion](a,b)
        elif opcion in operaciones_unarias:
            resultado = operaciones_unarias[opcion](a)
        else:
            resultado = "?"

        label_result.config(text=f"Resultado: {formatear_numero(resultado)}")
        actualizar_historial(opcion, a, b, resultado)

    except ZeroDivisionError:
        label_result.config(text="No se puede dividir por 0")
    except ValueError:
        label_result.config(text="Ingresá números válidos")
    except Exception:
        label_result.config(text="Error inesperado")

# ---------------- VENTANA ----------------
win = tk.Tk()
win.title("Calculadora")
win.geometry("620x720")
win.configure(bg=BG_PRINCIPAL)
win.iconbitmap(r"C:\Users\User\Desktop\M\proyectos _ programación- Python\Calculadora\Iconos\icono_ventana.ico")

main_frame = tk.Frame(win, bg=BG_PRINCIPAL, padx=25, pady=25)
main_frame.pack(fill="both", expand=True)

# ---------------- ESTILO ttk ----------------
style = ttk.Style()
style.theme_use("clam")

style.configure("TCombobox",
                fieldbackground=BG_ENTRADA,
                background=BG_SECUNDARIO,
                foreground=COLOR_TEXTO)

style.configure("TButton",
                background=BG_SECUNDARIO,
                foreground=COLOR_TEXTO)

style.configure("Treeview",
                background=BG_SECUNDARIO,
                fieldbackground=BG_SECUNDARIO,
                foreground=COLOR_TEXTO)

style.configure("Treeview.Heading",
                background=BG_ENTRADA,
                foreground=COLOR_TEXTO)

# ---------------- ENTRADAS ----------------
tk.Label(main_frame, text="Número A", bg=BG_PRINCIPAL, fg=COLOR_TEXTO).pack()
entry_a = tk.Entry(main_frame, bg=BG_ENTRADA, fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO, relief="flat")
entry_a.pack(fill="x", pady=6)

tk.Label(main_frame, text="Número B", bg=BG_PRINCIPAL, fg=COLOR_TEXTO).pack()
entry_b = tk.Entry(main_frame, bg=BG_ENTRADA, fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO, relief="flat")
entry_b.pack(fill="x", pady=6)

# ----- estilo especial para el combobox -----
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "ComboCalculadora.TCombobox",
    fieldbackground="#2f2f2f",   # fondo del campo
    background="#2f2f2f",
    foreground="#303030",        # texto visible
    arrowcolor="#FFFFFF"
)

# color de la lista desplegable
win.option_add("*TCombobox*Listbox.background", "#2f2f2f")
win.option_add("*TCombobox*Listbox.foreground", "#ffffff")
win.option_add("*TCombobox*Listbox.selectBackground", "#555555")
win.option_add("*TCombobox*Listbox.selectForeground", "#ffffff")

# ----- combobox -----
combo = ttk.Combobox(
    main_frame,
    values=[
        "Suma","Resta","Multiplicación","División",
        "Potencia","Modulo","Promedio",
        "Máximo","Mínimo","Porcentaje (A de B)",
        "Raíz de A","Valor absoluto A",
        "Redondear A","A²",
        "Log(A)","Log10(A)",
        "Seno(A)","Coseno(A)","Tangente(A)",
        "Factorial(A)","Exp(A)"
    ],
    state="readonly",
    style="ComboCalculadora.TCombobox"
)

combo.pack(fill="x", pady=15)
combo.set("Elegí una opción")
# ---------------- BOTONES ----------------
btn_frame = tk.Frame(main_frame, bg=BG_PRINCIPAL)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="Calcular", command=ejecutar_operacion).grid(row=0,column=0,padx=6)
ttk.Button(btn_frame, text="Limpiar", command=limpiar).grid(row=0,column=1,padx=6)
ttk.Button(btn_frame, text="Borrar historial", command=borrar_historial).grid(row=0,column=2,padx=6)

# ---------------- RESULTADO ----------------
label_result = tk.Label(main_frame, text="Resultado:",
                        font=("Segoe UI", 13, "bold"),
                        bg=BG_PRINCIPAL, fg=COLOR_TEXTO)
label_result.pack(pady=15)

# ---------------- HISTORIAL ----------------
tk.Label(main_frame, text="Historial", bg=BG_PRINCIPAL, fg=COLOR_TEXTO).pack(pady=(20,8))

columns = ("Operacion", "A", "B", "Resultado")

historial_tabla = ttk.Treeview(main_frame, columns=columns,show="headings",height=12)

for col in columns:
    historial_tabla.heading(col, text=col)
    historial_tabla.column(col, anchor="center", width=140)

historial_tabla.tag_configure("par", background=COLOR_ZEBRA_1)
historial_tabla.tag_configure("impar", background=COLOR_ZEBRA_2)

historial_tabla.pack(fill="both", expand=True)

# ---------------- ENTER ----------------
win.bind("<Return>", ejecutar_operacion)

win.mainloop()