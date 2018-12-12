import unittest
import permutations as p


class TestPermutations(unittest.TestCase):
    def setUp(self):
        self.example1 = [1]
        self.example2 = [1,2,3]
        self.example3 = []

    def test_case_1(self):
        expected = [[1]]
        solution = p.Solution()
        result = solution.permute(self.example1)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
        solution = p.Solution()
        result = solution.permute(self.example2)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = [[]]
        solution = p.Solution()
        result = solution.permute(self.example3)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()