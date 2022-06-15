valorNumerico = int(input("Introduce un numero: "))
valorMinimo = 0
valorMaximo = 5

dentroRango = valorNumerico >= valorMinimo and valorNumerico <= valorMaximo

if dentroRango:
    print(f"El numero {valorNumerico}, esta dentro de rango")
else:
    print(f"El numero {valorNumerico}, esta fuera de rango")