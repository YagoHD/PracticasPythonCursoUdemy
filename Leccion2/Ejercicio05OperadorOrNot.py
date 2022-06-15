vacaciones = False
diaDescanso = False

if vacaciones or diaDescanso:  # Ni es dia de descanso ni es vacaciones, tienes que trabajar
    print("Puedes asistir al cine")
else:
    print("Tienes que trabajar")
# LOGICA INVERTIDA
if not (vacaciones or diaDescanso):
    print("Tienes que ir a trabajar")
else:
    print("Puedes ir al cine")

vacaciones = True  # Son vacaciones puedes ir al cine
if vacaciones or diaDescanso:
    print("Puedes asistir al cine")
else:
    print("Tienes que trabajar")
# LOGICA INVERTIDA
if not (vacaciones or diaDescanso):
    print("Tienes que ir a trabajar")
else:
    print("Puedes ir al cine")
