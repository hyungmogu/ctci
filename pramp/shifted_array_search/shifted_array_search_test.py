import unittest
import shifted_array_search as s

class TestShiftedArraySearch(unittest.TestCase):
    def setUp(self):
        self.example1 = [2]
        self.example2 = [1,2]
        self.example3 = [0,1,2,3,4,5]
        self.example4 = [1,2,3,4,5,0]
        self.example5 = [9,12,17,2,4,5]
        self.example6 = [9,12,17,2,4,5,6]

    def test_case_1(self):
        expected = 0
        result = s.shifted_arr_search(self.example1,2)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected = 1
        result = s.shifted_arr_search(self.example2,2)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = 1
        result = s.shifted_arr_search(self.example3,1)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = 5
        result = s.shifted_arr_search(self.example4,0)
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected = 2
        result = s.shifted_arr_search(self.example5,17)
        self.assertEqual(expected, result)

    def test_case_6(self):
        expected = 4
        result = s.shifted_arr_search(self.example6,4)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()