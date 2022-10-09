#Haciendo clase abstacta

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):

    def __init__(self,ancho,alto):
        if self.validar(ancho,alto):
            self._ancho = ancho
            self._alto = alto
        else:
            self._ancho = 0
            self._alto = 0

    def __str__(self):
        return f'Clase FiguraGeomeetrica ancho: {self._ancho}, alto: {self._alto}'
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self,ancho):
        self._ancho = ancho
    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self, alto):
        self._alto = alto

    def validar(self,ancho,alto):
        if ancho < 0 or alto < 0:
            print("Error de creación de valor en la Figura")
            return False
        else:
            return True

    @abstractmethod
    def calcularArea(self):
        pass


