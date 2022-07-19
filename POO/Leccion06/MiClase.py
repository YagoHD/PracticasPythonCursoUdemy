class Miclase:
    #Valor de todos los objetos de la clase, todos tienen el mismo valor
    variable_clase = "Valor variable clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia #Variable de cada objeto no se comparte el valor

    @staticmethod
    def metodo_estatico():
        print(Miclase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)

# Miclase.metodo_clase()
miObjeto1 = Miclase("variable instancia")
# miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()