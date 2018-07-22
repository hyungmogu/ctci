import unittest
import zero_matrix as z

class TestZeroMatrix(unittest.TestCase):
    # Extreme Edge cases
    # def test_inputs(self):

    #     with self.assertRaises(TypeError):
    #         z.setZeros(3,(1,2))
    #         z.setZeros("a",(1,2))
    #         z.setZeros([1,2,3],"a")

    # def test_emptyArray(self):

    #     with self.assertRaises(ValueError):
    #         z.setZeros([],(1,2))
    #         z.setZeros([[]],(1,2))

    def test_checkType(self):
        self.assertEqual(z.getType([1,2,3]), "1dimHoriz")
        self.assertEqual(z.getType([[1],[2],[3]]), "1dimVertical")
        self.assertEqual(z.getType([[1,2,3],[4,5,6],[7,8,9]]), "multi")


    def test_setZero(self):
        self.assertEqual(z.setZeros([1,2,3], (0,1)), [0,0,0])
        self.assertEqual(z.setZeros([[1],[2],[3]], (1,0)), [[0],[0],[0]])
        self.assertEqual(z.setZeros([[1,2,3],[4,5,6],[7,8,9]],(0,1)), [[0,0,0],[4,0,6],[7,0,9]])

if __name__ == "__main__":
	unittest.main()
