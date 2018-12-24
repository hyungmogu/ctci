import unittest
import root_of_a_number as r


class TestRootOfANumber(unittest.TestCase):

    def setUp(self):
        self.example1 = 4
        self.example2 = 7
        self.example3 = 9
        self.example4 = 0.2
        self.example5 = 0
        self.example6 = 1

    def test_case1(self):
        expected = 2.0
        result = r.root(self.example1, 2)
        self.assertEqual(result, expected)

    def test_case2(self):
        expected = 1.913
        result = r.root(self.example2, 3)
        self.assertEqual(result, expected)

    def test_case3(self):
        expected = 2.080
        result = r.root(self.example3, 3)
        self.assertEqual(result,expected)

    def test_case4(self):
        expected = 0.447
        result = r.root(self.example4, 2)
        self.assertEqual(result, expected)

    def test_case5(self):
        expected = 0
        result = r.root(self.example5, 2)
        self.assertEqual(result,expected)

    def test_case6(self):
        expected = 1
        result = r.root(self.example6, 10)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()