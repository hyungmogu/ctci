class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None
		self.min = None



class Stack(object):
	def __init__(self, head = None):
		self.head = head

	def push(self, node):

		# When arg doesn't have the right data type
		if not isinstance(node,Node):
			raise TypeError("Operation stopped. The argument must be an instance of Node object.")


		# When all data type of this method is correct

		# When head of linked list is empty
		if self.head == None:
			node.min = node.value
			self.head = node
			return

		# When head of linked list is not empty
		if node.value < self.head.min:
			node.min = node.value
		else:
			node.min = self.head.min

		node.next = self.head
		self.head = node


	# def pop(self):
