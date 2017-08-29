import unittest
import partition as p

class TestLinkedListInsertMethod(unittest.TestCase):

	def test_when_arg_is_not_the_right_type(self):
		ll = p.LinkedList()

		with self.assertRaises(TypeError):
			ll.insert("hello world")

	def test_when_linked_list_is_empty(self):
		e1 = p.Node(1)
		ll = p.LinkedList()

		ll.insert(e1)

		self.assertEqual(ll.head.value, 1)
		self.assertEqual(ll.end.value, 1)


	def test_when_linked_list_is_not_empty(self):
		e1 = p.Node(1)
		e2 = p.Node(2)
		e3 = p.Node(3)
		ll = p.LinkedList(e1)

		self.assertEqual(ll.head.value, 1)
		self.assertEqual(ll.end.value, 1)

		ll.insert(e2)

		self.assertEqual(ll.head.next.value, 2)
		self.assertEqual(ll.end.value, 2)

		ll.insert(e3)

		self.assertEqual(ll.head.next.next.value, 3)
		self.assertEqual(ll.end.value, 3)


class TestPartitionMethod(unittest.TestCase):

	def test_when_the_arguement_is_not_the_right_type(self):

		# Note. this also considers the case when the linked list is empty.

		e1 = p.Node(1)
		e2 = p.Node(2)

		e1.next = e2

		with self.assertRaises(TypeError):
			p.partition(e1, "Hello world")

		with self.assertRaises(TypeError):
			p.partition(None, 1)


	def test_when_linked_list_has_one_node(self):

		e1 = p.Node(1)
		ll = p.LinkedList(e1)
		partitioned_ll = p.partition(ll.head, 1)
		partitioned_ll2 = p.partition(ll.head, 10)

		self.assertEqual(partitioned_ll.value, 1)
		self.assertEqual(partitioned_ll.next, None)
		self.assertEqual(partitioned_ll2.value, 1)
		self.assertEqual(partitioned_ll2.next, None)


	def test_when_partition_has_elements_smaller_equal_and_greater_than_x(self):

		# case 1
		elements_to_insert = [3,5,8,5,10,2]
		ll = p.LinkedList()

		for i in elements_to_insert:
			e = p.Node(i)
			ll.insert(e)

		partitioned_ll = p.partition(ll.head, 5)
		correct_answer = [3,2,5,5,8,10]
		i = 0

		current = partitioned_ll
		while current != None:
			self.assertEqual(current.value, correct_answer[i])
			current = current.next
			i += 1

	def test_when_partition_has_no_elements_smaller_than_x(self):

		elements_to_insert = [3,5,8,5,10,2]
		ll = p.LinkedList()

		for i in elements_to_insert:
			e = p.Node(i)
			ll.insert(e)

		partitioned_ll = p.partition(ll.head, 2)
		correct_answer = [2,3,5,8,5,10]
		i = 0

		current = partitioned_ll
		while current != None:
			self.assertEqual(current.value, correct_answer[i])
			current = current.next
			i += 1

		
	def test_when_partition_has_no_elements_equal_to_x(self):

		elements_to_insert = [3,5,8,5,10,2]
		ll = p.LinkedList()

		for i in elements_to_insert:
			e = p.Node(i)
			ll.insert(e)


		partitioned_ll = p.partition(ll.head, 6)
		correct_answer = [3,5,5,2,8,10]
		i = 0

		current = partitioned_ll
		while current != None:
			self.assertEqual(current.value, correct_answer[i])
			current = current.next
			i += 1

	def test_when_partition_has_no_elements_greater_than_x(self):

		elements_to_insert = [3,5,8,5,10,2]
		ll = p.LinkedList()

		for i in elements_to_insert:
			e = p.Node(i)
			ll.insert(e)


		partitioned_ll = p.partition(ll.head, 10)
		correct_answer = [3,5,8,5,2,10]
		i = 0

		current = partitioned_ll
		while current != None:
			self.assertEqual(current.value, correct_answer[i])
			current = current.next
			i += 1


	def test_when_partition_has_no_elements_smaller_than_x_and_equal_to_x(self):

		elements_to_insert = [3,5,8,5,10,2]
		ll = p.LinkedList()

		for i in elements_to_insert:
			e = p.Node(i)
			ll.insert(e)


		partitioned_ll = p.partition(ll.head, 1)
		correct_answer = [3,5,8,5,10,2]
		i = 0

		current = partitioned_ll
		while current != None:
			self.assertEqual(current.value, correct_answer[i])
			current = current.next
			i += 1

	def test_when_partition_has_no_elements_equal_to_x_and_greater_than_x(self):

		elements_to_insert = [3,5,8,5,10,2]
		ll = p.LinkedList()

		for i in elements_to_insert:
			e = p.Node(i)
			ll.insert(e)


		partitioned_ll = p.partition(ll.head, 12)
		correct_answer = [3,5,8,5,10,2]
		i = 0

		current = partitioned_ll
		while current != None:
			self.assertEqual(current.value, correct_answer[i])
			current = current.next
			i += 1

	def test_when_partition_has_no_elements_smaller_than_x_and_greater_than_x(self):

		elements_to_insert = [5,5]
		ll = p.LinkedList()

		for i in elements_to_insert:
			e = p.Node(i)
			ll.insert(e)


		partitioned_ll = p.partition(ll.head, 5)
		correct_answer = [5,5]
		i = 0

		current = partitioned_ll
		while current != None:
			self.assertEqual(current.value, correct_answer[i])
			current = current.next
			i += 1

	def test_when_there_are_only_two_nodes_in_ll(self):

		elements_to_insert = [1,2]
		ll = p.LinkedList()

		for i in elements_to_insert:
			e = p.Node(i)
			ll.insert(e)


		partitioned_ll = p.partition(ll.head, 2)
		correct_answer = [1,2]
		i = 0

		current = partitioned_ll
		while current != None:
			self.assertEqual(current.value, correct_answer[i])
			current = current.next
			i += 1


if __name__ == "__main__":
	unittest.main()