import unittest
import cube_volume

class testCubeVolume(unittest.TestCase):
    def test_cube_volume_good(self):
        self.assertEqual(cube_volume.cube_volume(3), 27)
        self.assertAlmostEqual(cube_volume.cube_volume(4.4), 85.184)
    
    def test_cube_volume_fail(self):
        self.assertEqual(cube_volume.cube_volume(3), 2)
    
    def test_cube_volume_complex(self):
        self.assertRaises(TypeError, cube_volume.cube_volume, 3j)
        self.assertRaises(TypeError, cube_volume.cube_volume, 9j + 5)
    
    def test_cube_volume_negative(self):
        self.assertRaises(ValueError, cube_volume.cube_volume, -2)
        self.assertRaises(ValueError, cube_volume.cube_volume, -2.2)

if __name__ == '__main__':
    unittest.main()