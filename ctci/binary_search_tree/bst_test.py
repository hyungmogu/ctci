import unittest
import bst as b

# class TestBSTSearchMethod(unittest.TestCase):

# 	def test_when_root_is_empty(self):
# 		bst = b.BinarySearchTree()

# 		self.assertEqual(bst.search(2), False)

# 	def test_when_there_is_only_root_in_the_tree(self):
# 		e1 = b.Node(3)
# 		bst = b.BinarySearchTree(e1)

# 		self.assertEqual(bst.search(3), True)
# 		self.assertEqual(bst.search(4), False)

# 	def test_when_there_is_more_than_one_root_in_the_tree(self):

# 		e1 = b.Node(20)

# 		bst = b.BinarySearchTree(e1)

# 		bst.insert(15)
# 		bst.insert(24)
# 		bst.insert(10)
# 		bst.insert(16)
# 		bst.insert(5)

# 		self.assertEqual(bst.search(3), False)
# 		self.assertEqual(bst.search(5), True)


class TestInsertMethod(unittest.TestCase):

	def test_when_root_node_is_empty(self):
		bst = b.BinarySearchTree()
		bst.insert(1)

		self.assertEqual(bst.root.value, 1)

	def test_when_node_with_same_value_exists(self):
		e1 = b.Node(3)

		bst = b.BinarySearchTree(e1)

		bst.insert(3)

		self.assertEqual(bst.root.value, 3)
		self.assertEqual(bst.root.lchild, None)
		self.assertEqual(bst.root.rchild, None)


	def test_when_node_with_same_value_does_not_exist(self):
		e1 = b.Node(20)
		bst = b.BinarySearchTree(e1)

		bst.insert(30)
		bst.insert(40)
		bst.insert(25)
		bst.insert(31)
		bst.insert(38)
		bst.insert(43)

		self.assertEqual(bst.root.lchild, None)
		self.assertEqual(bst.root.rchild.value, 30)
		self.assertEqual(bst.root.rchild.lchild.value, 25)
		self.assertEqual(bst.root.rchild.rchild.value, 40)
		self.assertEqual(bst.root.rchild.rchild.lchild.value, 31)
		self.assertEqual(bst.root.rchild.rchild.lchild.rchild.value, 38)

# class TestDisplayMethod(unittest.TestCase):

# 	def test_when_root_node_is_null(self):
# 		bst = b.BinarySearchTree()

# 		self.assertEqual(bst.display(), "")

# 	def test_when_there_is_one_node(self):
# 		e1 = b.Node(1)
# 		bst = b.BinarySearchTree(e1)

# 		self.assertEqual(bst.display(), "1")

# 	def test_when_there_is_more_than_one_node(self):

# 		e1 = b.Node(25)
# 		bst = b.BinarySearchTree(e1)
# 		bst.insert(16)
# 		bst.insert(30)
# 		bst.insert(12)
# 		bst.insert(20)
# 		bst.insert(23)
# 		bst.insert(38)

# 		self.assertEqual(bst.display(), "25 16 12 20 30 23 28")

if __name__ == "__main__":
	unittest.main()