class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.nombre}, {self.edad} años"

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f"Empleado: [Sueldo: {self.sueldo}] [Persona: {self.nombre}, {self.edad} años]"

if __name__ == "__main__":
    empleado1 = Empleado("Yago",23, 5000)
    print(empleado1.nombre)
    print(empleado1.edad)
    print(empleado1.sueldo)