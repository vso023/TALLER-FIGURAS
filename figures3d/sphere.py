import json
from figures.IFigura3D import Figure3D
from figures.figure import Figure


class Sphere(Figure, Figure3D):
    def __init__(self, ratio):
        super().__init__('Esfera')
        self.pi = 3.14159
        self.ratio = ratio

    def volume(self):
        return (4/3) * self.pi * (self.ratio ** 3)
    
    def surface(self):
        return 4 * self.pi * (self.ratio ** 2)
    
    def to_dict(self):
        return {
            #json.dumps() function will convert a subset of Python objects into a json string
            "tipo": self.type,
            "id": self.id,
            "radio": self.ratio,
            "volumen": self.volume(),
            "superficie": self.surface()
        }

