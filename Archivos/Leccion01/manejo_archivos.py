#Primero abrimos un archivo
#open: 1 abre un archivo ya existente, 2 si no existe lo crea, se le puede indicar que sea para leer o para escribir
#el encoding utf8 es opcional, en este caso lo puse para que soportara acentos
try:
    archivo = open("prueba.txt", "w", encoding="utf8")

    #write escribe informacion
    archivo.write("Agregamos información al archivo\n")
    archivo.write("Adios")
except Exception as e:
    print(e)
finally:
    #A partir de aqui, que lo cerramos ya no podemos trabajar con el archivo
    archivo.close()
    print("Fin del archivo")
    #Se cierra siempre ya que esta en el finally, haya excepciones o no en el try



# "r" lectura(modo default) | "a" anexa informacion, añade nueva sin borrar la anterior, crea el archivo si no existe
# "w" escribe informacion, crea el archivo si no existe | "x" crea el archivo y manda excepcion si ya existe
# "t" Texto (default) | "b" Binario