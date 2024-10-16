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
        self.all_figures = []
        self.figures2d = []
        self.figures3d = []

    def add_figure2d(self, figure):
        self.figures2d.append(figure)
        self.all_figures.append(figure)
        self.popup.display_results(f"Figura 2D agregada: {figure.to_json()}")

    def add_figure_3d(self, figure):
        self.figures3d.append(figure)
        self.all_figures.append(figure)
        self.popup.display_results(f"Figura 3D agregada: {figure.to_json()}") 
    
    def add_figure_to_all(self, figure):
        self.all_figures.append(figure)
        self.popup.display_results(f"Figura agregada a la lista general: {figure.to_json()}")

    def select_2dfigure(self):
        options = ['Circulo', 'Rectangulo', 'Cuadrado']
        selected_option = self.popup.read_menu_choice_combobox("Seleccione una figure 2D", options)
        
        if selected_option == 'Circulo':
            ratio = self.popup.read_double('Ingrese el radio del circulo')
            circle = Circle(ratio)
            self.add_figure2d(circle)
            #self.popup.display_results(json_result)
            #self.popup.display_results(f'Area del circulo: {circle.area}, Perimetro del circulo: {circle.perimeter}')

        if selected_option == 'Rectangulo':
            lenght = self.popup.read_double('Ingrese la base del rectangulo')
            height = self.popup.read_double('Ingrese la altura del rectangulo')

            rectangle = Rectangle(lenght, height)
            self.add_figure2d(rectangle)
            #self.popup.display_results(json_result)
            #self.popup.display_results(f'Area del rectangulo: {rectangle.area}, Perimetro del rectangulo: {rectangle.perimeter}')

        if selected_option == 'Cuadrado':
            side = self.popup.read_double('Ingrese el largo de los lados del cuadrado')
            square = Square(side)
            self.add_figure2d(square)
            #self.popup.display_results(json_result)


            #self.popup.display_results(f'Area del cuadrado: {square.area}, Perimetro del cuadrado: {square.perimeter}')
    
    def select_3dfigure(self):
        options = ['Cuboide', 'Cubo', 'Esfera']
        selected_option = self.popup.read_menu_choice_combobox("Seleccione una figure 3D", options)

        if selected_option == 'Cubo':
            height = self.popup.read_double('Ingrese la altura del cubo')

            cube = Cube(height)
            self.add_figure_3d(cube)
            #self.popup.display_results(json_result)
            
            #self.popup.display_results(f'Volumen del cubo: {cube.volume}, Superficie del cubo: {cube.surface}')
        
        if selected_option == 'Cuboide':
            height = self.popup.read_double('Ingrese la altura del cuboide')
            width = self.popup.read_double('Ingrese la anchura del cuboide')
            length = self.popup.read_double('Ingrese el largo del cuboide')

            cuboid = Cuboid(length, height, width)
            self.add_figure_3d(cuboid)
            #self.popup.display_results(json_result)
            #self.popup.display_results(f'Volumen del cuboide: {cuboid.volume}, Superficie del cuboide: {cuboid.surface}')

        if selected_option == 'Esfera':
            ratio = self.popup.read_double('Ingrese el radio de la esfera')

            sphere = Sphere(ratio)
            self.add_figure_3d(sphere)
            #self.popup.display_results(json_result)
            #self.popup.display_results(f'Volumen de la esfera: {sphere.volume}, Superficie de la esfera: {sphere.surface}')
        
    def display_all_figures(self):
        if self.all_figures:
            all_figures_json = JsonGenerator.figure_to_json(self.all_figures)
            self.popup.display_results(all_figures_json)
        else:
            self.popup.display_results('taylor swift')
    
    def display_2dfigures(self):
        if self.figures2d:
            figures2d = JsonGenerator.figure_to_json(self.figures2d)
            self.popup.display_results(figures2d)
        self.popup.display_results('No se han creado 2d')

    def display_3dfigures(self):
        if self.figures3d:
            figures3d = JsonGenerator.figure_to_json(self.figures3d)
            self.popup.display_results(figures3d)
        self.popup.display_results('No se han creado 3d')
    
    def run(self):
        continuar = True

        while continuar:
            # Definir las opciones del menú
            options = [
                "Agregar Fig. 2D",
                "Agregar Fig. 3D",
                "Consultar Figuras",
                "Consultar Figs. 2D",
                "Consultar Figs. 3D",
                "Salir"
            ]
            selected_option = self.popup.read_menu_choice_combobox('seleccione una opcion', options)

            match selected_option:
                    case -1:
                        self.popup.display_results('Opción invalida')
                    case 'Agregar Fig. 2D':
                        self.select_2dfigure()
                        break
                    case 'Agregar Fig. 3D':
                        self.select_3dfigure()
                        break
                    case 'Consultar Figuras':
                        self.display_all_figures()
                        break
                    case 'Consultar Figs. 2D':
                        self.display_2dfigures()
                        break
                    case 'Consultar Figs. 3D':
                        self.display_3dfigures()
                        break  
                    case 'Salir':
                        continuar = False