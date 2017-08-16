import unittest
import is_unique as q1

class TestIsUniqueMethod(unittest.TestCase):

	def test_when_string_is_empty(self): 

		with self.assertRaises(ValueError):
			q1.is_unique("")

		with self.assertRaises(ValueError):
			q1.is_unique("          ")


	def test_when_string_is_not_the_right_type(self):

		with self.assertRaises(TypeError):
			q1.is_unique(None)

		with self.assertRaises(TypeError):
			q1.is_unique(1)

	def test_when_string_is_right_and_not_empty(self):

		self.assertEqual(q1.is_unique("hi"), True)
		self.assertEqual(q1.is_unique("hello world"), False)


if __name__ == "__main__":
	unittest.main()