# CREAR CLASE Y MÉTODOS:
class Persona:
    # ATRIBUTOS QUE TENDRA LA CLASE
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

        #SE PONE EL GUION BAJO PARA INDICAR QUE SE RESTRINGE EL ACCESO AL ATRIBUTO, Y DOBLE GUION BAJO PARA RESTRINGIRLO
        #DEL TO DO, AUNQUE NO SE SUELE UTILIZAR

    # CREACION DE METODOS
    def mostrar_detalle(self):
        print(f"Persona: {self._nombre} {self._apellido}, tienes {self._edad} años")

    #PONEMOS PROPERTY PARA PODER ACCEDER UNICAMENTE AL ATRIBUTO CON EL SIGUIENTE METODO, Y SE PUEDE ACCEDER A EL COMO
    # SI SE TRATASE DE UN ATRIBUTO, SIN LOS PARENTESIS
    @property
    def nombre(self):
        print("LLAMANDO METODO GET NOMBRE")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print("LLAMANDO METODO SET NOMBRE")
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f"Persona: {self._nombre} {self._apellido} {self._edad}")

    def __del__(self):
        print(f"Persona: {self._nombre} {self._apellido} eliminado")
# INSTANCIAR OBJETOS:
if __name__ == "__main__":
    persona1 = Persona("Yago", "Ramos", 23)
    persona2 = Persona("Xiada", "Venn", 22)
    print(persona1.nombre, persona1.apellido, persona1.edad)
    persona1.nombre = "YaGo"
    print(persona1.nombre)
    persona2.mostrar_detalle()
    persona2.edad = 30
    persona2.mostrar_detalle()
    print(__name__)
#SI QUEREMOS UN ATRIBUTO DE SOLO LECTURA LE QUITAMOS LE METODO "SET" Y AL ATRIBUTO LO LLAMAMOS self._nombre