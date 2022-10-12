try:
    archivo = open('prueba.txt','w') #abrir o crear un archivo, segundo parametro es para leer, escribir,etc
    archivo.write("Agregamos Informacion al archivo\n")
    archivo.write("ADIOS!!")

except Exception as e:
    print(e)
finally:
    archivo.close()
