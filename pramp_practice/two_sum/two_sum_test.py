import unittest
import two_sum as t

class TestTwoSum(unittest.TestCase):

    def setUp(self):
        self.example1 = ''
        self.example2 = []
        self.example3 = [1,2,3,4,5]
        self.target3 = 8
        self.example4 = [11,7,2,15]
        self.target4 = 9

    def test_return_type_error_if_first_param_is_not_array(self):
        with self.assertRaises(TypeError):
            t.two_sum(self.example1,1)

    def test_return_type_error_if_second_param_is_not_int(self):
        with self.assertRaises(TypeError):
            t.two_sum(self.example3,0.01)

    def test_return_value_error_if_first_param_is_an_empty_array(self):
        with self.assertRaises(ValueError):
            t.two_sum(self.example2,4)

    def test_return_correct_coordinates(self):
        expected1 = [2,4]
        expected2 = [1,2]

        result1 = t.two_sum(self.example3, self.target3)
        result2 = t.two_sum(self.example4, self.target4)

        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)


if __name__ == '__main__':
    unittest.main()