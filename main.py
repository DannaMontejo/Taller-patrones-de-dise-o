from singleton import ConfiguracionGlobal
from factory import FabricaTelefono, FabricaComputadora
from abstract import FabricaEconomica
from decorator import CarcasaAntigolpes
from prototype import ClonarProducto

# Implementación de patrones de diseño 
# 1. Singleton
print("Patrón Singleton - Configuración global")
config = ConfiguracionGlobal()
config.modo_debug = True
config.mostrar_configuracion()

# 2. Factory method
print("Patrón Factory Method - Crear productos básicos")
fabrica_computadora = FabricaComputadora()
compu1 = fabrica_computadora.crear_producto("Lenovo ideapad",2300000)
compu1.describir()

# 3. Abstract factory
print("Patrón Abstract Factory - Implementar familias de productos")
fabrica_economica = FabricaEconomica()
producto_economico = fabrica_economica.crear_telefono()
producto_economico.describir()

# 4. Prototype
print("Patrón prototype - Clonar productos")
clon = ClonarProducto("Teléfono Clonable", 2500000)
clon_copia = clon.clonar()
clon_copia.describir()

# 5. Decorator
print("Patrón Decorator - Agregar funcionalidades dinámicas")
tel_con_carcasa = CarcasaAntigolpes(producto_economico)
print(f"Decorador 1: {tel_con_carcasa.describir()} | Costo final: ${tel_con_carcasa.calcular_costo_final()}")