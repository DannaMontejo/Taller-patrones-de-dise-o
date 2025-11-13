from abc import ABC, abstractmethod

#producto abstracto
class Producto(ABC):
    def __init__(self,nombre,precio,linea="Generica"):
        self.nombre = nombre
        self.precio = precio
        self.linea = linea
    
    @abstractmethod
    def describir(self):
        pass

#productos concretos
class Computadora(Producto):
    def describir(self):
        print(f"Computadora: {self.nombre} - ${self.precio}")

class Telefono(Producto):
    def describir(self):
        print(f"Teléfono: {self.nombre} - ${self.precio}")

class Tableta(Producto):
    def describir(self):
        print(f"Tableta: {self.nombre} - ${self.precio}")

#creador abstracto
class FabricaProducto(ABC):
    @abstractmethod
    def crear_producto(self, nombre, precio):
        pass

#creadores concretos
class FabricaComputadora(FabricaProducto):
    def crear_producto(self, nombre, precio):
        return Computadora(nombre, precio)

class FabricaTelefono(FabricaProducto):
    def crear_producto(self, nombre, precio):
        return Telefono(nombre, precio)

class FabricaTableta(FabricaProducto):
    def crear_producto(self, nombre, precio):
        return Tableta(nombre, precio)   

fabrica_computadora = FabricaComputadora()
compu1 = fabrica_computadora.crear_producto("Lenovo ideapad",2300000)
compu1.describir()