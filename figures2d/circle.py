
from figures.IFigura2D import Figure2D
from figures.figure import Figure
from generator.Id_generator import IdGenerator


class Circle(Figure, Figure2D):
    def __init__(self, ratio ):
        figure_id = IdGenerator.id_generator() 
        super().__init__('Circulo', figure_id)
        self.pi = 3.14159
        self.ratio = ratio

    def area(self):
        return self.pi * (self.ratio **2)
    
    def perimeter(self):
        return 2 * self.pi * self.ratio
    
    def to_dict(self):
        return { #json.dumps() function will convert a subset of Python objects into a json string
            "tipo": self.type,
            "id": self.id,
            "ratio": self.ratio,
            "area": self.area(),
            "perimetro": self.perimeter()
        }