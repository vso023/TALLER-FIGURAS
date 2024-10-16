from figures.IFigura2D import Figure2D
from figures.figure import Figure


class Rectangle(Figure, Figure2D):
    def __init__(self, length, height):
        super().__init__('Rectangulo')
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def to_dict(self):
        return{
            #json.dumps() function will convert a subset of Python objects into a json string
            "tipo": self.type,
            "id": self.id,
            "altura": self.height,
            "base": self.length,
            "area": self.area(),
            "perimetro": self.perimeter()
        }
