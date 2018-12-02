import unittest
import find_the_duplicates as f

class TestReverseWords(unittest.TestCase):
    def setUp(self):
        self.example1_1 = [11]
        self.example1_2 = [11]
        self.example2_1 = [1,3,5,9]
        self.example2_2 = [2,4,6,10]
        self.example3_1 = [1,2,3,5,6,7]
        self.example3_2 = [3,6,7,8,20]
        self.example4_1 = [1,2,3,5,6,7]
        self.example4_2 = [7,8,9,10,11,12]
        self.example5_1 = [10,20,30,40,50,60,70,80]
        self.example5_2 = [10,20,30,40,50,60]
        self.example6_1 = [10,20,30,40,50,60,70]
        self.example6_2 = [10,20,30,40,50,60,70]

    def test_case_1(self):
        expected =  [11]
        result = f.find_duplicates(self.example1_1, self.example1_2)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected =  []
        result = f.find_duplicates(self.example2_1, self.example2_2)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = [3,6,7]
        result = f.find_duplicates(self.example3_1, self.example3_2)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = [7]
        result = f.find_duplicates(self.example4_1, self.example4_2)
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected = [10,20,30,40,50,60]
        result = f.find_duplicates(self.example5_1, self.example5_2)
        self.assertEqual(expected, result)

    def test_case_6(self):
        expected = [10,20,30,40,50,60,70]
        result = f.find_duplicates(self.example6_1, self.example6_2)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()