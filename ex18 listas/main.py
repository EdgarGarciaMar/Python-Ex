#definir lista --arreglos
nombres = ["Juan","Karla","Ricardo","Maria"]
#imprimir lista
print(nombres)
#Acceder a la lista
print(nombres[0])
print(nombres[1])
#Acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
#imprimir un rango
print(nombres[0:2])
#Ir del inicio de la lista al indice sin incluirlo
print(nombres[:3])
#Desde el indice indicado hasta el final
print(nombres[1:])
#Cambiar el valor especificando un valor
nombres[3]= "Ivone"
print(nombres)
#iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("No hay mas nombres")
#Preguntar la longitud de un arreglo
print(len(nombres))
#Agregar un elemento
nombres.append("Lorenzo")
print(nombres)
#Agregar un elemento en un indice especifico
nombres.insert(1,"octavio")
print(nombres)
#Eliminar un elemento
nombres.remove("octavio")
#Remover el ultimo valor agregado3
nombres.pop()
print(nombres)
#Eliminar un indice
del nombres[0]
print(nombres)
#Limpiar el array
nombres.clear()
print(nombres)
#Borrar la lista por completo
del nombres


print(" ")
print("Inicio de tuplas")
#Tuplas, tipo de arreglo o lista no modificable
frutas = ("Naranja","Platano","Guayaba")
print(frutas)
#Longitud
print(len(frutas))
#Acceder a un elemento particular
print(frutas[0])
#Navegacion inversa
print(frutas[-1])
#Acceder a un rango
print(frutas[0:1])#No se incluye el ultimo indice "n-1"
#Recorrer elementos
for fruta in frutas:
    print(fruta,end=" ")#Para quitar el salto de linea automatico "\n"
#cambiar la tupla no se puede
#modificar de tupla a lista para poder modificarla
frutaLista = list(frutas) #Convertir la tupla a lista
frutaLista[0]="pera"
frutas= tuple(frutaLista)#Convertimos de lista a tupla
print("")
print(frutas)

print("")
print("Inicio de coleccion set")#coleccion sin orden y sin indices
planetas = {"Marte", "Jupiter","Venus"}
#Largo
print(len(planetas))
#Revisar el set
print("Marte" in planetas)
#Agregar un elemento
planetas.add("Tierra")
print(planetas)
#No se pueden duplicar el elementos
#Eliminar elementos
planetas.remove("Tierra")
print(planetas)
#Eliminar elemento si arrojar el error de que no coinside la key
planetas.discard("Jupiters")
print(planetas)
#limpiar el set
planetas.clear()
print(planetas)
#eliminar el set
del planetas



