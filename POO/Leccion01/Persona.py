# CREAR CLASE Y MÉTODOS:
class Persona:
    # ATRIBUTOS QUE TENDRA LA CLASE
    def __init__(self, nombre, apellido, edad, *args, **kwargs): #*args->TUPLA  **kwargs->DICCIONARIO
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = args
        self.terminos = kwargs

    # CREACION DE METODOS
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido}, tienes {self.edad} años")


# INSTANCIAR OBJETOS:
persona1 = Persona("Yago", "Ramos", 23)
persona2 = Persona("Xiada", "Venn", 22, 2,2,5,4, m="manzana", p="pera")

# MOSTRAR ATRIBUTOS MANUALMENTE Y CON METODO mostrar_detalle
print("Hola:", persona1.nombre, persona1.apellido, "tienes", persona1.edad, "años")
persona2.mostrar_detalle() #SE PUEDE HACER ASI DIRECTAMENTE CON EL OBJETO PERSONA 2
Persona.mostrar_detalle(persona2) #PERO TAMBIEN ASI CON LA CLASE PERSONA Y ESPECIFICAR EL OBJETO PERSONA2

# MODIFICAR ATRIBUTOS DE UN OBJETO:
persona1.nombre = "YagoRB"
persona1.apellido = "Ramos Bermúdez"
persona1.telefono = 678927000 # SE CREA UN ATRIBUTO PERO SOLO!!!! PARA PERSONA1
print("Hola:", persona1.nombre, persona1.apellido, "tienes", persona1.edad, "años, telefono ->", persona1.telefono, "Tupla:",persona2.valores, "Diccionario FRUTAS:",persona2.terminos)
