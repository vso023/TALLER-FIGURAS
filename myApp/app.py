"Module that contains the App class"
import json
from figures2d.circle import Circle
from figures2d.rectangle import Rectangle
from figures2d.square import Square
from figures3d.cube import Cube
from figures3d.cuboid import Cuboid
from figures3d.sphere import Sphere
from popUp.popUp import PopUp

class App:
    "Class that represents the application"
    def __init__(self):
        self.popup = PopUp()
        self.all_figures = []
        self.figures2d = []
        self.figures3d = []

    def add_figure2d(self, figure):
        "Function that adds a 2D figure to the list of 2D figures"
        self.figures2d.append(figure)
        self.all_figures.append(figure)
        self.popup.display_results(f"Figura 2D agregada: {figure.to_json()}")

    def add_figure_3d(self, figure):
        "Function that adds a 3D figure to the list of 3D figures"
        self.figures3d.append(figure)
        self.all_figures.append(figure)
        self.popup.display_results(f"Figura 3D agregada: {figure.to_json()}")

    def display_all_figures(self):
        "Function that displays all the figures created"
        if self.all_figures:
            all_figures_json = json.dumps([json.loads(figure.to_json()) for figure in self.all_figures])
            self.popup.display_results(all_figures_json)
        else:
            self.popup.display_results('No hay figuras creadas.')

    def display_2dfigures(self):
        "Function that displays all the 2D figures created"
        if self.figures2d:
            figures2d_json = json.dumps([json.loads(figure.to_json()) for figure in self.figures2d])
            self.popup.display_results(figures2d_json)
        else:
            self.popup.display_results('No se han creado figuras 2D.')

    def display_3dfigures(self):
        "Function that displays all the 3D figures created"
        if self.figures3d:
            figures3d_json = json.dumps([json.loads(figure.to_json()) for figure in self.figures3d])
            self.popup.display_results(figures3d_json)
        else:
            self.popup.display_results('No se han creado figuras 3D.')

    def select_2dfigure(self):
        "Function that allows the user to select a 2D figure to create"
        options = ['Circulo', 'Rectangulo', 'Cuadrado']
        selected_option = self.popup.read_menu_choice_string("Circulo", options)

        if selected_option == 'Circulo':
            ratio = self.popup.read_int_greater_than('Ingrese el radio del círculo')
            circle = Circle(ratio)
            self.add_figure2d(circle)

        elif selected_option == 'Rectangulo':
            length = self.popup.read_int_greater_than('Ingrese la base del rectángulo')
            height = self.popup.read_int_greater_than('Ingrese la altura del rectángulo')
            rectangle = Rectangle(length, height)
            self.add_figure2d(rectangle)

        elif selected_option == 'Cuadrado':
            side = self.popup.read_int_greater_than('Ingrese el largo de los lados del cuadrado')
            square = Square(side)
            self.add_figure2d(square)

    def select_3dfigure(self):
        "Function that allows the user to select a 3D figure to create"
        options = ['Cuboide', 'Cubo', 'Esfera']
        selected_option = self.popup.read_menu_choice_string("Esfera", options)

        if selected_option == 'Cubo':
            height = self.popup.read_int_greater_than('Ingrese la altura del cubo')
            cube = Cube(height)
            self.add_figure_3d(cube)

        elif selected_option == 'Cuboide':
            height = self.popup.read_int_greater_than('Ingrese la altura del cuboide')
            width = self.popup.read_int_greater_than('Ingrese la anchura del cuboide')
            length = self.popup.read_int_greater_than('Ingrese el largo del cuboide')
            cuboid = Cuboid(length, height, width)
            self.add_figure_3d(cuboid)

        elif selected_option == 'Esfera':
            ratio = self.popup.read_int_greater_than('Ingrese el radio de la esfera')
            sphere = Sphere(ratio)
            self.add_figure_3d(sphere)

    def run(self):
        "Function that runs the application"
        continuar = True
        while continuar:
            options = [
                "Agregar Fig. 2D",
                "Agregar Fig. 3D",
                "Consultar Figuras",
                "Consultar Figs. 2D",
                "Consultar Figs. 3D",
                "Salir"
            ]
            selected_option = self.popup.read_menu_choice_string("Agregar Fig. 2D", options)

            match selected_option:
                case 'Agregar Fig. 2D':
                    self.select_2dfigure()
                case 'Agregar Fig. 3D':
                    self.select_3dfigure()
                case 'Consultar Figuras':
                    self.display_all_figures()
                case 'Consultar Figs. 2D':
                    self.display_2dfigures()
                case 'Consultar Figs. 3D':
                    self.display_3dfigures()
                case 'Salir':
                    if self.popup.yes_or_no('deseas salir?'):
                        continuar = False
                case _:
                    self.popup.display_results('Opción inválida')


