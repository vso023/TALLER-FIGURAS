from abc import ABC, abstractmethod

class Figura2D(ABC):
    @abstractmethod
    def calcular_perimetro(self):
        pass

    @abstractmethod
    def calcular_area(self):
        pass
