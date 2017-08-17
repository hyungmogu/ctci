import unittest

import check_permutation as c


class TestCheckPermutationMethod(unittest.TestCase):

	def test_when_args_not_correct_type(self):
		with self.assertRaises(TypeError):
			c.is_permutation(1,"h")

		with self.assertRaises(TypeError):
			c.is_permutation("h", 1)

		with self.assertRaises(TypeError):
			c.is_permutation([1,2,3],1)

	def test_when_either_of_args_is_empty(self):
		with self.assertRaises(ValueError):
			c.is_permutation("h", "         ")
		with self.assertRaises(ValueError):
			c.is_permutation("  ", "h")
		with self.assertRaises(ValueError):
			c.is_permutation(" ","    ")

	def test_when_both_args_are_not_empty(self):
		self.assertEqual(c.is_permutation("hello",'olleh'), True)
		self.assertEqual(c.is_permutation("alright","no"), False)

if __name__ == "__main__":
	unittest.main()