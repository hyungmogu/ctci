import unittest
import palindrome as p


class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.example1 = 'aba'
        self.example2 = 'abba'
        self.example3 = 'abcdef'
        self.example4 = ''
        self.example5 = 0

    def test_return_type_error_if_not_string(self):
        with self.assertRaises(TypeError):
            p.is_palindrome(self.example5)

    def test_return_value_error_if_input_is_an_empty_string(self):
        with self.assertRaises(ValueError):
            p.is_palindrome(self.example4)

    def test_return_false_if_not_palindrome(self):
        expected = False

        result = p.is_palindrome(self.example3)

        self.assertEqual(expected, result)

    def test_return_true_if_palindrome(self):
        expected = True

        result1 = p.is_palindrome(self.example2)
        result2 = p.is_palindrome(self.example1)

        self.assertEqual(expected, result1)
        self.assertEqual(expected, result2)

if __name__ == '__main__':
    unittest.main()
