import unittest
import capitalize_letter as c


class TestCapitalizeLetter(unittest.TestCase):
    def setUp(self):
        self.example1 = 0
        self.example2 = ''
        self.example3 = 'hello'
        self.example4 = '!ello'
        self.example5 = 'hello  world'

    def test_return_type_error_given_wrong_input_type(self):
        with self.assertRaises(TypeError):
            c.capitalize_letter(self.example1)

    def test_return_value_error_given_empty_string(self):
        with self.assertRaises(ValueError):
            c.capitalize_letter(self.example2)

    def test_return_first_letter_must_be_uppercase(self):
        expected = 'Hello'
        result = c.capitalize_letter(self.example3)
        self.assertEqual(expected, result)

    def test_return_should_turn_first_letter_after_space_to_uppercase(self):
        expected = 'Hello  World'
        result = c.capitalize_letter(self.example5)
        self.assertEqual(expected, result)

    def test_return_word_other_than_alphabet_should_do_nothing(self):
        expected = self.example4
        result = c.capitalize_letter(self.example4)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()