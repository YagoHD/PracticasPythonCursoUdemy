from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

teclado1 = Teclado("HP", "USB")
raton1 = Raton("HP", "USB")
monitor1 = Monitor("Asus", 15)
computadora1 = Computadora("HP", monitor1, teclado1, raton1)

teclado2 = Teclado("Acer", "Bluetooth")
raton2 = Raton("Acer", "USB")
monitor2 = Monitor("Asus", 27)
computadora2 = Computadora("Acer", monitor2, teclado2, raton2)

teclado3 = Teclado("Gamer", "Bluetooth")
raton3 = Raton("Gamer", "Bluetooth")
monitor3 = Monitor("Gamer", 40)
computadora3 = Computadora("Gamer", monitor3, teclado3, raton3)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)

orden1.agregar_computadora(computadora3)
print(orden1)

computadoras2 = [computadora2, computadora3]
orden2 = Orden(computadoras2)
print(orden2)