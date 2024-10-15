from abc import ABC, abstractmethod

class Figure(ABC):

    def __init__(self, type, id_unico):
        self._type = type
        self._id = id_unico

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @abstractmethod
    def to_dict(self):
        pass