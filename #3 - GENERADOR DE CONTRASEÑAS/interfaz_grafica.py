# interfaz_grafica.py
import tkinter as tk
from tkinter import ttk, messagebox
from logica_contraseñas import LogicaContraseñas

class GeneradorContraseñas:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Generador de Contraseñas")

        self.longitud_label = ttk.Label(self.ventana, text="Longitud de la Contraseña:")
        self.longitud_entry = ttk.Entry(self.ventana)
        self.longitud_entry.insert(0, "12")
        self.mayus_checkbox_var = tk.BooleanVar()
        self.mayus_checkbox = ttk.Checkbutton(self.ventana, text="Incluir Mayúsculas", variable=self.mayus_checkbox_var)
        self.nums_checkbox_var = tk.BooleanVar()
        self.nums_checkbox = ttk.Checkbutton(self.ventana, text="Incluir Números", variable=self.nums_checkbox_var)
        self.symbols_checkbox_var = tk.BooleanVar()
        self.symbols_checkbox = ttk.Checkbutton(self.ventana, text="Incluir Símbolos", variable=self.symbols_checkbox_var)
        self.generar_button = ttk.Button(self.ventana, text="Generar Contraseña", command=self.generar_contraseña)
        self.contraseña_generada = tk.StringVar()
        self.contraseña_label = ttk.Label(self.ventana, textvariable=self.contraseña_generada)

        self.longitud_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        self.longitud_entry.grid(row=0, column=1, pady=5, padx=5)
        self.mayus_checkbox.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.nums_checkbox.grid(row=2, column=0, pady=5, padx=5, sticky="w")
        self.symbols_checkbox.grid(row=3, column=0, pady=5, padx=5, sticky="w")
        self.generar_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.contraseña_label.grid(row=5, column=0, columnspan=2, pady=5)

        self.logica = LogicaContraseñas()

    def generar_contraseña(self):
        try:
            longitud = int(self.longitud_entry.get())
            if 8 <= longitud <= 16:
                mayus = self.mayus_checkbox_var.get()
                nums = self.nums_checkbox_var.get()
                symbols = self.symbols_checkbox_var.get()
                self.contraseña_generada.set(self.logica.crear_contraseña(longitud, mayus, nums, symbols))
            else:
                messagebox.showerror("Error", "La longitud de la contraseña debe estar entre 8 y 16 caracteres.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un valor numérico para la longitud.")

    def iniciar_aplicacion(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = GeneradorContraseñas()
    app.iniciar_aplicacion()
