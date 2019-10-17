import unittest
import letter_case_permutations as l

class TestNQueens(unittest.TestCase):
    def setUp(self):
        self.example1 = "a1b2"
        self.example2 = "3z4"
        self.example3 = "12345"
        self.example4 = "C"
        self.example5 = ""

    def test_case_1(self):
        expected = ["a1b2", "a1B2", "A1b2", "A1B2"]
        solution = l.Solution()
        result = solution.letterCasePermutation(self.example1)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected = ["3z4", "3Z4"]
        solution = l.Solution()
        result = solution.letterCasePermutation(self.example2)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = ["12345"]
        solution = l.Solution()
        result = solution.letterCasePermutation(self.example3)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = ["c","C"]
        solution = l.Solution()
        result = solution.letterCasePermutation(self.example4)
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected = [""]
        solution = l.Solution()
        result = solution.letterCasePermutation(self.example5)
        self.assertEqual(expected, result)
if __name__ == '__main__':
    unittest.main()