from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, figure_type, figure_id):
        self._type = figure_type
        self._id = figure_id

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @abstractmethod
    def to_json(self):
        pass

