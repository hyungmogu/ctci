import sys

class Node:
	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None


class BinarySearchTree:
	def __init__(self, node):
		self.head = node
		self._prev_data = -sys.maxint - 1 #value for minint

	def validate(self, head):
		output = True
		current = head

		if (current != None):
			self.validate(current.leftChild)
			if (not self.is_bst(current)):
				output = False
				return output
			else:
				self._prev_data = ord(current.data) if (type(current.data).__name__ is 'string') else current.data
			self.validate(current.rightChild)


		return output


	def is_bst(self, node):
		data = node.data
	
		if (type(data).__name__ is 'string'):
			data = ord(node.data)
		

		return False if (data < self._prev_data) else True