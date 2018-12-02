import unittest
import pairs_with_specific_difference as p

class TestFindPairsWithGivenDifferenceBruteForce(unittest.TestCase):
    def setUp(self):
        self.example1_arr = []
        self.example1_k = 10

        self.example2_arr = [1]
        self.example2_k = 12

        self.example3_arr = [0, -1, -2, 2, 1]
        self.example3_k = 24

        self.example4_arr = [0, -1, -2, 2, 1]
        self.example4_k = 1

    def test_return_empty_list_if_input_is_list_without_elements(self):
        expected = []

        result = p.find_pairs_with_given_difference_brute_force(self.example1_arr, self.example1_k)

        self.assertEqual(result, expected)

    def test_return_empty_list_if_input_is_list_with_only_one_element(self):
        expected = []

        result = p.find_pairs_with_given_difference_brute_force(self.example2_arr, self.example2_k)

        self.assertEqual(result, expected)

    def test_return_empty_list_if_no_pairs_exist(self):
        expected =[]

        result = p.find_pairs_with_given_difference_brute_force(self.example3_arr, self.example3_k)

        self.assertEqual(result, expected)

    def test_return_pairs_with_given_difference_if_exists(self):
        expected = [[1, 0], [0, -1], [-1, -2], [2, 1]]

        result = p.find_pairs_with_given_difference_brute_force(self.example4_arr, self.example4_k)


class TestFindPairsWithGivenDifferenceImproved(unittest.TestCase):
    def setUp(self):
        self.example1_arr = []
        self.example1_k = 10

        self.example2_arr = [1]
        self.example2_k = 12

        self.example3_arr = [0, -1, -2, 2, 1]
        self.example3_k = 24

        self.example4_arr = [0, -1, -2, 2, 1]
        self.example4_k = 1

    def test_return_empty_list_if_input_is_list_without_elements(self):
        expected = []

        result = p.find_pairs_with_given_difference_improved(self.example1_arr, self.example1_k)

        self.assertEqual(result, expected)

    def test_return_empty_list_if_input_is_list_with_only_one_element(self):
        expected = []

        result = p.find_pairs_with_given_difference_improved(self.example2_arr, self.example2_k)

        self.assertEqual(result, expected)

    def test_return_empty_list_if_no_pairs_exist(self):
        expected =[]

        result = p.find_pairs_with_given_difference_improved(self.example3_arr, self.example3_k)

        self.assertEqual(result, expected)

    def test_return_pairs_with_given_difference_if_exists(self):
        expected = [[1, 0], [0, -1], [-1, -2], [2, 1]]

        result = p.find_pairs_with_given_difference_improved(self.example4_arr, self.example4_k)

if __name__ == '__main__':
    unittest.main()