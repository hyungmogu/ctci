import unittest
import number_of_paths as n

class TestNumberOfPaths(unittest.TestCase):
    def setUp(self):
        self.example1 = [9]
        self.example2 = [4,4]
        self.example3 = [4,4,1]
        self.example4 = [4,6,10,15,16]
        self.example5 = [4,6,10,15,16]
        self.example6 = [12,6,7,14,,19,3,0,25,40]

    def test_case_1(self):
        expected = []
        result = m.get_indices_of_item_wights(self.example1,9)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected = [1,0]
        result = m.get_indices_of_item_wights(self.example2,8)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = [2,1]
        result = m.get_indices_of_item_wights(self.example3,5)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = [3,1]
        result = m.get_indices_of_item_wights(self.example4,21)
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected = [4,0]
        result = m.get_indices_of_item_wights(self.example5,20)
        self.assertEqual(expected, result)

    def test_case_6(self):
        expected = [6,2]
        result = m.get_indices_of_item_wights(self.example6,7)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()