import unittest
import sentence_reverse as s

class TestReverseWords(unittest.TestCase):
    def setUp(self):
        self.example1 = [" "," "]
        self.example2 = ["a"," "," ","b"]
        self.example3 = ["h","e","l","l","o"]
        self.example4 = ["p","e","r","f","e","c","t"," ","m","a","k","e","s"," ","p","r","a","c","t","i","c","e"]
        self.example5 = ["y","o","u"," ","w","i","t","h"," ","b","e"," ","f","o","r","c","e"," ","t","h","e"," ","m","a","y"]
        self.example6 = ["g","r","e","a","t","e","s","t"," ","n","a","m","e"," ","f","i","r","s","t"," ","e","v","e","r"," ","n","a","m","e"," ","l","a","s","t"]

    def test_case_1(self):
        expected =  [" "," "]
        result = s.reverse_words(self.example1)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected =  ["b"," "," ","a"]
        result = s.reverse_words(self.example2)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = ["h","e","l","l","o"]
        result = s.reverse_words(self.example3)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = ["p","r","a","c","t","i","c","e"," ","m","a","k","e","s"," ","p","e","r","f","e","c","t"]
        result = s.reverse_words(self.example4)
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected =  ["m","a","y"," ","t","h","e"," ","f","o","r","c","e"," ","b","e"," ","w","i","t","h"," ","y","o","u"]
        result = s.reverse_words(self.example5)
        self.assertEqual(expected, result)

    def test_case_6(self):
        expected = ["l","a","s","t"," ","n","a","m","e"," ","e","v","e","r"," ","f","i","r","s","t"," ","n","a","m","e"," ","g","r","e","a","t","e","s","t"]
        result = s.reverse_words(self.example6)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()