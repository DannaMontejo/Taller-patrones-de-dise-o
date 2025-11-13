class ConfiguracionGlobal:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.modo_debug = False
            cls._instancia.idioma = "ES"
            cls._instancia.entorno = "Producción"
        return cls._instancia

    def mostrar_configuracion(self):
        print(f"Modo debug: {self.modo_debug} | Idioma: {self.idioma} | Entorno: {self.entorno}")

""" Prueba
config = ConfiguracionGlobal()
config.modo_debug = True
config.mostrar_configuracion()
"""