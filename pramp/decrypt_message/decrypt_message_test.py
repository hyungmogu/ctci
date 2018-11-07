import decrypt_message as d
import unittest

class TestDecryptMessage(unittest.TestCase):
    def setUp(self):
        self.example1 = ''
        self.example2 = 'bvq'
        self.example3 = 'dnotq'

    def test_return_nothing_when_input_is_nothing(self):
        expected = ''
        result = d.decrypt(self.example1)
        self.assertEqual(result, expected)

    def test_return_abc_when_decrypting_bvq(self):
        expected = 'abc'
        result = d.decrypt(self.example2)
        self.assertEqual(result, expected)

    def test_return_crime_when_decrypting_dnotq(self):
        expected = 'crime'
        result = d.decrypt(self.example3)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()