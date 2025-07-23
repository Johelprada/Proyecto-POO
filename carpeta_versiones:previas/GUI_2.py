"""
import tkinter as tk

interfaz = tk.Tk()
interfaz.title("ARCHIVADOR 3.000")
interfaz.geometry("680x500")

# Hacemos que la raíz use grid y se expanda
interfaz.grid_rowconfigure(0, weight=1)
interfaz.grid_columnconfigure(0, weight=1)

pantalla_inicio = tk.Frame(interfaz)
pantalla_dos = tk.Frame(interfaz)

for f in (pantalla_inicio, pantalla_dos):
    f.grid(row=0, column=0, sticky="nsew")

# --- Pantalla inicio ---
titulo = tk.Label(pantalla_inicio, text="Ingresar datos")
titulo.pack(pady=10)

entrada = tk.Entry(pantalla_inicio, width=30)
entrada.pack(pady=10)

etiqueta = tk.Label(pantalla_inicio, text="")
etiqueta.pack(pady=5)

def mostrar_texto():
    etiqueta.config(text=f"Escribiste: {entrada.get()}")

def ir_a_pantalla_dos():
    pantalla_dos.tkraise()

boton = tk.Button(pantalla_inicio, text="Mostrar texto", command=mostrar_texto)
boton.pack(pady=5)

boton2 = tk.Button(pantalla_inicio, text="Ir a pantalla 2", command=ir_a_pantalla_dos)
boton2.pack(pady=5)

# --- Pantalla dos ---
tk.Label(pantalla_dos, text="Esta es la pantalla 2").pack(pady=20)
tk.Button(pantalla_dos, text="Volver", command=lambda: pantalla_inicio.tkraise()).pack()

# Mostrar inicialmente la pantalla de inicio
pantalla_inicio.tkraise()

interfaz.mainloop()

"""
"""
#__pantalla_2:REGISTRO
boton_exportar = tk.Button(Window, text="Exportar a CSV",command="")
boton_exportar.pack(pady=5)

boton_descargar_registro = tk.Button(Window, text="Exportar a CSV",command="")
boton_exportar.pack(pady=5)

boton_guardar_registro = tk.Button(Window, text="Exportar a CSV",command="")
boton_exportar.pack(pady=5)

boton_agregar_nota = tk.Button(Window, text="Exportar a CSV",command="")
boton_exportar.pack(pady=5)

boton_agregar_cambio = tk.Button(Window, text="Exportar a CSV",command="")
boton_exportar.pack(pady=5)

boton_agregar_cambio = tk.Button(Window, text="Exportar a CSV",command="")
boton_exportar.pack(pady=5)

boton_agregar_paquete = tk.Button(Window, text="Exportar a CSV",command="")
boton_exportar.pack(pady=5)
"""
