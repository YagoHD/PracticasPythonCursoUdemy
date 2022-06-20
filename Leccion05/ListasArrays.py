# Definir la lista de nombres
nombres = ["Juan", "Carla", "Ricardo", "Maria"]
# Imrprimir la lista de nombres
print(nombres)
# Acceder de forma individual
print(nombres[0])
print(nombres[1])
# Acceder de forma individual a la inversa
print(nombres[-1])
print(nombres[-2])
# Acceder a un rango sin incluir el indice 2
print(nombres[0:2])
# Acceder a un rango  desde el inicio sin incluir el iondice final
print(nombres[:3])
# Acceder a un rango  desde el indice hasta el final incluyendo el indice
print(nombres[1:])
# Cambiar un valor
nombres[3] = "Ivan"
print(nombres)
# Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("No existen mas nombres en la lista")
# Preguntar el largo de una lista
print(len(nombres))
# Agregar un elemento a la lista
nombres.append("Pepe")
print(nombres)
# Insertar un nombre en un indice en concreto
nombres.insert(1, "Manolo")
print(nombres)
# Borrar un elemento
nombres.remove("Manolo")
print(nombres)
# Borrar el ultimo valor agregado
nombres.pop()
print(nombres)
# Borrar en un indice indicado
del nombres[0]
print(nombres)
# Limpiar lista
nombres.clear()
print(nombres)
# Borrar la lista por completo
del nombres
# print(nombres) ESTO DARIA ERROR POR QUE NO EXISTE ESTA LISTA AL HABERLA BORRADO
