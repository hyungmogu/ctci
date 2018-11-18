import unittest
import number_of_paths as n

class TestNumberOfPaths(unittest.TestCase):
    def setUp(self):
        self.example1 = 1
        self.example2 = 2
        self.example3 = 3
        self.example4 = 4
        self.example5 = 6
        self.example6 = 17

    def test_case_1(self):
        expected = 1
        result = n.num_of_paths_to_dest(self.example1)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected = 1
        result = n.num_of_paths_to_dest(self.example2)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = 2
        result = n.num_of_paths_to_dest(self.example3)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = 5
        result = n.num_of_paths_to_dest(self.example4)
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected = 42
        result = n.num_of_paths_to_dest(self.example5)
        self.assertEqual(expected, result)

    def test_case_6(self):
        expected = 35357670
        result = n.num_of_paths_to_dest(self.example6)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()