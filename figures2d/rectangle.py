import json
from figures.Figure2D import Figure2D
from figures.IFigure import Figure
from generator.Id_generator import IdGenerator


class Rectangle(Figure2D):
    def __init__(self, length, height):
        figure_id = IdGenerator.id_generator()  
        super().__init__('Rectangulo', figure_id)
        self.length = length
        self.height = height

    def area(self)->float:
        return self.length * self.height
    def perimeter(self)->float:
        return 2 * (self.length + self.height)
    
    def to_json(self):
        return json.dumps({
            "tipo": self.type,
            "id": self.id,
            "altura": self.height,
            "base": self.length,
            "area": self.area(),
            "perimetro": self.perimeter()
        })
