import unittest
import stack_in_linked_list as s

class TestStackInLinkedListPushMethod(unittest.TestCase):

	def test_when_root_node_is_null(self):

		e1 = s.Node(1)
		stack_in_ll = s.StackInLinkedList()
		stack_in_ll.push(e1)

		self.assertEqual(stack_in_ll.peek(), 1)
		self.assertEqual(stack_in_ll.root.next, None)


	def test_when_root_node_is_not_null(self):

		e1 = s.Node(1)
		e2 = s.Node(2)
		e3 = s.Node(3)

		stack_in_ll = s.StackInLinkedList(e1)

		self.assertEqual(stack_in_ll.peek(), 1)

		stack_in_ll.push(e2)

		self.assertEqual(stack_in_ll.peek(), 2)

		stack_in_ll.push(e3)

		self.assertEqual(stack_in_ll.peek(), 3)


class TestStackInLinkedListPopMethod(unittest.TestCase):

	def test_when_root_node_is_null(self):

		stack_in_ll = s.StackInLinkedList()

		with self.assertRaises(UnboundLocalError):
			stack_in_ll.pop()

	def test_when_root_node_is_not_null(self):

		e1 = s.Node(1)
		e2 = s.Node(2)
		e3 = s.Node(3)

		stack_in_ll = s.StackInLinkedList(e1)
		stack_in_ll.push(e2)
		stack_in_ll.push(e3)

		self.assertEqual(stack_in_ll.pop(), 3)
		self.assertEqual(stack_in_ll.pop(), 2)
		self.assertEqual(stack_in_ll.pop(), 1)


if __name__ == "__main__":
	unittest.main()