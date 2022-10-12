try:
    archivo = open("prueba.txt","r", encoding= "utf8")#En el primer parametro se puede poner la ruta, windows \\ ,en mac \
    print(archivo.read()) #meotodo normal para imprimir_todo el archivo
    #print(archivo.read(5)) #leer cierto numero de letras

    # Iterar las lineas
    for line in archivo:
        print(f'Linea: {line}')
    archivo.close()
except Exception as e:
    print(e)
finally:
    print("fin del archivo...")

