class cubo:
    def __init__(self, altura, anchura, profundidad):
        self.anchura = anchura
        self.altura = altura
        self.profundidad = profundidad

    def calculaVolumen(self):
        return self.altura * self.anchura * self.profundidad

altura = int(input("Proporciona la altura: "))
anchura = int(input("Proporciona la anchura: "))
profundidad = int(input("Proporciona la profundidad: "))

cubo1 = cubo(altura, anchura, profundidad)

print(f"Volumen: {cubo1.calculaVolumen()}")