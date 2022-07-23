#Leemos la informacion del archivo anteriormente creado
# "r" lectura(modo default) | "a" anexa informacion, añade nueva sin borrar la anterior, crea el archivo si no existe
# "w" escribe informacion, crea el archivo si no existe | "x" crea el archivo y manda excepcion si ya existe
# "t" Texto (default) | "b" Binario

archivo = open("prueba.txt","r", encoding="utf8")
#print(archivo.read())#read nos lee el archivo
#esto esta comentado, por que como ya fue leydo no quedan mas caracteres por leer y no nos dejaria hacer mas pruebas a continuacion


#Leer algunos caracteres
# print((archivo.read(5)))
# print(archivo.read(4))

#Leer lineas completas
# print(archivo.readline())
# print(archivo.readline())

#Iterar el archivo
# for linea in archivo:
#     print(linea)

#Leer lineas nos devuelve una lista
# print(archivo.readlines())

#Acceder solo a una linea de la lista
# print(archivo.readlines()[2])

#Abrimos un nuevo archivo
#a - anexar informacion
archivo2 = open("copia.txt","w", encoding="utf8")
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print("Se ha terminado el proceso de leer y copiar archivos")