
#Funcion que convierte F a C
def FareahrenheitCelcius(fahrenheit=0):
    return (fahrenheit-32)/1.8

#Funcion que convierte  C a F
def CelciusFareahrenheit(celcius=0):
    return (celcius*1.8)+32

def menu(opc):
    if opc == 0:
        celcius = float(input("Ingresa los grados celcius = "))
        convercionCelciusFareahrenheit = CelciusFareahrenheit(celcius)
        print(f'Los grados fahrenheit son : {convercionCelciusFareahrenheit:.2f}') #Impresion de 2 decimales
    elif opc == 1:
        fahrenheit = float(input("Ingresa los grados faharenheit = "))
        convercionFareahrenheitCelcius = FareahrenheitCelcius(fahrenheit)
        print(f'Los grados Celcius son : {convercionFareahrenheitCelcius:0.2f}')
    else:
        print("Opc no valida")

print("0: Convertir de C a F")
print("1: Convertir de F a C")
opc = int(input("Ingresa una opcion 0-1 : "))
menu(opc)
