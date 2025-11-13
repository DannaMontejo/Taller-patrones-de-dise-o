from factory import Producto, FabricaTelefono

# Decorador abstracto
class ProductoDecorador(Producto):
    def __init__(self, producto: Producto):
        self._producto = producto
        self.nombre = producto.nombre 
        self.precio = producto.precio

    def describir(self):
        return self._producto.describir()

# Decoradores Concretos
class CarcasaAntigolpes(ProductoDecorador):
    def describir(self):
        base_desc = self._producto.describir()
        return f"{base_desc} + Carcasa Antigolpes (Resistencia)"

    def calcular_costo_final(self):
        return self.precio + 50000 

class SoftwareEmpresarial(ProductoDecorador):
    def describir(self):
        base_desc = self._producto.describir()
        return f"{base_desc} + Software Empresarial (Licencia)"

    def calcular_costo_final(self):
        return self.precio + 100000
    
""" Prueba    
fabrica = FabricaTelefono()
tel = fabrica.crear_producto("Telefono 1", 1200000)
tel.describir()
tel_con_carcasa = CarcasaAntigolpes(tel)
print(f"Decorador 1: {tel_con_carcasa.describir()} | Costo final: ${tel_con_carcasa.calcular_costo_final()}")
"""