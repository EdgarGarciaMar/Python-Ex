#range(inicio,fin(Requerido),Iterador) Todos son numeros
print("Numeros divisibles por 3 0-10")
for numero in range(0,11,1):# el valor final de range funciona con la exp n-1, si es n=10, el for solo llega a 9
    if numero % 3 == 0:
        print(numero)
else:
    print("Fin del ejercicio 1")

print("Rango de 2 a 6 ")
for numero2 in range(2,7,1):
    print(numero2)
else:
    print("Fin del ejercicio 2")

print("Rango de 3 a 10 de 2 en 2")
for numero3 in range(3,11,2):
    print(numero3)
else:
    print("Fin del ejercicio 3")