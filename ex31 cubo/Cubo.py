class Cubo:

    def __init__(self,ancho,profundidad,alto):
        self.ancho = ancho
        self.profundidad = profundidad
        self.alto = alto

    def calcularVolumen(self):
        return self.ancho * self.profundidad * self.alto


ancho = int(input("Ingresa el ancho: "))
profundidad = int(input("Ingresa la profundidad: "))
alto = int(input("Ingresa el alto: "))

cubo = Cubo(ancho,profundidad,alto)

print(f'El volumen es {cubo.calcularVolumen()} m^3')
