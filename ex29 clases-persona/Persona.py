#clases en codigo duro
class Persona:#Nombre de la clase igual al proyecto por buenas practicas
    def __init__(self):#Metodo inicializador que recibe la referencia del objeto
        self.nombre = "Juan" #Atributos
        self.apellido = "Perez"
        self.edad = 28

#Crear un objeto
"""
Se crea una variable para almacenar el objeto e identificarlo
posteriormente se llama a la clase la cual llamara al constructor que python
tiene oculto
"""
persona1 = Persona()
#Acceso de a los atributos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)