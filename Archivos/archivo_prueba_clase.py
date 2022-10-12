from ManjeoArchivos import ManejoArchivos
#Uso de clase de manejador de archivos
#Contex manger-Administrador de recursos
with ManejoArchivos("prueba.txt") as archivo:
    print(archivo.read())