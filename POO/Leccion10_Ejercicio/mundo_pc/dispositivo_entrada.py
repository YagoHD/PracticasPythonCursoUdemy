class DispositivoEntrada:
    def __init__(self, marca, tipo_entrada):
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    @property
    def tipo_entrada(self):
        return f"Tipo entrada: {self._tipo_entrada}"

    @property
    def marca(self):
        return f"Marca: {self._marca}"

    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self._tipo_entrada = tipo_entrada

    @marca.setter
    def marca(self, marca):
        self._marca = marca