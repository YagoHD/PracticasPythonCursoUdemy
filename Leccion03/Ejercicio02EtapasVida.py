# Este ejercicio nos dice que porporcionemos una edad y nos respondera con un mensaje personalizado

edad = int(input("Proporciona tu edad: "))

if edad >= 0 and edad < 10:
    print("La infancia es increible")
elif edad >= 10 and edad < 20:
    print("Etapa educativa en la vida")
elif edad >= 20 and edad < 30:
    print("Amor, dinero y vida adulta")
else:
    print("Etapa de vida no reconocida")
