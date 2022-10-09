def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado


print(f'Los valores multiplicados son: {multiplicar(1, 2)}')
print(f'Los valores multiplicados son: {multiplicar(2, 2, 2)}')
print(f'Los valores multiplicados son: {multiplicar(3, 5, 15)}')
