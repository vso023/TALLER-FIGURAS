import unittest
from figures2d.circle import Circle
from figures2d.rectangle import Rectangle

class TestFigures2d(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53975)

    def test_circle_perimeter(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.perimeter(), 31.4159)

    def test_rectangle_area(self):
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)

    def test_rectangle_perimeter(self):
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.perimeter(), 18)

    def test_to_dict_circle(self):
        circle = Circle(5)
        expected_dict = {
            "tipo": "Circulo",
            "id": circle.id,
            "ratio": 5,
            "area": circle.area(),
            "perimetro": circle.perimeter()
        }
        self.assertEqual(circle.to_dict(), expected_dict)

        

    
