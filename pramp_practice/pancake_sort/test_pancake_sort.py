import unittest
import pancake_sort as p


class TestPancakeSort(unittest.TestCase):
    def setUp(self):
        self.example1 = [1,3,1]

    def test_return_sorted_array(self):
        expected = [1,1,3]

        result = p.pancake_sort(self.example1)

        self.assertEqual(result, expected)

class TestFlip(unittest.TestCase):
    def setUp(self):
        self.example1 = [1,2,3,4,5]

    def test_return_first_value_as_4_after_flipping_k_is_3(self):
        expected = 4

        result = p.flip(self.example1, 4)

        self.assertEqual(result[0], expected)

class TestPanckaeSort(unittest.TestCase):
    def setUp(self):
        self.example1 = [1,2,3,4,5]

    def test_return_3_if_i_is_4(self):
        expected = 4

        result = p.get_max_index_value(self.example1, 4)

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()