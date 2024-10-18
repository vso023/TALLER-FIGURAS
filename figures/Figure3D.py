from abc import ABC, abstractmethod
from figures.IFigure import Figure

class Figure3D(Figure, ABC):
    def __init__(self, type, id):
        self._type = type
        self._id = id

    def get_id(self):
        return self._id

    def get_type(self):
        return self._type

    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def surface(self):
        pass
