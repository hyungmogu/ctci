import unittest
import root_of_a_number as r


class TestRootOfANumber(unittest.TestCase):

    def setUp(self):
        self.example1 = 4
        self.example2 = 7
        self.example3 = 9
        self.example4 = 0.2

    def test_result_when_rooting_value_greater_than_1(self):
        expected = 1.913

        result = r.root(self.example2, 3)

        self.assertEqual(result, expected)

    def test_return_result_when_rooting_decimals(self):
        expected = 0.447

        result = r.root(self.example4, 2)

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()