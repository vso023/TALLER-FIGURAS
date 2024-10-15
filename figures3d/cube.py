import json
from figures.IFigura3D import Figure3D
from figures.figure import Figure


class Cube(Figure, Figure3D):
    def __init__(self, height ):
        super().__init__('Cubo')
        self.height = height

    def volume(self):
        return self.height ** 3
    
    def surface(self):
        return 6 * (self.height ** 2)
    
    def to_json(self):
        return json.dumps({ #json.dumps() function will convert a subset of Python objects into a json string
            "tipo": self.type,
            "id": self.id,
            "altura": self.height,
            "volumen": self.volume(),
            "superficie": self.surface()
        })