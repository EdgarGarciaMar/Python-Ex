miVariable = int(input(f'Ingresa un numero para ver si es par o inpar: '))

test = miVariable % 2 == 0

if miVariable:
    print(f'El numero {miVariable} es par.')
else:
    print(f'El numero {miVariable} es inpar.')
