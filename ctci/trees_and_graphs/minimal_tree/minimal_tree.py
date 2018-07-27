import math


class Node:
	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None


class BinarySearchTree:
	def __init__(self):
		self.root = None

	# def in_order_traversal(self):

	# def get_height(self):

	@staticmethod
	def create_bst(start, end, array):

		output = None
		leftChild = None
		rightChild = None

		# check if edge cases are of concern
		if len(array) == 0:
			return output

		if len(array) == 1:
			output = Node(array[0]) 
			return output

		# see if it meets the base condition (for recursion)
		if start == end:
			output = Node(array[start]) 
			return output	

		# get the middle of the array
		middle_idx = int(math.floor((((start * 1.0) - end)/2)))

		middle_node = Node(array[middle_idx])


		# get the left chind and the right child of the array

		if (middle_idx - 1 >= start):
			leftChild = BinarySearchTree.create_bst(start, middle_idx - 1, array)

		if (middle_idx + 1 <= end):
			rightChild = BinarySearchTree.create_bst(middle_idx + 1, end, array)


		middle_node.leftChild = leftChild
		middle_node.rightChild = rightChild

		output = middle_node

		return output


