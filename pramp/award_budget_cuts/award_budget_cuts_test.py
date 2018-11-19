import unittest
import award_budget_cuts as a

class TestFindGrantsCap(unittest.TestCase):
    def setUp(self):
        self.example1 = [2,4]
        self.example2 = [2,4,6]
        self.example3 = [2,100,50,120,167]
        self.example4 = [2,100,50,120,1000]
        self.example5 = [21,100,50,120,130,110]
        self.example6 = [210,200,150,193,130,110,209,342,117]

    def test_case_1(self):
        expected = 1.5
        result = a.find_grants_cap(self.example1,3)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected = 1
        result = a.find_grants_cap(self.example2,3)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = 128
        result = a.find_grants_cap(self.example3,400)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = 47
        result = a.find_grants_cap(self.example4,190)
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected = 23.8
        result = a.find_grants_cap(self.example5,140)
        self.assertEqual(expected, result)

    def test_case_6(self):
        expected = 211
        result = a.find_grants_cap(self.example6,1530)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()