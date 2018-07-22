import unittest
import matrix_rotation as m

class TestMatrixRotation(unittest.TestCase):
	def setUp(self):
		self.matrix22 = [[1,2],[3,4]]
		self.matrix33 = [[1,2,3],[4,5,6],[7,8,9]]
		self.matrix44 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

	def test_get_depth(self):
		self.assertEqual(m.getDepth(self.matrix22), 1)
		self.assertEqual(m.getDepth(self.matrix33), 1)

	def test_rotate_right(self):
		m.rotateRight(self.matrix22, 0)
		self.assertEqual(self.matrix22, [[2,4],[3,4]])

	def test_rotate_bottom(self):
		m.rotateBottom(self.matrix22, 0)
		self.assertEqual(self.matrix22, [[1,4],[3,3]])

	def test_rotate_left(self):
		m.rotateLeft(self.matrix22, 0)
		self.assertEqual(self.matrix22, [[1,2],[1,3]])

	def test_rotate_top(self):
		temp = [1,2]
		m.rotateTop(self.matrix22, 0, temp)
		self.assertEqual(self.matrix22, [[2,2],[1,4]])

	def test_rotation_edge(self):
		self.assertEqual(m.rotateCCW([]),[]);
		self.assertEqual(m.rotateCCW([1]), [1]);

	def test_rotation_even(self):
		self.assertEqual(m.rotateCCW(self.matrix22), [[2,4],[1,3]])
		self.assertEqual(m.rotateCCW(self.matrix44), [[4,8,12,16],[3,7,11,15],[2,6,10,14],[1,5,9,13]])

	def test_rotation_odd(self):
		self.assertEqual(m.rotateCCW(self.matrix33), [[3,6,9],[2,5,8],[1,4,7]])

if __name__ == '__main__':
	unittest.main()