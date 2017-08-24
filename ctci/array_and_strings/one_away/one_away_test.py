import unittest
import one_away as o

class TestOneAwayMethod(unittest.TestCase):

	def test_when_one_or_more_args_is_incorrect(self):

		with self.assertRaises(TypeError):
			o.one_away(1,"hello")

		with self.assertRaises(TypeError):
			o.one_away(None, 1)

	def test_when_one_or_more_args_is_empty(self):

		with self.assertRaises(ValueError):
			o.one_away("","hello")

		with self.assertRaises(ValueError):
			o.one_away("", "   ")		

	def test_when_both_args_are_non_empty(self):

		self.assertEqual(o.one_away("pale","bale"), True)
		self.assertEqual(o.one_away("bake","bae"), True)
		self.assertEqual(o.one_away("pale","bake"), False)

if __name__ == "__main__":
	unittest.main()