# Ejercicio 1. Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
print("Iterar un rango de 0 a 10 e imprimir números divisibles entre 3")
for celda in range(11):
    if celda % 3 == 0:
        print(celda)
# Ejercicio 2. Crear un rango de numeros de 2 a 6, e imprimelos
print("Crear un rango de numeros de 2 a 6, e imprimelos")
rango = range(2, 7)
for celda in rango:
    print(celda)
# Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1
print("Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1")
rango = range(3, 11, 2)
for celda in rango:
    print(celda)
