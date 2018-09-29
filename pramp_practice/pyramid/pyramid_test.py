import unittest
import pyramid as p


class TestPrintPyramid(unittest.TestCase):
    def setUp(self):
        self.example1 = ''
        self.example2 = 0

    def test_return_type_error_if_input_outher_than_int_is_given(self):
        with self.assertRaises(TypeError):
            p.print_pyramid(self.example1)

    def test_return_value_error_if_0_given(self):
        with self.assertRaises(ValueError):
            p.print_pyramid(self.example2)

class TestGeneratePyramid(unittest.TestCase):
    def setUp(self):
        self.example1 = 3
        self.example2 = 4

    def test_return_array_of_hash_tags_given_steps(self):
        expected1 = ['  #  ', ' ### ', '#####']
        expected2 = ['   #   ', '  ###  ', ' ##### ', '#######']

        result1 = p.get_pyramid(self.example1)
        result2 = p.get_pyramid(self.example2)

        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)

if __name__ == '__main__':
    unittest.main()