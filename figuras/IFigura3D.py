from abc import ABC, abstractmethod

class Figura3D(ABC):
    @abstractmethod
    def calcular_volumen(self):
        pass

    @abstractmethod
    def calcular_superficie(self):
        pass
