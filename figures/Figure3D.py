from abc import ABC, abstractmethod
from figures.IFigure import Figure

class Figure3D(Figure, ABC):
    def __init__(self,figure_type, figure_id):
        super().__init__(figure_type, figure_id)

    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def surface(self):
        pass
