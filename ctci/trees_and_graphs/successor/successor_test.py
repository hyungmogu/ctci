import unittest
from successor import Node, BinarySearchTree

class TestSuccessor(unittest.TestCase):

	def setUp(self):
		self.head = Node(14)
		
		self.node1 = Node(13)
		self.node1.parent = self.head
		self.node2 = Node(17)
		self.node2.parent = self.head
		
		self.node3 = Node(10)
		self.node3.parent = self.node1
		self.node4 = Node(16)
		self.node4.parent = self.node2
		self.node5 = Node(19)
		self.node5.parent = self.node2

		self.node6 = Node(9)
		self.node6.parent = self.node3
		self.node7 = Node(12)
		self.node7.parent = self.node3
		self.node8 = Node(15)
		self.node8.parent = self.node4
		self.node9 = Node(18)
		self.node9.parent = self.node5
		self.node10 = Node(20)
		self.node10.parent = self.node5


		self.head.leftChild = self.node1
		self.head.rightChild = self.node2

		self.node1.leftChild = self.node3

		self.node2.leftChild = self.node4
		self.node2.rightChild = self.node9

		self.node3.leftChild = self.node6
		self.node3.rightChild = self.node7


		self.node4.leftChild = self.node8

		self.node5.leftChild = self.node9
		self.node5.rightChild = self.node10

		self.bst = BinarySearchTree(self.head)



	def test_successor(self):
		# setup
		expected1 = 14
		expected2 = 17
		expected3 = 18
		expected4 = 12
		expected5 = 17
		expected6 = 20
		expected7 = 13
		expected8 = None

		# exercise
		result1 = self.bst.successor(self.node1)
		result2 = self.bst.successor(self.head)
		result3 = self.bst.successor(self.node2)
		result4 = self.bst.successor(self.node3)
		result5 = self.bst.successor(self.node4)
		result6 = self.bst.successor(self.node5)
		result7 = self.bst.successor(self.node7)
		result8 = self.bst.successor(self.node10)

		# verify
		self.assertEqual(result1.data, expected1)
		self.assertEqual(result2.data, expected2)
		self.assertEqual(result3.data, expected3)
		self.assertEqual(result4.data, expected4)
		self.assertEqual(result5.data, expected5)
		self.assertEqual(result6.data, expected6)


if __name__ == '__main__':
	unittest.main()