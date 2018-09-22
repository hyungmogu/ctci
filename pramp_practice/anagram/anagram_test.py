import unittest
import anagram as a


class TestAnagram(unittest.TestCase):

    def setUp(self):
        self.example1 = 'RAIL! SAFETY!'
        self.example2 = 'abcdef'
        self.example3 = ''
        self.example4 = 0

    def test_return_type_error_if_not_string(self):
        with self.assertRaises(TypeError):
            a.anagram(self.example4, 'any string')

        with self.assertRaises(TypeError):
            a.anagram('any string', self.example4)

    def test_return_value_error_if_string_empty(self):
        with self.assertRaises(ValueError):
            a.anagram(self.example3, 'anystring')
        with self.assertRaises(ValueError):
            a.anagram('any string', self.example3)

    def test_return_true_when_anagram(self):
        expected = True
        result = a.anagram(self.example1, 'rail safety')
        self.assertEqual(result, expected)

    def test_return_false_when_not_anagram(self):
        expected = False
        result = a.anagram(self.example2, 'bedfes')
        self.assertEqual(result, expected)


class TestStripSpecialCharacters(unittest.TestCase):
    def setUp(self):
        self.example = 'helloworld'


if __name__ == '__main__':
    unittest.main()