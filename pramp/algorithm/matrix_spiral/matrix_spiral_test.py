import unittest
import matrix_spiral_review as s

class TestSpiralCopy(unittest.TestCase):
    def setUp(self):
        self.example1 = [[1]]
        self.example2 = [[1,2],[4,3]]
        self.example3 = [[1,2,3], [8,9,4], [7,6,5]]
        self.example4 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]

    def test_case_1(self):
        expected = [1]
        result = s.spiral_copy(self.example1)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected = [1,2,3,4]
        result = s.spiral_copy(self.example2)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = [1,2,3,4,5,6,7,8,9]
        result = s.spiral_copy(self.example3)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = [1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12]
        result = s.spiral_copy(self.example4)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()