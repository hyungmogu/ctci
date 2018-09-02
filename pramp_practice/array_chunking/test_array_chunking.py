import unittest
import array_chunking as a

class TestArrayChunking(unittest.TestCase):

    def setUp(self):
        self.example1 = [1,2,3,4,5,6,7,8]
        self.example2 = [1,2,4,5,7,8]
        self.example3 = [1,2,3,4]

    def test_return_type_error_if_input_for_array_is_other_than_array(self):
        with self.assertRaises(TypeError):
            a.array_chunking(0,3)

    def test_return_type_error_if_input_for_subarray_size_is_other_than_0(self):
        with self.assertRaises(TypeError):
            a.array_chunking([1,2,3,4,5],'hello world')

    def test_return_value_error_if_array_is_empty(self):
        with self.assertRaises(ValueError):
            a.array_chunking([],3)

    def test_return_value_error_if_subarray_size_is_less_than_1(self):
        with self.assertRaises(ValueError):
            a.array_chunking([1,2,3,4,5],-1)

    def test_return_subarrays_of_subarray_size(self):
        expected1 = [[1,2,3],[4,5,6],[7,8]]
        expected2 = [[1,2],[4,5],[7,8]]
        expected3 = [[1],[2],[3],[4]]

        result1 = a.array_chunking(self.example1, 3)
        result2 = a.array_chunking(self.example2, 2)
        result3 = a.array_chunking(self.example3, 1)

if __name__ == '__main__':
    unittest.main()