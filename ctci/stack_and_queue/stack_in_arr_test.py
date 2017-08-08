import unittest
import stack_in_arr as s

class TestStackInArrInit(unittest.TestCase):

	def test_init_when_size_is_greater_than_zero(self):

		stack_in_arr = s.StackInArray(5)

		self.assertEqual(len(stack_in_arr.arr), 5)
		self.assertEqual(stack_in_arr.top, -1)
		self.assertEqual(stack_in_arr.size, 5)


class TestStackInArrPushMethod(unittest.TestCase):

	def test_case_when_full(self):

		stack_in_arr = s.StackInArray(5)
		stack_in_arr.push(5)
		stack_in_arr.push(4)
		stack_in_arr.push(3)
		stack_in_arr.push(2)
		stack_in_arr.push(1)

		with self.assertRaises(IndexError):
			stack_in_arr.push(0) 

	def test_case_when_not_full_single(self):

		stack_in_arr = s.StackInArray(10)
		stack_in_arr.push(10)

		self.assertEqual(stack_in_arr.arr[0], 10)

	def test_case_when_not_full_multiple(self):

		stack_in_arr = s.StackInArray(10)
		stack_in_arr.push(10)
		stack_in_arr.push(5)

		self.assertEqual(stack_in_arr.arr[0], 10)
		self.assertEqual(stack_in_arr.arr[1], 5)


class TestStackInArrPopMethod(unittest.TestCase):

	def test_case_when_empty(self):

		stack_in_arr = s.StackInArray(5)

		with self.assertRaises(LookupError):
			stack_in_arr.pop()

	def test_case_when_not_empty(self):

		stack_in_arr = s.StackInArray(5)
		stack_in_arr.push(5)
		stack_in_arr.push(4)
		stack_in_arr.push(3)
		stack_in_arr.push(2)

		self.assertEqual(stack_in_arr.pop(), 2)

if __name__ == "__main__":
	unittest.main()