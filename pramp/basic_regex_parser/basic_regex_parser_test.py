import unittest
import basic_regex_parser as b

class TestReverseWords(unittest.TestCase):
    def setUp(self):
        self.example1_1 = ""
        self.example1_2 = ""
        self.example2_1 = "aa"
        self.example2_2 = "a"
        self.example3_1 = "bb"
        self.example3_2 = "bb"
        self.example4_1 = ""
        self.example4_2 = "a*"
        self.example5_1 = "abbdbb"
        self.example5_2 = "ab*d"
        self.example6_1 = "aba"
        self.example6_2 = "a.a"
        self.example7_1 = "acd"
        self.example7_2 = "ab*c."
        self.example8_1 = "abaa"
        self.example8_2 = "a.*a*"

    def test_case_1(self):
        expected =  True
        result = b.is_match(self.example1_1, self.example1_2)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected =  False
        result = b.is_match(self.example2_1, self.example2_2)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = True
        result = b.is_match(self.example3_1, self.example3_2)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = True
        result = b.is_match(self.example4_1, self.example4_2)
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected = False
        result = b.is_match(self.example5_1, self.example5_2)
        self.assertEqual(expected, result)

    def test_case_6(self):
        expected = True
        result = b.is_match(self.example6_1, self.example6_2)
        self.assertEqual(expected, result)

    def test_case_7(self):
        expected = True
        result = b.is_match(self.example7_1, self.example7_2)
        self.assertEqual(expected, result)

    def test_case_8(self):
        expected = True
        result = b.is_match(self.example8_1, self.example8_2)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()