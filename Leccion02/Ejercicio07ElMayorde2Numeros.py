numero1 = int(input("Introduce un numero: "))
numero2= int(input("Introdice un numero: "))

if numero1 > numero2:
    print(f"El {numero1} es mayor")
elif numero2 > numero1:
    print(f"El {numero2} es mayor")
else:
    print(f"Los numeros {numero1} y {numero2}, som iguales")