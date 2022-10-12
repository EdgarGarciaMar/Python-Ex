from Empleado import Empleado
from Gerente import Gerente


def imprimirDetalles(objeto):
    print(objeto)
    print(type(objeto))
    #Metodo de instancia
    if isinstance(objeto, Gerente): #comprobacion si algun parametro pertenece a un objeto
        print(f'Departamento: {objeto.departamento}')

empleado = Empleado(nombre="juan",sueldo=5000)
imprimirDetalles(empleado)


gerente = Gerente(nombre="Karla",sueldo=6000,departamento="Sistemas")
imprimirDetalles(gerente)