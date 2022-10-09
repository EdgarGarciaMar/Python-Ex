class Persona:  # Herencia simple, todas las clases heredan de la clase object
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def __str__(self): #Metodo para sobreescribir los parametros de la clase, permite imprimir los valores de la clase en otro archivo donde se importe la clase
        return f'Persona: {self._nombre}, Edad {self._edad}' # represents the class objects as a string

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad


class Empleado(Persona):  # Se pone la clase persona porque es la clase padre
    def __init__(self, nombre, edad, sueldo): # Se inicializan los parametros de la clase heredada
        super().__init__(nombre, edad) # Se inicializa el constructor de la clase heredada
        self._sueldo = sueldo

    def __str__(self):
        return f' {super().__str__()}, Sueldo: {self._sueldo}' # Como la clase padre tiene str, solo lo llamamos por herencia con super y concatenamos con el parametro de sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

if __name__ == "__main__":
    empleado1 = Empleado("Juan", 28, 100)
    print(f'{empleado1.nombre} {empleado1.edad}, {empleado1.sueldo}')
