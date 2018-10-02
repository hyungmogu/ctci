import unittest
import matrix_spiral as m

class TestMatrixSpiral(unittest.TestCase):
    def setUp(self):
        self.example1 = 2
        self.example2 = 3
        self.example3 = 0
        self.example4 = 'asd'

    def test_return_type_error_if_input_is_not_int(self):
        with self.assertRaises(TypeError):
            m.matrix_spiral(self.example4)

    def test_return_value_error_if_input_is_less_than_0(self):
        with self.assertRaises(ValueError):
            m.matrix_spiral(self.example3)

    def test_return_matrix_spiral(self):
        expected1 = [[1, 2], [4, 3]]
        expected2 = [[1,2,3], [8,9,4], [7,6,5]]

        result1 = m.matrix_spiral(self.example1)
        result2 = m.matrix_spiral(self.example2)

        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)


if __name__ == '__main__':
    unittest.main()