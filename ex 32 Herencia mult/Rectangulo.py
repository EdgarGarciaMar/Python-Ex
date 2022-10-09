from FiguraGeometrica import *
from color import *

class Rectangulo(FiguraGeometrica,Color):

    def __init__(self,base,altura,color):
        FiguraGeometrica.__init__(self,base,altura)
        Color.__init__(self,color)
        self._base = base
        self._altura = altura
        self._color = color

    def __str__(self):
        return f'Clase Rectangulo Base: {self._base}, altura:  {self._altura} {FiguraGeometrica.__str__(self)} {Color.__str__(self)}'


    def calcularArea(self):
            return self._alto * self._ancho