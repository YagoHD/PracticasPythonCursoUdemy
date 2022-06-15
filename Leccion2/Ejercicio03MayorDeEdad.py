edadAdulto = 18
edadPersona = int(input("Introduce tu edad: "))

if edadPersona >= edadAdulto:
    print(f"Eres mayor de edad, tienes {edadPersona} años")
else:
    print(f"Eres menor de edad, tienes {edadPersona} años")