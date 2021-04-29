import unittest
import list_avg

class testListAvg(unittest.TestCase):
    def test_list_avg_good(self):
        self.assertEqual(list_avg.list_avg([3, 4, 5, 6]), 4.5)
        self.assertEqual(list_avg.list_avg([-3.5,3.5]), 0)
    
    def test_list_avg_fail(self):
        self.assertEqual(list_avg.list_avg([3,3,3]), 1)
    
    def test_list_avg_empty(self):
        self.assertRaises(ValueError, list_avg.list_avg, [])
    
    def test_list_avg_wrong_type(self):
        self.assertRaises(TypeError, list_avg.list_avg, [3, 4, 'asdf'])
        self.assertRaises(TypeError, list_avg.list_avg, ['203', '101', '3'])

if __name__ == '__main__':
    unittest.main()