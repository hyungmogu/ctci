class Node(object):
	def __init__(self, value = None):
		self.value = value
		self.next = None

class StackInLinkedList(object):
	def __init__(self, node = None):
		self.root = node

	def push(self, node):

		if self.root == None:
			self.root = node
			return

		temp = node
		temp.next= self.root
		self.root = temp

	def pop(self):

		if self.root == None:
			raise UnboundLocalError("Operation stopped. Node is empty")

		temp = self.root
		self.root = temp.next
		temp.next = None

		return temp.value

	def peek(self):
		return self.root.value