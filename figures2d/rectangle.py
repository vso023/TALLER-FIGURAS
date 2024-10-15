
import json
from figures.IFigura2D import Figure2D
from figures.figure import Figure


class Rectangle(Figure, Figure2D):
    def __init__(self, length, width):
        super().__init__('Rectangulo')
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def to_json(self):
        return json.dumps({
            #json.dumps() function will convert a subset of Python objects into a json string
            "tipo": self.type,
            "id": self.id,
            "altura": self.width,
            "base": self.length,
            "area": self.area(),
            "perimetro": self.perimeter()
        }

        )
