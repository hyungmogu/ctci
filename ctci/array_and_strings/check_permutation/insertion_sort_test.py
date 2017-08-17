import insertion_sort as i
import unittest

class TestInsertionSort(unittest.TestCase):

	def test_when_arguement_has_wrong_type(self):
		with self.assertRaises(TypeError):
			i.insertion_sort(1,0)

		with self.assertRaises(TypeError):
			i.insertion_sort("Hello world", "hi")

		with self.assertRaises(TypeError):
			i.insertion_sort([5,4,3,2,1], "hi")

	def test_when_array_has_no_element(self):
		arr = []
		with self.assertRaises(LookupError):
			i.insertion_sort(arr,0)

	def test_when_array_has_one_element(self):
		arr = [1]
		self.assertEqual(i.insertion_sort(arr,1), [1])

	def test_when_array_has_more_than_one_element(self):
		arr = [5,4,3,2,1]
		self.assertEqual(i.insertion_sort(arr,5), [1,2,3,4,5])

if __name__ == "__main__":
	unittest.main()