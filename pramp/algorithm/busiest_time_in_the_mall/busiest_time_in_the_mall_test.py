import unittest
import busiest_time_in_the_mall as b

class TestFindBusiestPeriod(unittest.TestCase):
    def setUp(self):
        self.example1 = [[1487799426,21,1]]
        self.example2 = [[1487799425,21,0],[1487799427,22,1],[1487901318,7,0]]
        self.example3 = [[1487799425,21,1],[1487799425,4,0],[1487901318,7,0]]
        self.example4 = [[1487799425,14,1],[1487799425,4,0],[1487799425,2,0],[1487800378,10,1],[1487801478,18,0],[1487801478,18,1],[1487901013,1,0],[1487901211,7,1],[1487901211,7,0]]
        self.example5 = [[1487799425,14,1],[1487799425,4,1],[1487799425,2,1],[1487800378,10,1],[1487801478,18,1],[1487901013,1,1],[1487901211,7,1],[1487901211,7,1]]
        self.example6 = [[1487799425,14,1],[1487799425,4,0],[1487799425,2,0],[1487800378,10,1],[1487801478,18,0],[1487801478,19,1],[1487801478,1,0],[1487801478,1,1],[1487901013,1,0],[1487901211,7,1],[1487901211,8,0]]

    def test_case_1(self):
        expected = 1487799426
        result = b.find_busiest_period(self.example1)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected = 1487799427
        result = b.find_busiest_period(self.example2)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = 1487799425
        result = b.find_busiest_period(self.example3)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = 1487800378
        result = b.find_busiest_period(self.example4)
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected = 1487901211
        result = b.find_busiest_period(self.example5)
        self.assertEqual(expected, result)

    def test_case_6(self):
        expected = 1487801478
        result = b.find_busiest_period(self.example6)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()