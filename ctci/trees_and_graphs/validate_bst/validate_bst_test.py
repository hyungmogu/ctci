import unittest
from validate_bst import Node, BinarySearchTree


class TestValidate(unittest.TestCase):
	def setUp(self):
		self.head1 = Node(3)
		node1 = Node(2)
		node2 = Node(4)
		node3 = Node(1)
		node4 = Node(5)

		self.head1.leftChild = node1
		self.head1.rightChild = node2
		node1.leftChild = node3
		node2.rightChild = node4


	def test_validate(self):
		expected1 = True
		bst = BinarySearchTree(self.head1)

		result1 = bst.validate(self.head1)

		self.assertEqual(result1, expected1)


if __name__ == '__main__':
	unittest.main();