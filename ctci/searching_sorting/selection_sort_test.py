import unittest
import selection_sort as s

class TestSelectionSort(unittest.TestCase):

	def test_when_arr_is_not_correct_type(self):

		with self.assertRaises(TypeError):
			s.selection_sort("hello",2)

		with self.assertRaises(TypeError):
			s.selection_sort([1,2,3], "hi")

		with self.assertRaises(TypeError):
			s.selection_sort("hello", "hi")


	def test_when_array_is_empty(self):

		with self.assertRaises(ValueError):
			s.selection_sort([], 2)

	def test_when_array_has_one_element(self):

		self.assertEqual(s.selection_sort([1],1),[1])

	def test_when_array_has_more_than_one_element(self):

		self.assertEqual(s.selection_sort([5,4,3,2,1],5), [1,2,3,4,5]) 


if __name__ == "__main__":
	unittest.main()