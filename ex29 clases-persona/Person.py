class Person:
    #*args es para una tupla
    #*kwargs es para un diccionario
    def __init__(self, nombre, apellido, edad,*args,**kwargs):  # parametros y atributos de objeto
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    def mostrarDetalle(self):  # Parametro self se agrega a todos los metodos [Metodo]
        print(f'Persona: {self.nombre} {self.apellido} , Edad: {self.edad}, Tupla: {self.args}, Diccionario : {self.kwargs} ')

#Implementacion de metodos
#Valores de la tupla "1234",2,3,4
#Valores de el diccionario m="manzana",p="pera"
persona1 = Person("Edgar","Garcia",20,"1234",2,3,4,m="manzana",p="pera")
persona1.mostrarDetalle()

#Acceso de metodos atravez de la clase "No es comun"
Person.mostrarDetalle(persona1)

#Agregar atributos privados a un objeto
persona1.telefono = "1234567"
print(f' Persona1 Telefono : {persona1.telefono}')
#Implementacion sin metodos
'''persona1 =Person("Edgar","Garcia",20)
print(f'Persona 1 = {persona1.nombre} {persona1.apellido} , Edad: {persona1.edad}')


persona2 = Person ("Luis","Martinez",29)
print(f'Persona 2 = {persona2.nombre} {persona2.apellido} , Edad: {persona2.edad}')


#Modificar los valores de los objetos sin encapsulamiento (modificacion de atributos dentro de la clase
persona1.nombre = "Juan Carlos"
persona1.apellido = "Juarez"
persona1.edad = 25
print(f'Persona 1 modificada = {persona1.nombre} {persona1.apellido} , Edad: {persona1.edad}')
'''
