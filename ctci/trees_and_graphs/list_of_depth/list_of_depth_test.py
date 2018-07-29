import unittest
from list_of_depth import Node, BreadthFirstSearch

class TestListOfDepth(unittest.TestCase):
	def test_list_of_depth_edge_cases(self):
		## it returns empty list if no head is given
		# setup
		head = None

		# exercise
		result = BreadthFirstSearch.list_of_depth(head)

		# verify
		self.assertEqual(result, [])


		## it returns list of 1 if only one node is given
		#setup
		head2 = Node(1)

		result2 = BreadthFirstSearch.list_of_depth(head2)

		self.assertEqual(result2[0].data, 1)
		self.assertEqual(result2[0].next, None)

	def test_list_of_depth_general_case(self):
		## it returns list of nodes with each representing the head at depth D		
		# Setup
		node1 = Node(1)
		node2 = Node(2)
		node3 = Node(3)
		node4 = Node(4)
		node5 = Node(5)

		node3.leftChild = node2
		node3.rightChild = node4
		node2.leftChild = node1
		node4.rightChild = node5

		head = node3

		# exercise
		result = BreadthFirstSearch.list_of_depth(head)

		# verify
		self.assertEqual(result[0].data, 3)
		self.assertEqual(result[0].next, None)

		self.assertEqual(result[1].data, 2)
		self.assertEqual(result[1].next.data, 4)
		self.assertEqual(result[1].next.next, None)

		self.assertEqual(result[2].data, 1)
		self.assertEqual(result[2].next.data, 5)
		self.assertEqual(result[2].next.next, None)










if __name__ == '__main__':
	unittest.main();