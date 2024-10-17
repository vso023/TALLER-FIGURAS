import unittest
from figures3d.cube import Cube
from figures3d.cuboid import Cuboid
from figures3d.sphere import Sphere

class TestFigures3d(unittest.TestCase):

    def test_cube_volume(self):
        cube = Cube(5)
        self.assertAlmostEqual(cube.volume(), 125)

    def test_cube_surface(self):
        cube = Cube(5)
        self.assertAlmostEqual(cube.surface(), 150)

    def test_cuboid_volume(self):
        cuboid = Cuboid(4, 5, 6)
        self.assertEqual(cuboid.volume(), 120)

    def test_cuboid_surface(self):
        cuboid = Cuboid(4, 5, 6)
        self.assertEqual(cuboid.surface(), 148)

    def test_sphere_volume(self):
        sphere = Sphere(5)
        self.assertAlmostEqual(sphere.volume(), 523.5983333333332)

    def test_sphere_surface(self):
        sphere = Sphere(5)
        self.assertAlmostEqual(sphere.surface(), 314.159)

    def test_to_dict_cube(self):
        cube = Cube(5)
        expected_dict = {
            "tipo": "Cubo",
            "id": cube.id,
            "altura": 5,
            "volumen": cube.volume(),
            "superficie": cube.surface()
        }
        self.assertEqual(cube.to_dict(), expected_dict)

if __name__ == "__main__":
    unittest.main()

    
