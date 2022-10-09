from FiguraGeometrica import *
from color import *

class Cuadrado(FiguraGeometrica,Color): #Importa el orden

    def __init__(self,lado,color):
        FiguraGeometrica.__init__(self,lado,lado)
        color.__init__(self,color)
        self._color = color
        self._lado = lado

    def __str__(self):
        return f'Clase cuadrado lado {self._lado} {FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

    def calcularArea(self): #metodo abstraacto que debe ser implementado en las clases hijas como esta
        return self._alto * self._ancho

