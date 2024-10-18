import json
from figures.Figure3D import Figure3D
from generator.Id_generator import IdGenerator

class Sphere(Figure3D):
    def __init__(self, ratio):
        figure_id = IdGenerator.id_generator()  
        super().__init__('Esfera', figure_id)
        self.pi = 3.14159
        self.ratio = ratio

    def volume(self) -> float:
        return (4/3) * self.pi * (self.ratio ** 3)
    
    def surface(self) -> float:
        return 4 * self.pi * (self.ratio ** 2)
    
    def to_json(self):
        return json.dumps({
            "tipo": self.type,
            "id": self.id,
            "radio": self.ratio,
            "volumen": self.volume(),
            "superficie": self.surface()
        })

