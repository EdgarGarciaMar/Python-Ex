from Producto import Producto


class Orden:
    contadorOrdenes = 0
    def __init__(self,productos):
        Orden.contadorOrdenes +=1
        self._idOrden = Orden.contadorOrdenes
        self._productos = list(productos)

    def agregarProductos(self,producto):
        self._productos.append(producto)

    def calcularTotal(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productosStr = ''
        for producto in self._productos:
            productosStr += producto.__str__()+'|'
        return f'Orden:{self._idOrden}, \n Productos : {productosStr}'

if __name__ == '__main__':
    p = Producto('camisa',100.00)
    p2 = Producto('pantalon',200.00)
    productos  = [p,p2]
    orden1 = Orden(productos)
    print(orden1)
    orden2 =Orden(productos)
    print(orden2)

