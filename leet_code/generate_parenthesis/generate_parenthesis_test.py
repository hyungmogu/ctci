import unitest
import generate_parenthesis as g


class TestGenerateParenthesis(unittest.TestCase):
    def setUp(self):
        self.example1 = 1
        self.example2 = 2
        self.example3 = 4
        self.example4 = 0

    def test_case_1(self):
        expected = ["()"]
        solution = g.Solution()
        result = solution.generateParenthesis(self.example1)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected = ["(())", "()()"]
        solution = g.Solution()
        result = solution.generateParenthesis(self.example2)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        solution = g.Solution()
        result = solution.generateParenthesis(self.example3)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = []
        solution = g.Solution()
        result = solution.generateParenthesis(self.example3)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()