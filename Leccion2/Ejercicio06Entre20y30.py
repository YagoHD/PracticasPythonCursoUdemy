edad = int(input("Introduce tu edad: "))

veintes = edad>=20 and edad<=30
print(veintes)
treintas = edad >=30 and edad <40
print(treintas)

if veintes or treintas:
    print("Dentro de rango (20's) o (30's)")
    if veintes: # IF ANIDADO
        print("Dentro de los 20's")
    elif treintas: # IF ANIDADO
        print("Dentro de los 30's")
else:
    print("Fuera de los (20's) o (30's)")

# EL MODO MAS SIMPLIFICADO Y OPTIMO DE REALIZAR EL EJERCIICO
if (20 <= edad < 30) or (30 <= edad < 40):
    print("Dentro de rango (20's) o (30's)")
    if (20 <= edad < 30): # IF ANIDADO
        print("Dentro de los 20's")
    elif (30 <= edad < 40): # IF ANIDADO
        print("Dentro de los 30's")
else:
    print("Fuera de los (20's) o (30's)")