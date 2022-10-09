class Rectangulo:

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura
    

base = int(input("Ingresa la base: "))
altura = int(input("Ingresa la altura: "))

rectangulo = Rectangulo(base,altura)

print(f'El area es: {rectangulo.calcularArea()}')