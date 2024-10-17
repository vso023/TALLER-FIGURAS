import json
from figures.IFigura2D import Figure2D
from figures.figure import Figure
from generator.Id_generator import IdGenerator


class Square(Figure, Figure2D ):
    def __init__(self, side):
        figure_id = IdGenerator.id_generator()  
        super().__init__('Cuadrado', figure_id)
        self.side = side

    def area(self):
        return self.side** 2
    
    def perimeter(self):
        return self.side *4
    
    def to_dict(self):
        return {
            "tipo": self.type,
            "id": self.id,
            "side": self.side,
            "area": self.area(),
            "perimetro": self.perimeter()
        }
    