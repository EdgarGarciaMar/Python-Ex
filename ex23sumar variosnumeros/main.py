def sumarNNumeros(*args):
    sumaFinal = 0
    for numero in args:
        sumaFinal += numero

    return sumaFinal

print(f'La suma de todos los numeros es: {sumarNNumeros(1,1)}')
print(f'La suma de todos los numeros es: {sumarNNumeros(1,2,3,4,5) }')
print(f'La suma de todos los numeros es: {sumarNNumeros(9,3,5) }')
#Palabra reservada pass es para declarar la funcion sin implementacion
#Esto es util para tener idea de la impmentacion de funciones
"""
def miFuncion():
    pass
    
miFuncion()
"""

