from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self,nombre, sueldo, departamento):
        Empleado.__init__(self,nombre=nombre,sueldo=sueldo)
        self._departamento = departamento

    @property
    def departamento(self):
        return self._departamento
    @departamento.setter
    def departamento(self,departamento):
        self._departamento = departamento

    def __str__(self):
        return f'Gerente [Departamento: {self._departamento} {Empleado.__str__(self)}'

