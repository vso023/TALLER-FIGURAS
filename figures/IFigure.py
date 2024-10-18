from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, tipo, id_unico):
        self._tipo = tipo
        self._id = id_unico

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._tipo

    @abstractmethod
    def to_json(self):
        pass

