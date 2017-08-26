import unittest
import stack_min as s

class TestStackPushMethod(unittest.TestCase):

	def test_when_data_type_of_arg_is_incorrect(self):

		stack = s.Stack()

		with self.assertRaises(TypeError):
			stack.push(" ")


	def test_when_linked_list_is_empty(self):

		stack = s.Stack()
		e1 = s.Node(1)
		stack.push(e1)

		self.assertEqual(stack.head.value, 1)
		self.assertEqual(stack.head.min, 1)


	def test_when_linked_list_is_not_empty(self):

		stack = s.Stack()
		e1 = s.Node(3)
		e2 = s.Node(2)
		e3 = s.Node(4)
		e4 = s.Node(1)


		stack.push(e1)

		self.assertEqual(stack.head.value, 3)
		self.assertEqual(stack.head.min, 3)

		stack.push(e2)
		
		self.assertEqual(stack.head.value, 2)
		self.assertEqual(stack.head.min, 2)


		stack.push(e3)

		self.assertEqual(stack.head.value, 4)
		self.assertEqual(stack.head.min, 2)

		stack.push(e4)

		self.assertEqual(stack.head.value, 1)
		self.assertEqual(stack.head.min, 1)




# class TestStackPopMethod(unittest.TestCase):

# 	def test_when



# class TestStackMinMethod(unittest.TestCase):

# 	def test_


if __name__ == "__main__":
	unittest.main()