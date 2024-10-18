
from abc import ABC, abstractmethod
from figures.IFigure import Figure

class Figure2D(Figure, ABC):
    def __init__(self, type, id):
        self._type = type
        self._id = id

    def get_id(self):
        return self._id

    def get_type(self):
        return self._type

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
