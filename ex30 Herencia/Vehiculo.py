class Vehiculo: #Clase padre

    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        return f'Color: {self._color}, Ruedas: {self._ruedas}'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return self._ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas


if __name__ == "__main__":
    v = Vehiculo("Rojo", 4)
    print(v.color)
    print(v.ruedas)
    print(v)
    print("set")
    v.color = "Amarillo"
    print(v)
