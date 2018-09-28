import unittest
import printing_steps as p


class TestPrintSteps(unittest.TestCase):
    def setUp(self):
        self.example1 = 0
        self.example2 = 'hello world'

    def test_return_type_error_if_wrong_input_type_registered(self):
        with self.assertRaises(TypeError):
            p.print_steps(self.example2)

    def test_return_value_error_if_no_steps_defined(self):
        with self.assertRaises(ValueError):
            p.print_steps(self.example1)


class TestGetSteps(unittest.TestCase):
    def setUp(self):
        self.example1 = 4
        self.example2 = 5
        self.example3 = 1

    def test_return_get_steps(self):
        expected1 = ['#', '##', '###', '####']
        expected2 = ['#', '##', '###', '####', '#####']
        expected3 = ['#']

        result1 = p.get_steps(self.example1)
        result2 = p.get_steps(self.example2)
        result3 = p.get_steps(self.example3)

        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)


if __name__ == '__main__':
    unittest.main()