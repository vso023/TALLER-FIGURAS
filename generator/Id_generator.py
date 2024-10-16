class IdGenerator:
    _contador = 1

    @classmethod
    def id_generator(cls):
        id_unico = f"{cls._contador}"
        cls._contador += 1
        return id_unico
