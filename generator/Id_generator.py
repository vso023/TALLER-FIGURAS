class GeneradorID:
    _contador = 1

    @classmethod
    def generar_id(cls):
        id_unico = f"Figura-{cls._contador}"
        cls._contador += 1
        return id_unico
