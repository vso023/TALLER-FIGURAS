from abc import ABC, abstractmethod

class Figure2d(ABC):
    @abstractmethod
    def perimeter(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass
