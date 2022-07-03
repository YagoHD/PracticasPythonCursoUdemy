from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("Creacion objeto cuadrado".center(50,"-"))
cuadrado1 = Cuadrado(lado= 5, color= "rojo")
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
# print(cuadrado1.color)
cuadrado1.alto = 9
cuadrado1.ancho = 9
print("Calculo area cuadrado:",cuadrado1.calcular_area())
print(cuadrado1)
#MRO - Method Resolution Order
print(Cuadrado.mro())
print()
print("Creacion objeto rectangulo".center(50,"-"))
rectangulo1 = Rectangulo(ancho=9,alto=8,color= "verde")
print("Calculo area rectangulo:",rectangulo1.calcular_area())
print(rectangulo1)