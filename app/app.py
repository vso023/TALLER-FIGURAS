from figures2d.circle import Circle
from figures2d.rectangle import Rectangle
from figures2d.square import Square
from figures3d.cube import Cube
from figures3d.cuboid import Cuboid
from figures3d.sphere import Sphere
from generator.Json_generator import JsonGenerator
from popUp.popUp import PopUp

class App:
    def __init__(self):
        self.popup = PopUp()
    def select_2dfigure(self):
        options = ['Circulo', 'Rectangulo', 'Cuadrado']
        selected_option = self.popup.read_menu_choice_string("Seleccione una figura 2D", options)
        
        if selected_option == 'Circulo':
            ratio = self.popup.read_double('Ingrese el radio del circulo')
            circle = Circle(ratio)
            json_result = JsonGenerator.figure_to_json(circle)
            self.popup.display_results(json_result)
            #self.popup.display_results(f'Area del circulo: {circle.area}, Perimetro del circulo: {circle.perimeter}')

        if selected_option == 'Rectangulo':
            lenght = self.popup.read_double('Ingrese la base del rectangulo')
            height = self.popup.read_double('Ingrese la altura del rectangulo')

            rectangle = Rectangle(lenght, height)
            json_result = JsonGenerator.figure_to_json(rectangle)
            self.popup.display_results(json_result)
            #self.popup.display_results(f'Area del rectangulo: {rectangle.area}, Perimetro del rectangulo: {rectangle.perimeter}')

        if selected_option == 'Cuadrado':
            side = self.popup.read_double('Ingrese el largo de los lados del cuadrado')
            square = Square(side)
            json_result = JsonGenerator.figure_to_json(square)
            self.popup.display_results(json_result)


            #self.popup.display_results(f'Area del cuadrado: {square.area}, Perimetro del cuadrado: {square.perimeter}')
    
    def select_3dfigure(self):
        options = ['Cuboide', 'Cubo', 'Esfera']
        selected_option = self.popup.read_menu_choice_string("Seleccione una figura 3D", options)

        if selected_option == 'Cubo':
            height = self.popup.read_double('Ingrese la altura del cubo')

            cube = Cube(height)
            json_result = JsonGenerator.figure_to_json(cube)
            self.popup.display_results(json_result)
            
            #self.popup.display_results(f'Volumen del cubo: {cube.volume}, Superficie del cubo: {cube.surface}')
        
        if selected_option == 'Cuboide':
            height = self.popup.read_double('Ingrese la altura del cuboide')
            width = self.popup.read_double('Ingrese la anchura del cuboide')
            length = self.popup.read_double('Ingrese el largo del cuboide')

            cuboid = Cuboid(length, height, width)
            json_result = JsonGenerator.figure_to_json(cuboid)
            self.popup.display_results(json_result)
            #self.popup.display_results(f'Volumen del cuboide: {cuboid.volume}, Superficie del cuboide: {cuboid.surface}')

        if selected_option == 'Esfera':
            ratio = self.popup.read_double('Ingrese el radio de la esfera')

            sphere = Sphere(ratio)
            json_result = JsonGenerator.figure_to_json(sphere)
            self.popup.display_results(json_result)
            #self.popup.display_results(f'Volumen de la esfera: {sphere.volume}, Superficie de la esfera: {sphere.surface}')
        