import unittest
import getting_different_number as g

class TestReverseWords(unittest.TestCase):
    def setUp(self):
        self.example1 = [0]
        self.example2 = [0,1,2]
        self.example3 = [1,3,0,2]
        self.example4 = [100000]
        self.example5 = [1,0,3,4,5]
        self.example6 = [0,100000]

    def test_case_1(self):
        expected =  1
        result = g.get_different_number(self.example1)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected =  3
        result = g.get_different_number(self.example2)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = 4
        result = g.get_different_number(self.example3)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = 0
        result = g.get_different_number(self.example4)
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected =  2
        result = g.get_different_number(self.example5)
        self.assertEqual(expected, result)

    def test_case_6(self):
        expected = 1
        result = g.get_different_number(self.example6)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()