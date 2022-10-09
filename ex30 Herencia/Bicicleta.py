from Vehiculo import *


class Bicicleta(Vehiculo):  # clase hijo 2

    def __init__(self, tipo, color, ruedas):
        super().__init__(color, ruedas)
        self._tipo = tipo

    def __str__(self):
        return f'Tipo: {self._tipo} {super().__str__()}'

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo


if __name__ == "__main__":
    b = Bicicleta("Bicicleta", "Blue", 2)
    print(b)
