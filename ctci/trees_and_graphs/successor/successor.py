class Node:
	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None
		self.parent = None


class BinarySearchTree:

	def __init__(self, node):
		self.head = node

	def successor(self, node):
		output = None

		if not node:
			return output

		if node.rightChild != None:
			output = node.rightChild
			return output

		if node.parent != None:
			if node.parent.data == node.data:
				output = node.parent if node == node.parent.leftChild else None

			if node.parent.data > node.data:
				output = node.parent

			return output

		
		if node.parent.parent != None:
			if node.parent.parent.data == node.data:
				output = node.parent if (node == node.parent.rightChild) and (node.parent == node.parent.parent.leftChild) else None

			if node.parent.parent.data > node.data:
				output = node.parent.parent

			return output


		return output


