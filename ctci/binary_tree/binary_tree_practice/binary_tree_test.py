import unittest
import binary_tree as b


class TestSearch(unittest.TestCase):

	# def test_when_root_node_is_empty(self):
	# 	bt = b.BinaryTree()
	# 	self.assertEqual(bt.search(1), None)

	# def test_when_there_is_only_one_node(self):
	# 	root = b.Node(1)
	# 	bt = b.BinaryTree(root)
	# 	self.assertEqual(bt.search(2), None)
	# 	self.assertEqual(bt.search(1), True)

	def test_when_there_are_multiple_same_nodes_in_the_tree(self):
		root = b.Node(3)
		e1 = b.Node(3)
		e2 = b.Node(3)
		e3 = b.Node(4)
		e4 = b.Node(5)

		bt = b.BinaryTree(root)
		bt.root.lchild = e1
		bt.root.rchild = e2
		bt.root.lchild.lchild = e3
		bt.root.rchild.lchild = e4

		#self.assertEqual(bt.search(3), True)
		#self.assertEqual(bt.search(6), None)

	def test_when_there_are_none_of_the_same_nodes_in_the_tree(self):

		root = b.Node(6)
		e1 = b.Node(7)
		e2 = b.Node(8)
		e3 = b.Node(9)
		e4 = b.Node(10)

		bt = b.BinaryTree(root)
		bt.root.lchild = e1
		bt.root.rchild = e2
		bt.root.lchild.lchild = e3
		bt.root.rchild.lchild = e4

		#self.assertEqual(bt.search(6), True)
		self.assertEqual(bt.search(7), True)		
		#self.assertEqual(bt.search(11), None)


if __name__ == "__main__":
	unittest.main() 