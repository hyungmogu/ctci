import unittest
import merge_sort as m

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.example1 = ''

        self.example2 = [{},['a','b'],1,2,False]

        self.example3 = []

        self.example4 = [4,2,1,2,5]

    def test_return_type_error_if_input_is_not_array(self):
        with self.assertRaises(TypeError):
            m.merge_sort('')

    def test_return_value_error_if_array_elements_are_not_basic_data_types(self):
        with self.assertRaises(ValueError):
            m.merge_sort(self.example2)

    def test_return_empty_array_if_array_has_no_elements(self):
        expected = []

        result = m.merge_sort(self.example3)

        self.assertEqual(expected, result)

    def test_return_array_with_items_in_sorted_order(self):
        expected = [1,2,2,4,5]

        result = m.merge_sort(self.example4)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()