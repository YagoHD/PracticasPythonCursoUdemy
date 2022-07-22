#CREAMOS NUESTRA PROPIA EXCEPCION

class NumerosIdenticosException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje