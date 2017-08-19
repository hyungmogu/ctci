import unittest
import delete_middle_node as l

class TestInsertMethodInLinkedList(unittest.TestCase):

	def test_add_node_when_head_is_empty(self):
		ll = l.LinkedList()
		e1 = l.Node(4)
		ll.insert(e1)

		self.assertEqual(ll.head.value, 4)
		self.assertEqual(ll.head.next, None)

	def test_when_data_type_of_arg_is_incorrect(self):

		ll = l.LinkedList()
		with self.assertRaises(TypeError):
			ll.insert(4)

	def test_when_adding_node_to_non_empty_head(self):
		e1 = l.Node(4)
		e2 = l.Node(2)
		e3 = l.Node(3)
		ll = l.LinkedList(e1) 
		ll.insert(e2)
		ll.insert(e3)

		self.assertEqual(ll.head.next.value, 2)
		self.assertEqual(ll.head.next.next.value, 3)
		self.assertEqual(ll.head.next.next.next, None)

class TestDisplayMethod(unittest.TestCase):

	def test_when_head_is_empty(self):

		ll = l.LinkedList()

		self.assertEqual(ll.display(), "")


	def test_when_ll_is_not_empty(self):

		e1 = l.Node(1)
		e2 = l.Node(2)
		e3 = l.Node(3)

		ll = l.LinkedList(e1)
		ll.insert(e2)
		ll.insert(e3)

		self.assertEqual(ll.display(), "1 2 3")

class TestDeleteMiddleNodeMethod(unittest.TestCase):

	def test_when_the_middle_node_is_not_the_right_type(self):
		e1 = l.Node(2)
		e2 = l.Node(3)
		e3 = l.Node(4)

		ll = l.LinkedList(e1)
		ll.insert(e2)
		ll.insert(e3)

		with self.assertRaises(TypeError):
			ll.delete_middle_node(2)

		with self.assertRaises(TypeError):
			ll.delete_middle_node(None)

	def test_when_the_middle_node_is_last_node(self):

		e1 = l.Node(1)
		e2 = l.Node(2)
		e3 = l.Node(3)

		ll = l.LinkedList(e1)
		ll.insert(e2)
		ll.insert(e3)

		with self.assertRaises(ValueError):
			ll.delete_middle_node(e3)

	def test_when_there_are_more_than_one_node(self):

		e1 = l.Node(1)
		e2 = l.Node(2)
		e3 = l.Node(3)
		e4 = l.Node(4)
		e5 = l.Node(5)

		ll = l.LinkedList(e1)
		ll.insert(e2)
		ll.insert(e3)
		ll.insert(e4)
		ll.insert(e5)

		ll.delete_middle_node(e3)

		self.assertEqual(ll.display(), "1 2 4 5")


if __name__ == "__main__":
	unittest.main()