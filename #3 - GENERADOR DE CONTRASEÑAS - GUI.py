import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

def generar_letra(mayus: bool) -> chr:
    if mayus is False:
        return chr(random.randint(ord('a'), ord('x')))
    if mayus is True:
        n = random.randint(0, 1)
        if n == 0:
            return chr(random.randint(ord('a'), ord('x')))
        if n == 1:
            return chr(random.randint(ord('A'), ord('X')))

def generar_numero():
    return str(random.randint(0, 9))

def generar_simbolo() -> chr:
    return chr(random.randint(33, 46))

def crear_contraseña(longitud: int, mayus: bool, nums: bool, symbols: bool) -> str:
    opciones = []
    if mayus is True:
        opciones.append(1)
    if nums is True:
        opciones.append(2)
    if symbols is True:
        opciones.append(3)
    aux = len(opciones)

    contraseña = ""
    for c in range(0, longitud):
        if opciones.__contains__(1) and opciones.__contains__(2) and opciones.__contains__(3): 
            randomAux = random.randint(1, 3)
            if randomAux == 1:
                contraseña += generar_letra(mayus)
            if randomAux == 2:
                contraseña += generar_numero()
            if randomAux == 3:
                contraseña += generar_simbolo()
        elif opciones.__contains__(3): 
            randomAux = random.randint(1, 2)
            if randomAux == 1:
                contraseña += generar_letra(mayus)
            if randomAux == 2:
                contraseña += generar_simbolo()
        elif opciones.__contains__(2): 
            randomAux = random.randint(1, 2)
            if randomAux == 1:
                contraseña += generar_letra(mayus)
            if randomAux == 2:
                contraseña += generar_numero()
        elif opciones.__contains__(1): 
            contraseña += generar_letra(True)
        elif len(opciones) == 0: 
            contraseña += generar_letra(False)
    return contraseña

def generar_contraseña():
    try:
        longitud = int(longitud_entry.get())
        if 8 <= longitud <= 16:
            mayus = mayus_checkbox_var.get()
            nums = nums_checkbox_var.get()
            symbols = symbols_checkbox_var.get()
            contraseña_generada.set(crear_contraseña(longitud, mayus, nums, symbols))
        else:
            tk.messagebox.showerror("Error", "La longitud de la contraseña debe estar entre 8 y 16 caracteres.")
    except ValueError:
        tk.messagebox.showerror("Error", "Por favor, introduce un valor numérico para la longitud.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")

# Variables de control
longitud_label = ttk.Label(ventana, text="Longitud de la Contraseña:")
longitud_entry = ttk.Entry(ventana)
longitud_entry.insert(0, "12")  # Valor por defecto
mayus_checkbox_var = tk.BooleanVar()
mayus_checkbox = ttk.Checkbutton(ventana, text="Incluir Mayúsculas", variable=mayus_checkbox_var)
nums_checkbox_var = tk.BooleanVar()
nums_checkbox = ttk.Checkbutton(ventana, text="Incluir Números", variable=nums_checkbox_var)
symbols_checkbox_var = tk.BooleanVar()
symbols_checkbox = ttk.Checkbutton(ventana, text="Incluir Símbolos", variable=symbols_checkbox_var)
generar_button = ttk.Button(ventana, text="Generar Contraseña", command=generar_contraseña)
contraseña_generada = tk.StringVar()
contraseña_label = ttk.Label(ventana, textvariable=contraseña_generada)

# Posicionamiento de widgets
longitud_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")
longitud_entry.grid(row=0, column=1, pady=5, padx=5)
mayus_checkbox.grid(row=1, column=0, pady=5, padx=5, sticky="w")
nums_checkbox.grid(row=2, column=0, pady=5, padx=5, sticky="w")
symbols_checkbox.grid(row=3, column=0, pady=5, padx=5, sticky="w")
generar_button.grid(row=4, column=0, columnspan=2, pady=10)
contraseña_label.grid(row=5, column=0, columnspan=2, pady=5)

# Bucle principal
ventana.mainloop()
