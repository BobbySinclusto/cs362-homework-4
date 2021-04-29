import unittest
import full_name

class testCubeVolume(unittest.TestCase):
    def test_full_name_good(self):
        self.assertEqual(full_name.full_name('Bobby', 'Sinclusto'), 'Bobby Sinclusto')
        self.assertEqual(full_name.full_name('Greg', 'Todd'), 'Greg Todd')
    
    def test_full_name_fail(self):
        self.assertEqual(full_name.full_name('Bob', 'Tom'), 'Joey Joeman')
    
    def test_full_name_wrong_type(self):
        self.assertRaises(TypeError, full_name.full_name, 4, 5)
        self.assertRaises(TypeError, full_name.full_name, 'Test', ['subject', 2])

if __name__ == '__main__':
    unittest.main()