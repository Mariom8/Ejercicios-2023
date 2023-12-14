# logica_contraseñas.py
import random

class LogicaContraseñas:

    @staticmethod
    def generar_letra(mayus: bool) -> chr:

        if not mayus:

            return chr(random.randint(ord('a'), ord('x')))
        
        return chr(random.randint(ord('a'), ord('x'))) if random.randint(0, 1) == 0 else chr(random.randint(ord('A'), ord('X')))

    @staticmethod
    def generar_numero():

        return str(random.randint(0, 9))

    @staticmethod
    def generar_simbolo() -> chr:

        return chr(random.randint(33, 46))

    def crear_contraseña(self, longitud: int, mayus: bool, nums: bool, symbols: bool) -> str:

        opciones = []

        if mayus:

            opciones.append(1)

        if nums:

            opciones.append(2)

        if symbols:

            opciones.append(3)

        contraseña = ""

        for _ in range(longitud):

            if 1 in opciones and 2 in opciones and 3 in opciones: # Letras, numeros y simbolos

                random_aux = random.randint(1, 3)

                if random_aux == 1:

                    contraseña += self.generar_letra(mayus)

                elif random_aux == 2:

                    contraseña += self.generar_numero()

                elif random_aux == 3:

                    contraseña += self.generar_simbolo()

            elif 1 not in opciones and 2 in opciones and 3 in opciones: # Numeros y simbolos

                random_aux = random.randint(1, 3)

                if random_aux == 1:

                    contraseña += self.generar_letra(mayus)

                elif random_aux == 2:

                    contraseña += self.generar_numero()

                elif random_aux == 3:

                    contraseña += self.generar_simbolo()
                    

            elif opciones.__contains__(3): # Letras y simbolos

                random_aux = random.randint(1, 2)
                if random_aux == 1:

                    contraseña += self.generar_letra(mayus)

                elif random_aux == 2:

                    contraseña += self.generar_simbolo()

            elif opciones.__contains__(2): 

                random_aux = random.randint(1, 2)

                if random_aux == 1:

                    contraseña += self.generar_letra(mayus)

                elif random_aux == 2:

                    contraseña += self.generar_numero()

            elif opciones.__contains__(1): 

                contraseña += self.generar_letra(True)

            elif len(opciones) == 0: 

                contraseña += self.generar_letra(False)

        return contraseña
