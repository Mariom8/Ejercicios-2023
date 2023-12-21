

# /*
#  * Crea un programa capaz de interactuar con un fichero TXT.
#  * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección. 
#  * Únicamente el código.
#  * 
#  * - Si no existe, debe crear un fichero llamado "text.txt".
#  * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
#  *   en una nueva línea cada vez que se pulse el botón "Enter".
#  * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
#  *   a continuación o borrar su contenido y comenzar desde el principio.
#  * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
#  *   el texto que ya posee el fichero.  
#  */


import os

archivo_txt = "texto_prueba.txt"

# Verificar si el archivo existe
if os.path.exists(archivo_txt):
    print(f"El archivo {archivo_txt} ya existe.")

    opcion = input(f"Si desea seguir escribiendo a continuación pulse 'S', de lo contrario pulse 'N' y se borrará el contenido: ")

    if opcion == 'S':
        
        with open(archivo_txt, 'r') as archivo:

            for linea in archivo:

                print(linea)

        print()
        

        while True:

            texto = input("Escribe el texto a introducir y pulse 'Enter' para continuar. Escribe 'end' para salir del programa.")

            if texto == 'end':

                exit()

            with open(archivo_txt, 'a') as archivo:
                archivo.write("\n"+texto)
            
    if opcion == 'N':

        with open(archivo_txt, 'w') as archivo:
            archivo.write("")

            print(f"Contenido del archivo {archivo_txt} borrado.")

        while True:

            texto = input("Escribe el texto a introducir y pulse 'Enter' para continuar. Escribe 'end' para salir del programa.")

            if texto == 'end':

                exit()

            with open(archivo_txt, 'a') as archivo:
                archivo.write("\n"+texto)




else:
    # Crear el archivo si no existe
    with open(archivo_txt, 'w') as archivo:
        print(f"Se ha creado el archivo {archivo_txt}.")

    while True:

            texto = input("Escribe el texto a introducir y pulse 'Enter' para continuar. Escribe 'end' para salir del programa.")

            if texto == 'end':

                exit()

            with open(archivo_txt, 'a') as archivo:
                archivo.write("\n"+texto)

