from abc import ABC, abstractmethod
from figures.IFigure import Figure

class Figure3D(Figure, ABC):
    def __init__(self, type, id):
        super().__init__(type, id)


    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def surface(self):
        pass
