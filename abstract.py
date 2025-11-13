from abc import ABC, abstractmethod
from factory import Computadora,Tableta,Telefono

class FabricaLinea(ABC):
    @abstractmethod
    def crear_computadora(self):
        pass

    @abstractmethod
    def crear_telefono(self):
        pass

    @abstractmethod
    def crear_tableta(self):
        pass


class FabricaPremium(FabricaLinea):
    def crear_computadora(self):
        return Computadora("Computadora linea premium", 5000000)

    def crear_telefono(self):
        return Telefono("Teléfono linea premium", 3600000)

    def crear_tableta(self):
        return Tableta("Tableta linea premium", 1500000)


class FabricaEstandar(FabricaLinea):
    def crear_computadora(self):
        return Computadora("Computadora linea estándar", 2400000)

    def crear_telefono(self):
        return Telefono("Teléfono linea estándar", 1800000)

    def crear_tableta(self):
        return Tableta("Tableta linea estándar", 1000000)


class FabricaEconomica(FabricaLinea):
    def crear_computadora(self):
        return Computadora("Computadora linea económica", 1500000)

    def crear_telefono(self):
        return Telefono("Teléfono linea económico", 700000)

    def crear_tableta(self):
        return Tableta("Tableta linea económica", 800000)
    
""" Prueba
fabrica_premium = FabricaPremium()
producto_premium = fabrica_premium.crear_computadora()
producto_premium.describir()
"""