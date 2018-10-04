import unittest
import fibonacci_number as f


class TestFibonacciNumber(unittest.TestCase):
    def setUp(self):
        self.example1 = 4
        self.example2 = -1
        self.example3 = ''
        self.example4 = 0
        self.example5 = 1
        self.example6 = 2

    def test_return_type_error_if_input_not_integer(self):
        memo = {}
        with self.assertRaises(TypeError):
            f.fibonacci_number(self.example3, memo)

    def test_return_value_error_if_input_has_value_less_than_zero(self):
        memo = {}
        with self.assertRaises(ValueError):
            f.fibonacci_number(self.example2, memo)

    def test_return_0_if_n_is_0(self):
        expected = 0
        memo = {}

        result = f.fibonacci_number(self.example4, memo)
        self.assertEqual(expected, result)

    def test_return_1_if_n_is_1(self):
        expected = 1
        memo = {}

        result = f.fibonacci_number(self.example5, memo)
        self.assertEqual(expected, result)

    def test_return_1_if_n_is_2(self):
        expected = 1
        memo = {}

        result = f.fibonacci_number(self.example6, memo)
        self.assertEqual(expected, result)

    def test_return_fibonacci_number(self):
        expected = 3
        memo = {}

        result = f.fibonacci_number(self.example1, memo)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()