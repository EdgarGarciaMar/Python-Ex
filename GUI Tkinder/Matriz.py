B = [] # Declaramos la matriz [Lista]
valor = 0
for i in range(6):
    B.append([]) # Agregamos la columna
    for j in range(6):
        valor += 1
        B[i].append(valor)

#Impresion con formato
for fila in B:
    print("[", end=" ")
    for elemento in fila:
        print(elemento, end=" ") # End es para dejar un espacio o agregar un texto al final
    print("]")
print()