
# /*
#  * Crea un programa que analice texto y obtenga:
#  * - Número total de palabras.
#  * - Longitud media de las palabras.
#  * - Número de oraciones del texto (cada vez que aparecen un punto).
#  * - Encuentre la palabra más larga.
#  *
#  * Todo esto utilizando un único bucle.
#  */



texto = input(print("Introduce el texto a analizar:"))


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

#print(dicc)




key_list = list(dicc.keys())
value_list = list(dicc.values())  # Convertir a lista

lista_resultados = []

valor_a_buscar = max(value_list)

for i in range(len(dicc)):

    if value_list[i] == valor_a_buscar:

        lista_resultados.append(key_list[i])


print("Palabra/s mas larga:", lista_resultados, "caracteres =", valor_a_buscar)









