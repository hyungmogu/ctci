import unittest
import two_sum as t

class TestFindGrantsCap(unittest.TestCase):
    def setUp(self):
        self.example1 = [2,7,11,15]
        self.example2 = []
        self.example3 = [0]
        self.example4 = [1,2]
        self.example5 = [11,7,8,5]

    def test_case_1(self):
        expected = [0,1]
        result = t.two_sum(self.example1,9)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected = [1,3]
        result = t.two_sum(self.example1,22)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = []
        result = t.two_sum(self.example2,400)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = []
        result = t.two_sum(self.example3,190)
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected = []
        result = t.two_sum(self.example4,4)
        self.assertEqual(expected, result)

    def test_case_6(self):
        expected = [1,3]
        result = t.two_sum(self.example5,12)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()