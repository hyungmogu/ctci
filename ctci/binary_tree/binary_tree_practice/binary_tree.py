class Node(object):
	def __init__(self, value):
		self.value = value
		self.lchild = None
		self.rchild = None


class BinaryTree(object):

	def __init__(self, root=None):
		self.root = root

	def search(self, value):
		return self.post_order_search(self.root,value)

	def post_order_search(self, node, value):
		current = node

		if current == None:
			return False

		if current.value != value:
			return self.post_order_search(current.lchild, value) or self.post_order_search(current.rchild, value)
		else:
			return True


