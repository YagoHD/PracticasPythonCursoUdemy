# TIPOS bool (BOOLEAN)
miVariable = False
print(miVariable)

miVariable = 3 > 2
print(miVariable)

if miVariable:
    print("El resultado fue verdadero")
else:
    print("El resultado fue falso")

# FUNCION INPUT para procesar la entrada del usuario
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)

# EJERCICIO 3 Califica tu dia
calificacion = int(input("Califica tu dia (del 1 al 10)"))
print("Mi dia estuvo de: ", calificacion)
