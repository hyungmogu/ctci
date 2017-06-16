import unittest

import recursion as r

class TestFibonacci(unittest.TestCase):
	def test_when_n_is_zero(self):

		self.assertEqual(r.fibonacci(0), 0)

	def test_when_n_is_one(self):
		self.assertEqual(r.fibonacci(1), 1)

	def test_when_n_is_greater_than_one(self):
		self.assertEqual(r.fibonacci(5), 5)
		self.assertEqual(r.fibonacci(8), 21)
		self.assertEqual(r.fibonacci(12), 144)


if __name__ == '__main__':
	unittest.main()