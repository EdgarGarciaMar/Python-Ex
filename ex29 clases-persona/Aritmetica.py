class Aritmetica:
    #Clase aritmetica para realizar operaciones
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b

    def restar(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        if self.b == 0:
            print("Error, No se puede divir entre 0")
            return -1
        else:
            return self.a/self.b


aritmetica1 = Aritmetica(5,3)
print(f'Resultado de la suma : {aritmetica1.sumar()}')
print(f'Resultado de la resta : {aritmetica1.restar()}')
print(f'Resultado de la mult : {aritmetica1.multiplicar()}')
print(f'Resultado de la division : {aritmetica1.dividir():.2f}')#Formato de los decimales