import json
from figures.Figure2D import Figure2D
from figures.IFigure import Figure
from generator.Id_generator import IdGenerator


class Square(Figure2D):
    def __init__(self, side):
        figure_id = IdGenerator.id_generator()  
        super().__init__('Square', figure_id) 
        self._side = side

    def area(self) -> float:
        return self._side ** 2

    def perimeter(self) -> float:
        return 4 * self._side

    def to_json(self) -> dict:
        return json.dumps({
            'tipo': self.type,
            'id': self.id,
            'lado': self._side,
            'area': self.area(),
            'perimetro': self.perimeter()
        })

    