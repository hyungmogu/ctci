import unittest
import deletion_distance as d

class TestDeletionDistance(unittest.TestCase):
    def test_case_1(self):
        expected =  0
        result = d.deletion_distance("","")
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected =  3
        result = d.deletion_distance("","hit")
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected =  4
        result = d.deletion_distance("neat","")
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = 3
        result = d.deletion_distance("heat","hit")
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected = 2
        result = d.deletion_distance("hot","not")
        self.assertEqual(expected, result)

    def test_case_6(self):
        expected =  9
        result = d.deletion_distance("some","thing")
        self.assertEqual(expected, result)

    def test_case_7(self):
        expected = 1
        result = d.deletion_distance("abc","adbc")
        self.assertEqual(expected, result)

    def test_case_8(self):
        expected = 0
        result = d.deletion_distance("awesome","awesome")
        self.assertEqual(expected, result)

    def test_case_9(self):
        expected = 2
        result = d.deletion_distance("ab","ba")
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main()