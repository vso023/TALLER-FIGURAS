
import json
from figures.Figure2D import Figure2D
from generator.Id_generator import IdGenerator

class Circle(Figure2D):
    def __init__(self, ratio):
        figure_id = IdGenerator.id_generator() 
        super().__init__('Circulo', figure_id)
        self.pi = 3.14159
        self.ratio = ratio

    def area(self)->float:
        return self.pi * (self.ratio **2)
    
    def perimeter(self)->float:
        return 2 * self.pi * self.ratio
    
    def to_json(self):
        return json.dumps({
            "tipo": self.type,
            "id": self.id,
            "radio": self.ratio,
            "area": self.area(),
            "perimetro": self.perimeter()
        })