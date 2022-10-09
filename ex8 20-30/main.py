edad = int(input("Introduce tu edad: "))

veintes = edad >= 20 and edad < 30
treintas = edad >=30 and edad < 40

casoEspecial = veintes and treintas

if veintes:
    print(f'{edad} años es una edad considerada 20"s ')
elif casoEspecial != True:
    print(f'{edad} años no esta en los 20"s o 30"s ')
else:
    print(f'{edad} años es una edad considerada 30"s ')
