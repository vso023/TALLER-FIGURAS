from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass
