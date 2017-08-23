import unittest
import sum_list as s

class TestInsertMethod(unittest.TestCase):

	def test_when_the_data_type_of_arg_is_incorrect(self):
		ll = s.LinkedList()

		with self.assertRaises(TypeError):
			ll.insert(1)

	def test_when_ll_is_empty(self):
		e1 = s.Node(1)
		ll = s.LinkedList()
		ll.insert(e1)

		self.assertEqual(ll.head.value, 1)

	def test_when_ll_is_not_empty(self):

		e1 = s.Node(1)
		e2 = s.Node(2)
		e3 = s.Node(3)

		ll = s.LinkedList(e1)
		ll.insert(e2)
		ll.insert(e3)

		self.assertEqual(ll.head.value, 1)
		self.assertEqual(ll.head.next.value, 2)
		self.assertEqual(ll.head.next.next.value, 3)


class TestDisplayMethod(unittest.TestCase):

	def test_when_head_is_empty(self):
		ll = s.LinkedList()
		self.assertEqual(ll.display(), "")

	def test_when_linked_list_is_not_empty(self):
		e1 = s.Node(1)
		e2 = s.Node(2)
		e3 = s.Node(3)

		ll = s.LinkedList(e1)
		ll.insert(e2)
		ll.insert(e3)

		self.assertEqual(ll.display(), "1 2 3")


class TestSumList(unittest.TestCase):

	def test_when_one_or_more_args_have_incorrect_data_type(self):
		n1d1 = s.Node(1)
		n1 = s.LinkedList(n1d1)

		with self.assertRaises(TypeError):
			s.sum_list(n1,1)


	def test_when_both_lists_have_the_same_digits(self):

		n1d1 = s.Node(9)
		n1d2 = s.Node(2)
		n1d3 = s.Node(3)

		n2d1 = s.Node(2)
		n2d2 = s.Node(3)
		n2d3 = s.Node(4)

		n1 = s.LinkedList(n1d1)
		n1.insert(n1d2)
		n1.insert(n1d3)

		n2 = s.LinkedList(n2d1)
		n2.insert(n2d2)
		n2.insert(n2d3)

		output = s.sum_list(n1,n2)

		self.assertEqual(output.display(), "1 6 7")


if __name__ == "__main__":
	unittest.main()