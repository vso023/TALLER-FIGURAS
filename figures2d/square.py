import json
from figures.Figure2D import Figure2D
from figures.IFigure import Figure
from generator.Id_generator import IdGenerator


class Square(Figure2D, Figure):
    def __init__(self, side):
        super().__init__('Square')  # Llamada al constructor de la clase abstracta
        self._side = side

    def area(self) -> float:
        return self._side ** 2

    def perimeter(self) -> float:
        return 4 * self._side

    def to_dict(self) -> dict:
        return {
            'tipo': self.type,
            'id': self.id,
            'lado': self._side,
            'area': self.area(),
            'perimetro': self.perimeter()
        }

    