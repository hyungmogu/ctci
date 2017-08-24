import unittest
import merge_sort as m

class TestMergeTwoArraysFunction(unittest.TestCase):

	def test_when_one_or_more_args_have_wrong_type(self):

		with self.assertRaises(TypeError):
			m.merge_arrays("a",[1,2,3],1,3)

		with self.assertRaises(TypeError):
			m.merge_arrays([1,2,3],"a",3,1)

		with self.assertRaises(TypeError):
			m.merge_arrays([1,2,3],[4,5,6],"a",3)

		with self.assertRaises(TypeError):
			m.merge_arrays([1,2,3],[4,5,6],3,"b")

		with self.assertRaises(TypeError):
			m.merge_arrays("b",[4,5,6],"b",3)

	def test_when_either_arr1_or_arr2_is_emtpy(self):

		with self.assertRaises(ValueError):
			m.merge_arrays([],[1,2,3],0,3)

		with self.assertRaises(ValueError):
			m.merge_arrays([1,2,3],[],3,0)

		with self.assertRaises(ValueError):
			m.merge_arrays([],[],0,0)

	def test_when_both_arr1_and_arr2_are_non_empty(self):

		self.assertEqual(m.merge_arrays([1,2,3],[4,5,6],3,3),[1,2,3,4,5,6])
		self.assertEqual(m.merge_arrays([5,10,12,15],[6,12,12,14],4,4), [5,6,10,12,12,12,14,15])

if __name__ == "__main__":
	unittest.main()