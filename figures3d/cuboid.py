import json
from figures.IFigura3D import Figure3D
from figures.figure import Figure


class Cuboid(Figure, Figure3D):
    def __init__(self, length, height, width):
        super().__init__('Cuboide')
        self.length = length
        self.height = height
        self.width = width

    def volume(self):
        return self.height * self.length * self.width
    
    def surface(self):
        return (2 * self.length * self.width) + (2 * self.length * self.height) + (2 * self.width * self.height)

    def to_json(self):
        return json.dumps({
            #json.dumps() function will convert a subset of Python objects into a json string
            "tipo": self.type,
            "id": self.id,
            "altura": self.height,
            "anchura": self.width,
            "largo": self.length,
            "volumen": self.volume(),
            "superficie": self.surface()
            
        }

        )