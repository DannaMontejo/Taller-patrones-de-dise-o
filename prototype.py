import copy
from factory import Producto

class ClonarProducto(Producto):
    def describir(self):
        print(f"Producto clonado: {self.nombre} - ${self.precio}")

    def clonar(self):
        return copy.deepcopy(self)

"""" Prueba    
clon = ClonarProducto("Teléfono Clonable", 2500000)
clon_copia = clon.clonar()
clon_copia.describir()
"""