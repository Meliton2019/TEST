import tkinter as tk
from tkinter import messagebox

# Función que se ejecuta al hacer clic en el botón
def mostrar_texto():
    texto = entrada.get()
    etiqueta_resultado.config(text=f"Has escrito: {texto}")
def gay_texto():
    gay.config(text=f"SI")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Diablo Loco")
ventana.geometry("1080x1910")  # Tamaño de la ventana

# Crear widgets
etiqueta = tk.Label(ventana, text="Escribe algo:")
etiqueta.pack(pady=5)

entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

boton = tk.Button(ventana, text="Mostrar", command=mostrar_texto)
boton.pack(pady=5)

boton = tk.Button(ventana, text="¿Soy Gay?", command=gay_texto)
boton.pack(pady=5)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

gay = tk.Label(ventana, text="")
gay.pack(pady=1)

# Iniciar el bucle principal
ventana.mainloop()
