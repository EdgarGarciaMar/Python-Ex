"""#For en python
cadena = "Hola"

for letra in cadena:
    print(f'letra: {letra}')
else: # else de cuando termina el for
    print("fin For")

#break termina ciclos
for letra in "Holanda":
    if letra == "a":
        print(f'Letra encontrada: {letra}')
        break
    else:
        print("fin del for")
"""
"""A
for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}')
"""
for i in range(6):
    if i % 2 != 0:
        continue #Ejecuta la siguiente iteracion en el ciclo
    print(f'Valor: {i}')

