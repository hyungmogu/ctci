import unittest
from circular_list import LinkedList, Node

class TestCircularList(unittest.TestCase):
	def setUp(self):

		h = Node(1)
		e1 = Node("a")
		e2 = Node("b")
		e3 = Node("c")
		e4 = Node("d")

		self.ll = LinkedList(h)

		self.ll.add(e1)
		self.ll.add(e2)
		self.ll.add(e3)
		self.ll.add(e4)
		self.ll.add(e2)


	def test_circular_list(self):

		node = self.ll.find_circular_node()
		self.assertEqual(node.value, "b")


if __name__ == '__main__':
	unittest.main()