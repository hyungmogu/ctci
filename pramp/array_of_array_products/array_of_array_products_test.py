import unittest
import array_of_array_products as a

class TestArrayOfArrayProducts(unittest.TestCase):
    def setUp(self):
        self.example1 = []
        self.example2 = [1]
        self.example3 = [2,2]
        self.example4 = [2,7,3,4]
        self.example5 = [2,3,0,982,10]
        self.example6 = [-3,17,430,-6,5,-12,-11,5]

    def test_case_1(self):
        expected = []
        result = a.array_of_array_products(self.example1)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected = []
        result = a.array_of_array_products(self.example2)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = [2,2]
        result = a.array_of_array_products(self.example3)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = [84,24,56,42]
        result = a.array_of_array_products(self.example4)
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected = [0,0,58920,0,0]
        result = a.array_of_array_products(self.example5)
        self.assertEqual(expected, result)

    def test_case_6(self):
        expected = [-144738000,25542000,1009800,-72369000,86842800,-36184500,-39474000,86842800]
        result = a.array_of_array_products(self.example6)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()