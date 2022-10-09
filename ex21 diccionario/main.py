#Dict (key,value), es muy similar a un struct en c
diccionario = {
    "IDE": "Integrated Development Enviroment",
    "OOP": "Object Oriented Programing",
    "DBMS": "Database Management Systems"
}
print(diccionario)
# Largo
print(len(diccionario))
#Acceder a un elemento (key)
print(diccionario["IDE"])
#Otra forma de recuperar un elemento
print(diccionario.get("OOP"))
#Modificacion de elementos
diccionario["IDE"] = "integrated development environment"
print(diccionario)
#Recorrer los elementos de un diccionario
print("---Recorridos---")
print("Llave y valores:")
for termino,valor in diccionario.items():
    print(termino, valor)
#Recuperacion de llaves
print("Termino:")
for termino in diccionario.keys():
    print(termino)
#Recuperacion de valores
print("Valores:")
for valor in diccionario.values():
    print(valor)
#Preguntar si ya existe una llave
print("IDE" in diccionario)
#no esta
print("IDe" in diccionario)
#Agregar un elemento [No se pueden duplicar las llaves, si ya existe se actualiza los valores]
diccionario["PK"]= "Primary Key"
print(diccionario)

#Remover un elemento
diccionario.pop("DBMS")
print(diccionario)
#Limpiar sin eliminar la variable de diccionario
diccionario.clear()
print(diccionario)
#Eliminar completamente el diccionario
del diccionario