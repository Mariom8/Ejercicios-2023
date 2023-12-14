

""" Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)
 """

from ast import main
from operator import contains
import random

def generar_letra(mayus:bool) -> chr:

    if mayus is False:

        return chr((random.randint(ord('a'), ord('x'))))

    if mayus is True:

        n = random.randint(0,1)

        if n == 0:

            return chr((random.randint(ord('a'), ord('x'))))

        if n == 1:

            return chr((random.randint(ord('A'), ord('X'))))

def generar_numero():

    return str((random.randint(0,9)))

def generar_simbolo() -> chr:

    return chr((random.randint((33), (46))))




def crear_contraseña(longitud:int, mayus:bool, nums:bool, symbols:bool)-> str:

    opciones = []

    if mayus is True:

        opciones.append(1)

    if nums is True:

        opciones.append(2)

    if symbols is True:

        opciones.append(3)
    
    aux = len(opciones)

    
    
    # mayus = 1
    # nums = 2
    # symbols = 3

    contraseña = ""

    for c in range(0, longitud):

        
        if opciones.__contains__(1) and opciones.__contains__(2) and opciones.__contains__(3): # Letras, numeros y simbolos

            randomAux = random.randint(1,3)

            if randomAux == 1:
                
                contraseña += generar_letra(mayus)

            if randomAux == 2:
                 
                 contraseña += generar_numero()

            if randomAux == 3:
                 
                 contraseña += generar_simbolo()

        elif opciones.__contains__(3): # Letras y simbolos

            randomAux = random.randint(1,2)

            if randomAux == 1:
                
                contraseña += generar_letra(mayus)

            if randomAux == 2:
                 
                 contraseña += generar_simbolo()

        elif opciones.__contains__(2): # Letras y numeros

            randomAux = random.randint(1,2)

            if randomAux == 1:
                
                contraseña += generar_letra(mayus)

            if randomAux == 2:
                 
                 contraseña += generar_numero()

        elif opciones.__contains__(1): # Letras mayusculas y minusculas
                
                contraseña += generar_letra(True)

        elif len(opciones) == 0: # Letras minusculas
                
                contraseña += generar_letra(False)
            
        
        

    return contraseña



while True:

    longitud = 0

    mayus = False

    nums = False

    symbols = False

    print(crear_contraseña(longitud, mayus, nums, symbols))
            
        

        


    