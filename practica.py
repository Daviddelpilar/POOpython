class Producto():
    def __init__(self,nombre,unidades,precio):
        self.nombre=nombre
        self.unidades=unidades
        self.precio=precio

    def Informacion(self):
        print(f'el producto {self.nombre} cuesta {self.precio} y quedan {self.unidades}')


class Servicio():
    def __init__(self):
        print('El servicio es basico')


class Estandar(Servicio):
    def consultarDetalle(self):
        print('El servicio es estandar')


class Premium(Servicio):
    def consultarDetalle(self):
        print('El servicio es premium')


producto1=Producto('camisa', 10, 9.95)
producto1.Informacion()
Estandar.consultarDetalle()
Premium.consultarDetalle()

