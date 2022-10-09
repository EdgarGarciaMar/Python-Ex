numero = int(input("Porporciona un valor entre 1-3: "))
numeroTexto = ""
if numero == 1:
    numeroTexto= "numero uno"
elif numero == 2:
    numeroTexto = "numero dos"
elif numero == 3:
    numeroTexto = "numero tres"
else:
    numeroTexto = "numero fuera de rango"


print(f'Numero proporcionado: {numero}->{numeroTexto}')

