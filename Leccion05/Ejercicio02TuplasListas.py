# Dada la siguiente tupla,
# crear una lista que sólo incluya los números menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)
# PRIMERO CREAMOS LA LISTA
lista = []
# AHORA FILTRAMOS LOS ELEMENTOS A PASAR A LA LISTA SOLO LOS MENORES DE 5
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)

print(lista)
