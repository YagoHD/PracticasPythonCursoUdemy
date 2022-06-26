class rectangulo:
    def __init__(self, altura, ancho):
        self.altura = altura
        self.ancho = ancho

    def calculaArea(self):
        return self.ancho * self.altura


altura = int(input("Introduce el alto: "))
ancho = int(input("Introduce el ancho: "))
rectangulo1 = rectangulo(altura,ancho)

print(f"Area: {rectangulo1.calculaArea()}")