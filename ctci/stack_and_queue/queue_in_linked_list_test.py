import unittest
import queue_in_linked_list as q 



class TestEnqueueMethod(unittest.TestCase):

	def test_when_front_and_back_are_null(self):

		e1 = q.Node(1)
		ll = q.QueueInLinkedList()

		ll.enqueue(e1)

		self.assertEqual(ll.head.value, 1)
		self.assertEqual(ll.back.value, 1)

	def test_when_front_and_back_are_not_null(self): 

		e1 = q.Node(1)
		e2 = q.Node(2)

		ll = q.QueueInLinkedList(e1)
		ll.enqueue(e2)

		self.assertEqual(ll.head.value, 1)
		self.assertEqual(ll.back.value, 2)


class TestDequeueMethod(unittest.TestCase):

	def test_when_front_and_back_are_null(self):
		ll = q.QueueInLinkedList()

		with self.assertRaises(LookupError):
			ll.dequeue()

	def test_when_ll_has_one_node(self):
		e1 = q.Node(1)
		ll = q.QueueInLinkedList(e1)

		self.assertEqual(ll.dequeue(), 1)
		self.assertEqual(ll.head, None)
		self.assertEqual(ll.back, None)

	def test_when_ll_has_more_than_one_node(self):

		e1 = q.Node(1)
		e2 = q.Node(2)
		e3 = q.Node(3)

		ll = q.QueueInLinkedList(e1)
		ll.enqueue(e2)
		ll.enqueue(e3)

		self.assertEqual(ll.dequeue(), 1)
		self.assertEqual(ll.dequeue(), 2)
		self.assertEqual(ll.back.value, 3)
		self.assertEqual(ll.head.value, 3)


if __name__ == "__main__":
	unittest.main()