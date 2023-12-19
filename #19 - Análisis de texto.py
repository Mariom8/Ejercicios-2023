
# /*
#  * Crea un programa que analice texto y obtenga:
#  * - Número total de palabras.
#  * - Longitud media de las palabras.
#  * - Número de oraciones del texto (cada vez que aparecen un punto).
#  * - Encuentre la palabra más larga.
#  *
#  * Todo esto utilizando un único bucle.
#  */






texto = "Este es un ejemplo, con algunas palabras. Y también tiene puntos."


palabras = texto.split()

resultado = [elemento.strip(",") for elemento in palabras]

oraciones = 0

for palabra in resultado:

    if palabra.__contains__("."):

        oraciones += 1
    
print("Número de oraciones del texto:", oraciones, "\n")

numero_palabras = len(resultado)

print("Número total de palabras:", numero_palabras, "\n")

total = 0

for palabra in resultado:

    total = total + len(palabra)

media = total/numero_palabras

media = round(media)


print("Longitud media de las palabras:", media, "\n")



resultado2 = [elemento.strip(".,") for elemento in palabras]

longitud = 0
i = 0

dicc = dict()

for palabra in resultado2:

    dicc[palabra] = len(palabra)

print(dicc)



key_list = dicc.keys()
value_list = dicc.values()

valor_a_buscar = max(value_list)
print(valor_a_buscar)



for i in range(len(dicc)):

    if value_list[i] == valor_a_buscar:

        print(key_list[i])







