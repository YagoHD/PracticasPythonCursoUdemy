class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"[Vehiculo: color->{self.color}, {self.ruedas}->ruedas]"

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f"[Coche: velocidad->{self.velocidad}] [Vehiculo: color->{self.color}, {self.ruedas}->ruedas]"

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"[Bicibleta: tipo->{self.tipo}] [Vehiculo: color->{self.color}, {self.ruedas}->ruedas]"
