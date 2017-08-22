import unittest
import urlify as u

class TestURLifyfunction(unittest.TestCase):

	def test_when_the_data_type_of_one_more_arg_is_incorrect(self):
		
		with self.assertRaises(TypeError):
			u.urlify(1,2)

		with self.assertRaises(TypeError):
			u.urlify("hello world","hi")

	def test_when_true_length_of_char_is_gt_than_num_of_char(self):

		with self.assertRaises(ValueError):
			u.urlify(" ", 5)

	def test_when_the_input_string_is_empty(self):

		with self.assertRaises(ValueError):
			u.urlify("",0)

		with self.assertRaises(ValueError):
			u.urlify(" ", 0)


	def test_when_all_args_are_correct(self):

		self.assertEqual(u.urlify("hello world", 11), "hello%20world")
		self.assertEqual(u.urlify("hello world     ", 11), "hello%20world     ")

if __name__ == "__main__":
	unittest.main()