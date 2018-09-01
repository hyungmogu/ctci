import unittest
import fizzbuzz as fz

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.example1 = 15

    def test_return_fizz_when_divisible_by_3(self):
        expected = 'fizz'

        result = fz.get_fizzbuzz(self.example1)

        for key, result_i in enumerate(result):
            value = key + 1
            if value % 3 == 0 and not value % 15 == 0:
                self.assertEqual(result_i, expected)

    def test_return_fuzz_when_divisible_by_5(self):
        expected = 'buzz'

        result = fz.get_fizzbuzz(self.example1)

        for key, result_i in enumerate(result):
            value = key + 1
            if value % 5 == 0 and not value % 15 == 0:
                self.assertEqual(result_i, expected)

    def test_return_fizzbuzz_when_divisible_by_both_3_and_5(self):
        expected = 'fizzbuzz'

        result = fz.get_fizzbuzz(self.example1)

        for key, result_i in enumerate(result):
            value = key + 1
            if (value % 5 == 0) and (value % 3 == 0):
                self.assertEqual(result_i, expected)


    def test_return_i_when_neither_divisible_by_3_nor_5(self):
        result = fz.get_fizzbuzz(self.example1)

        for key, result_i in enumerate(result):
            value = key + 1
            if not (value % 5 == 0 or value % 3 == 0):
                self.assertEqual(result_i, value)

if __name__ == '__main__':
    unittest.main()
