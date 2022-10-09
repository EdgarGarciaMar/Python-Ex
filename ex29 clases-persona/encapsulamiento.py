class Person:

    def __init__(self, nombre, apellido, edad, lectura):  # parametros y atributos de objeto
        self._nombre = nombre  # _nombre sirve para hacer privado el atributo (Sugerencia al programador) y solo lo puede usar la clase [Atributo encapsulado]
        self._apellido = apellido  # __nombre si hace privado el atributo, solo la clase lo puede acceder
        self._edad = edad
        self._lectura = lectura

    # Decorador de property: evita que se accesen a los atributos fuera de la clase y facilita la sitaxis
    @property
    # metodos get para obtener los valores de la clase
    def nombre(self):
        return self._nombre

    # Setter
    @nombre.setter  # Se pone el atributo sin parentesis y setter para modificar el valor
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def lectura(self):
        return self._lectura

    def mostrarDetalle(self):  # Parametro self se agrega a todos los metodos [Metodo]
        print(f'Persona: {self._nombre} {self._apellido} , Edad: {self._edad}')  # Atributos usando self si se puede

    #Metodo destructor
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido} Eliminado')

#Imports de modulos
#from Person import Person
#print(__name__) sirve para ver que archivo de python se esta ejecutando
#Con esta comprobacion evitamos que este codigo se ejecute en otro modulo o archivo
if __name__ == "__main__":
    persona = Person("Edgar", "Garcia", 20, "VARIABLE")
    # Getter
    print(
        f'Nombre : {persona.nombre} {persona.apellido}, Edad: {persona.edad}')  # Al usar el property ya no es necesario usar el parentesis para el metodo getter [Aceso de manera indirecta]

    # Setter
    persona.nombre = "Luis"
    persona.apellido = "Gomez"
    persona.edad = 21

    print(f'Nombre : {persona.nombre} {persona.apellido}, Edad: {persona.edad}')
    # Variables de solo lectura
    # Son variables que son como las demas y cuentan con metodo get pero no set, ya que si se quiere modificar mandara un error

    print(f'Variable de solo lectura {persona.lectura}')
    # persona.lectura = "algo" linea que da un error
    

