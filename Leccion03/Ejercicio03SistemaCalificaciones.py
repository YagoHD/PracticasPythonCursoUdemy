# 9-10 A/8-9 B/7-8 C/6-7 D/0-6 F
calificacionNumerica = int(input("Introduce tu nota: "))
calificacionLetra = None

if calificacionNumerica >= 9 and calificacionNumerica <=10:
    calificacionLetra = "A"
elif calificacionNumerica >= 8 and calificacionNumerica < 9:
    calificacionLetra = "B"
elif calificacionNumerica >= 7 and calificacionNumerica < 8:
    calificacionLetra = "C"
elif calificacionNumerica >= 6 and calificacionNumerica < 7:
    calificacionLetra = "D"
elif calificacionNumerica >= 0 and calificacionNumerica < 6:
    calificacionLetra = "F"
else:
    calificacionLetra = "Valor no reconocido, porporcione uno valido"

print(f"Tu nota {calificacionNumerica}, es un {calificacionLetra}")