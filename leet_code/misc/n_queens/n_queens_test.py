import unittest
import n_queens as n

class TestNQueens(unittest.TestCase):
    def setUp(self):
        self.example1 = 1
        self.example2 = 0
        self.example3 = 4

    def test_case_1(self):
        expected = [["Q"]]
        solution = n.Solution()
        result = solution.solveNQueens(self.example1)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected = []
        solution = n.Solution()
        result = solution.solveNQueens(self.example2)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
        solution = n.Solution()
        result = solution.solveNQueens(self.example3)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()