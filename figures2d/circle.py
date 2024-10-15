
import json
from figures.IFigura3D import Figure3D
from figures.figure import Figure


class Circle(Figure, Figure3D):
    def __init__(self, ratio ):
        super().__init__('Circulo')
        self.pi = 3.14159
        self.ratio = ratio

    def area(self):
        return self.pi * (self.ratio **2)
    
    def perimeter(self):
        return 2 * self.pi * self.ratio
    
    def to_json(self):
        return json.dumps({ #json.dumps() function will convert a subset of Python objects into a json string
            "tipo": self.type,
            "id": self.id,
            "ratio": self.ratio,
            "area": self.area(),
            "perimetro": self.perimeter()
        })