#manejo de contexto
#Con esta forma se ahorra usar el try
#cierra automaticamente el cierre
with open("prueba.txt","r",encoding="utf8") as archivo:
    print(archivo.read())