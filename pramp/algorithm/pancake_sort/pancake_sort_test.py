import unittest
import pancake_sort as p

class TestPancakeSort(unittest.TestCase):
    def setUp(self):
        self.example1 = [1]
        self.example2 = [1,2]
        self.example3 = [1,3,1]
        self.example4 = [3,1,2,4,6,5]
        self.example5 = [10,9,8,7,6,5,4,3,2,1]
        self.example6 = [10,9,8,6,7,5,4,3,2,1,9,10,8,7,6,5,4,3,2,1,10,9,8,7,6,5,4,3,2,1]

    def test_case_1(self):
        expected = [1]
        result = p.pancake_sort(self.example1)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected = [1,2]
        result = p.pancake_sort(self.example2)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected =  [1, 1, 3]
        result = p.pancake_sort(self.example3)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected =  [1,2,3,4,5,6]
        result = p.pancake_sort(self.example4)
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected = [1,2,3,4,5,6,7,8,9,10]
        result =  p.pancake_sort(self.example5)
        self.assertEqual(expected, result)

    def test_case_6(self):
        expected = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]
        result =  p.pancake_sort(self.example6)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()