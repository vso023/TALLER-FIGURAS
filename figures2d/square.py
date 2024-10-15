import json
from figures.IFigura2D import Figure2D
from figures.figure import Figure


class Square(Figure, Figure2D ):
    def __init__(self, side):
        super().__init__('Cuadrado')
        self.side = side

    def area(self):
        return self.side** 2
    
    def perimeter(self):
        return self.side *4
    
    def to_dict(self):
        return { #json.dumps() function will convert a subset of Python objects into a json string
            "tipo": self.type,
            "id": self.id,
            "side": self.side,
            "area": self.area(),
            "perimetro": self.perimeter()
        }
    