
from abc import ABC, abstractmethod
from figures.IFigure import Figure

class Figure2D(Figure, ABC):
    def __init__(self, figure_type, figure_id):
        super().__init__(figure_type, figure_id)


    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
