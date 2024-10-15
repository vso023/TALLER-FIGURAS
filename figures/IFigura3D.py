from abc import ABC, abstractmethod

class Figure3D(ABC):
    @abstractmethod
    def volume(self) -> float:
        pass

    @abstractmethod
    def surface(self) -> float :
        pass
