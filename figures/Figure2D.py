
from abc import ABC, abstractmethod
from figures.IFigure import Figure

class Figure2D(Figure, ABC):
    def __init__(self, type, id):
        super().__init__(type, id)


    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
