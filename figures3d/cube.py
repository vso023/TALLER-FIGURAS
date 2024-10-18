import json
from figures.Figure3D import Figure3D
from figures.IFigure import Figure
from generator.Id_generator import IdGenerator


class Cube(Figure3D):
    def __init__(self, height ):
        figure_id = IdGenerator.id_generator()  
        super().__init__('Cubo', figure_id)
        self.height = height

    def volume(self)->float:
        return self.height ** 3
    
    def surface(self)->float:
        return 6 * (self.height ** 2)
    
    def to_json(self):
        return json.dumps({ 
            "tipo": self.type,
            "id": self.id,
            "altura": self.height,
            "volumen": self.volume(),
            "superficie": self.surface()
        })