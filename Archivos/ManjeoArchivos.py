class ManejoArchivos: #util para archivos o conexion base de datos
    def __init__(self, nombre):
        self._nombre = nombre

    def __enter__(self): #para entrar al archivo
        print("Entrando al recurso".center(50,"-"))
        self._nombre = open(self._nombre,"r",encoding="utf8")
        return self._nombre
    def __exit__(self, exc_type, exc_val, exc_tb): #Salir archivo. param:tipo de exepcion, valor de exepcion, traza el error
        print("Recurso cerrado".center(50,"-"))
        if self._nombre:
            self._nombre.close()