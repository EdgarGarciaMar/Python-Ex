class Producto:
    contadorProductos =0
    def __init__(self,nombre, precio):
        Producto.contadorProductos +=1
        self._idProducto = Producto.contadorProductos
        self._nombre = nombre
        self._precio = precio

    @property
    def idProducto(self):
        return self._idProducto

    @idProducto.setter
    def idProducto(self,idProducto):
        self._idProducto =idProducto

    @property
    # metodos get para obtener los valores de la clase
    def nombre(self):
        return self._nombre

    # Setter
    @nombre.setter  # Se pone el atributo sin parentesis y setter para modificar el valor
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self,precio):
        self._precio = precio

    def __str__(self):
        return f'ID: {self.idProducto}, Nombre: {self.nombre}, Precio: {self.precio}'

if __name__ ==  "__main__":
    p = Producto('camisa',100.00)
    print(p)
    p2 = Producto('pantalon',200.00)
    print(p2)