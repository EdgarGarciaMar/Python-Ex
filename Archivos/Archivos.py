try:
    archivo = open('prueba.txt','w', encoding='utf8') #abrir o crear un archivo, segundo parametro es para leer, escribir,etc encodign para poner acentos
    archivo.write("Agregamos Información al archivo\n")
    archivo.write("ADIOS!!")

except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Fin del archivo')
