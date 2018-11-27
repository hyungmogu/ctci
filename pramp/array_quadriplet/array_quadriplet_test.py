import unittest
import array_quadriplet as a

class TestFindArrayQuadriplet(unittest.TestCase):
    def setUp(self):
        self.example1 = []
        self.example2 = [4,4,4]
        self.example3 = [4,4,4,2]
        self.example4 = [4,4,4,4]
        self.example5 = [2,7,4,0,9,5,1,3]
        self.example6 = [2,7,4,0,9,5,1,3]
        self.example7 = [1,2,3,4,5,9,19,12,12,19]

    def test_case_1(self):
        expected = []
        result = a.find_array_quadruplet(self.example1,12)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected = []
        result = a.find_array_quadruplet(self.example2,12)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = []
        result = a.find_array_quadruplet(self.example3,16)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = [4,4,4,4]
        result = a.find_array_quadruplet(self.example4,16)
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected = [0,4,7,9]
        result = a.find_array_quadruplet(self.example5,20)
        self.assertEqual(expected, result)

    def test_case_6(self):
        expected = []
        result = a.find_array_quadruplet(self.example6,120)
        self.assertEqual(expected, result)

    def test_case_7(self):
        expected = [4,5,12,19]
        result = a.find_array_quadruplet(self.example7,40)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()