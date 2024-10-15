from abc import ABC, abstractmethod

class Figure(ABC):
    _id_counter = 0

    def __init__(self, type):
        Figure._id_counter += 1
        self._type = type
        self._id = Figure._id_counter

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @abstractmethod
    def to_json(self):
        pass