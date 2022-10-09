from Vehiculo import *


class Coche(Vehiculo): #clase hijo 1

    def __init__(self, velocidad, color, ruedas):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    def __str__(self):
        return f'Coche=> Velocidad : {self._velocidad} km/h {super().__str__()}'

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad


if __name__ == "__main__":
    c = Coche(100, "Rojo", 4)
    print(c)
    print("set")
    c.color = "Amarillo"
    c.velocidad = 20
    print(c)
