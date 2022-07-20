from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))

empleado = Empleado("Yago",5000)
imprimir_detalles(empleado)

gerente = Gerente("Xiada",3000,"Fotografia")
imprimir_detalles(gerente)