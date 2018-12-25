import decrypt_message as d
import unittest

class TestDecryptMessage(unittest.TestCase):
    def setUp(self):
        self.example1 = ''
        self.example2 = 'bvq'
        self.example3 = 'dnotq'
        self.example4 = 'flgxswdliefy'

    def test_case1(self):
        expected = ''
        result = d.decrypt(self.example1)
        self.assertEqual(result, expected)

    def test_case2(self):
        expected = 'abc'
        result = d.decrypt(self.example2)
        self.assertEqual(result, expected)

    def test_case3(self):
        expected = 'crime'
        result = d.decrypt(self.example3)
        self.assertEqual(result, expected)

    def test_case4(self):
        expected = 'encyclopedia'
        result = d.decrypt(self.example4)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()