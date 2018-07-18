import unittest
import string_compression as s

class TestStringCompression(unittest.TestCase):
    def test_compressString(self):
        self.assertEqual(s.compress_string("a"), "a")
        self.assertEqual(s.compress_string("ab"), "ab")
        self.assertEqual(s.compress_string("bb"), "bb")
        self.assertEqual(s.compress_string("bcb"), "bcb")
        self.assertEqual(s.compress_string("bbb"), "b3")
        self.assertEqual(s.compress_string("bbaabcccccaaa"), "b2a2bc5a3")
        self.assertEqual(s.compress_string("abcdefg"), "abcdefg")

if __name__ == "__main__":
	unittest.main()
