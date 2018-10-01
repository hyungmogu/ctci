import unittest
import get_your_vowels as g

class TestGetYourVowels(unittest.TestCase):
    def setUp(self):
        self.example1 = 'Hi There!'
        self.example2 = 'Why do you ask?'
        self.example3 = 'Why?'
        self.example4 = ''
        self.example5 = 0

    def test_return_type_error_if_input_is_other_than_string(self):
        with self.assertRaises(TypeError):
            g.get_your_vowels(self.example5)

    def test_return_value_error_if_input_is_emtpy(self):
        with self.assertRaises(ValueError):
            g.get_your_vowels(self.example4)

    def test_retrun_number_of_vowels(self):
        expected1 = 3
        expected2 = 4
        expected3 = 0

        result1 = g.get_your_vowels(self.example1)
        result2 = g.get_your_vowels(self.example2)
        result3 = g.get_your_vowels(self.example3)

        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)


if __name__ == '__main__':
    unittest.main()