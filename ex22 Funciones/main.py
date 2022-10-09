#Parametros son declarados en la funcion {parametro nombre de la variable }
def miFuncion(nombre, apellido): #def para funcion y cuidar la identacion y de igual forma primero se debe definir y luego se llama
    print("Funcion")
    print(f'Hola {nombre} {apellido}')

miFuncion("Edgar","G")#Argumentos son los que le pasamos a la funcion, argumento es el valor
miFuncion("karla","Lara")
#Para debuggear funciones, se da clik en step over para las llamadas y codigo secuencial o ciclos
#Para entrar a la definicion y proceso de las funciones se da step into y asi poder ver la ejecucion del codigo dentro de la funcion

def suma(a,b):
    return a + b #Devuelve un valor

resultado= suma(5,3)
print(f'El resultado es: {resultado}')
print(f'El 2resultado es: {suma(1,2)}')

#Valores por default
def suma2(a=0,b=0): # Se inicializan a 0 para que no de error el programa
    return a + b

print(f'Valores default:{suma2()}')
print(f'Valores default reescritos:{suma2(2,8)}')


#Argumentos variables *args notacion de python
def listarNombres(*nombres): #Parametros que no sabemos la cantidad, esto se comporta como una tupla
    for nombre in nombres:
        print(nombre)

listarNombres("Juan", "Karla", "Maria", "Ernesto") # Tupla inmutable
listarNombres("Laura", "Carlos")

#Argumentos variables llave-valor Python
#paso de diccionario

def listarTerminos(**terminos): #doc kwargs para recibir parametros llave-valor diccionarios
    for llave, valor in terminos.items():
        print(f'Llave: {llave}, Valor: {valor}')

listarTerminos(IDE = "Integrated Developement Enviroment", PK = "Primary Key") #La llave no necesia comillas y el valor es cualquier tipo de dato
listarTerminos(DBMS = "Database Management System")

#Distintos tipos de datos como argumentos de una funcion
def desplegarNombres(nombres): #lista de datos
    for nombre in nombres:
        print(nombre)

nombres = ["Juan","Karla","Guillermo"]
desplegarNombres(nombres)
desplegarNombres("Carlos") #Iteracion de una lista de caracteres
desplegarNombres((10,11)) #Tupla de 2 elementos enteros iterable
desplegarNombres([10,11]) #Lista de 2 elementos enteros iterable y modificable