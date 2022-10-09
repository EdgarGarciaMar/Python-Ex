from Cuadrado import *
from Rectangulo import *
from pack.pack import Pack #Import desde otra carpeta

print("Creacion de un cuadrado".center(50,"-"))
cuadrado1 = Cuadrado(lado =-5,color ="rojo") #Auto documentacion
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(f'Area {cuadrado1.calcularArea()}')
print(cuadrado1)
#MRO METHOD RESOLUTION ORDER
print (f'MRO')
print(Cuadrado.mro()) # Para aclarar dudas de cual es la resolucion en herencia multiple
print("Creacion de rectangulo".center(50,"-"))
rectangulo = Rectangulo(base=5, altura=10, color="Verde")
print(rectangulo)
print(f'Color {rectangulo.color}')
print(f'Alto {rectangulo.alto}')
print(f'base {rectangulo.ancho}')
print(f'Area {rectangulo.calcularArea()}')
#Prueba del setter
rectangulo.alto=9
rectangulo.ancho=9
print(f'Alto {rectangulo.alto}')
print(f'base {rectangulo.ancho}')

pack1 = Pack("HI")