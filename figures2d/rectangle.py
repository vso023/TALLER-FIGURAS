from figures.IFigura2D import Figure2D
from figures.figure import Figure
from generator.Id_generator import IdGenerator


class Rectangle(Figure, Figure2D):
    def __init__(self, length, height):
        figure_id = IdGenerator.id_generator()  
        super().__init__('Rectangulo', figure_id)
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height
    def perimeter(self):
        return 2 * (self.length + self.height)
    
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
