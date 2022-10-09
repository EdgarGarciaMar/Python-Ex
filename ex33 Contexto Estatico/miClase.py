class MiClase:

    variableClase = "Valor de clase"

    def __init__(self, variableinstancia):
        self._variableInstancia = variableinstancia

    @property
    def variableInstancia(self):
        return self._variableInstancia

    #metodos estaticos
    @staticmethod
    def metodoEstatico(): #no recibe el parametro de self ni info de la clase
        print(MiClase.variableClase)

    #metodo de clase
    @classmethod
    def metodoClase(cls):#Parametro de la clase
        print(cls.variableClase)

        #metodo de instancia de los objetos
    def metodoInstancia(self): #contexto dinamico si puede acceder a los metodos estaticos de la clase
        self.metodoClase() #Metodos de los objetos que permiten modificar por medio de los metodos de clase las variables de clase
        self.metodoEstatico() #llamamos al metodo estatico


print(MiClase.variableClase)#Imprimir la variable de clase
miClase = MiClase("VALOR VARIABLE INSTANCIA")
print(miClase.variableInstancia)
print(MiClase.variableClase)

MiClase.variableClase2 = "Valor variable clase 2" #Variable de clase dinamica
print(MiClase.variableClase2)
print(miClase.variableClase2)#Accediendo desde un objeto si corre con este warning

#llamando al metodo estatico
print("Metodo estatico".center(50, "-"))
MiClase.metodoEstatico()

#llamando al metodo de clase
print("Metodo de clase".center(50,"-"))
MiClase.metodoClase()

#Contexto estatico dinamico

print("Contexto Estatico o dinamico".center(50,"-"))
miObjeto = MiClase("Hola")
#miObjeto.metodoClase()
miObjeto.metodoInstancia()
