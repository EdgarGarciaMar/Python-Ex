try:
    archivo2 = open("prueba.txt","r",encoding="utf8")
    archivo = open("copia.txt","a",encoding="utf8")
    archivo.write(archivo2.read()+" \n Hola!! \n")
    archivo.close()
    archivo2.close()
except Exception as e:
    print(e)
finally:
    print("Fin del archivo add")