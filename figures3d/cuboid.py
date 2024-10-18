import json
from figures.Figure3D import Figure3D
from figures.IFigure import Figure
from generator.Id_generator import IdGenerator

class Cuboid(Figure3D, Figure):
    def __init__(self, length, height, width):
        figure_id = IdGenerator.id_generator()  
        super().__init__('Cuboide', figure_id)
        self.length = length
        self.height = height
        self.width = width

    def volume(self)->float:
        return self.height * self.length * self.width
    
    def surface(self)->float:
        return (2 * self.length * self.width) + (2 * self.length * self.height) + (2 * self.width * self.height)

    def to_dict(self):
        return {
            "tipo": self.type,
            "id": self.id,
            "altura": self.height,
            "anchura": self.width,
            "largo": self.length,
            "volumen": self.volume(),
            "superficie": self.surface()
            
        }

    