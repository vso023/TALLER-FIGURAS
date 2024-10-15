import json
from figures.IFigura3D import Figure3D
from figures.figure import Figure


class square(Figure, Figure3D ):
    def __init__(self, side):
        super().__init__('Cuadrado')
        self.side = side

    def area(self):
        return self.side** 2
    
    def perimeter(self):
        return self.side *4
    
    def to_json(self):
        return json.dumps({ #json.dumps() function will convert a subset of Python objects into a json string
            "tipo": self.type,
            "id": self.id,
            "side": self.side,
            "area": self.area(),
            "perimetro": self.perimeter()
        })
    