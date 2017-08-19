import unittest
import palindrome_permutation as p

class TestPalindromePermutationFunction(unittest.TestCase):

	def test_when_the_type_of_arg_is_incorrect(self):

		with self.assertRaises(TypeError):
			p.palindrome_permutation(1)

	def test_when_string_is_empty(self):

		with self.assertRaises(ValueError):
			p.palindrome_permutation("    ")

	def test_when_string_is_not_palindrome(self):

		self.assertEqual(p.palindrome_permutation("aa bcaa"), False)

	def test_when_string_is_palindrome(self):

		self.assertEqual(p.palindrome_permutation("aa  bcb aa"), True)


if __name__ == "__main__":
	unittest.main()