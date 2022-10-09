def impresionRecursiva(numero):
    if numero < 0:
        print(f'El {numero} no es valido')
    elif numero >= 1:
        print(f'{numero}')
        impresionRecursiva(numero-1)
    elif numero == 0:
        return
    else:
        print("Fin de la recursion")

print("Prueba 1")
impresionRecursiva(5)
print("Prueba 2")
impresionRecursiva(3)
print("prueba 3")
impresionRecursiva(-1)
print("prueba 4")
impresionRecursiva(0)