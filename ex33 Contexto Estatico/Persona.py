class Persona:
    contadorPersonas = 0

    def __init__(self, nombre, edad):
        self._idPersona = Persona.generarSiguienteValor()
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f'Persona [{self._idPersona} {self._nombre} {self._edad}]'

    @property
    def idPersona(self):
        return self._idPersona

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @classmethod
    def generarSiguienteValor(cls):
        cls.contadorPersonas += 1
        return cls.contadorPersonas


persona1 = Persona(nombre="Juan", edad=28)
print(persona1)
persona2 = Persona(nombre="Karla", edad=31)
print(persona2)
print(f'Valor de contador personas = {Persona.contadorPersonas}')
