class Node(object):
	def __init__(self, value):
		self.value = value
		self.lchild = None
		self.rchild = None


class BinarySearchTree(object):
	def __init__(self, root=None):
		self.root = root

	def display(self):

		current = self.root

		if current == None:
			return 


	def search(self, value):
		current = self.root

		if current == None:
			return False

		# current is null
		while current != None:

			if current.value == value:
				return True

			elif current.value < value:
				current = current.rchild

			else:
				current = current.lchild

		return False

	def insert(self, value):
		# insert operation has to be done recursively
		
		current = self.root

		if current == None:
			self.root = Node(value)
			return

		while current != None:
			if value > current.value:
				if current.rchild == None:
					current.rchild = Node(value)
					break
				else:
					current = current.rchild

			elif value < current.value:
				if current.lchild == None:
					current.lchild = Node(value)
					break
				else:
					current = current.lchild

			else:
				break

	def display(self):
		current = self.root

		if current == None:
			return ""

		if current.lchild == None and current.rchild == None:
			return "{0}".format(current.value)

		else:
			output = ""
			return self.dfs_search(current, output)


	def dfs_search(self, node, output):

		if node == None:
			return

		output = output + str(node.value) + " "

		self.dfs_search(node.lchild, output)
		self.dfs_search(node.rchild, output)

		return output.rstrip()
