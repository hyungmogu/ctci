class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None


class QueueInLinkedList(object):
	def __init__(self, node=None):
		self.head = node
		self.back = node

	def peek(self):
		return self.head.value

	def enqueue(self, node):

		if self.head is None and self.back is None:
			self.head = node
			self.back = node
			return

		self.back.next = node
		self.back = node


	def dequeue(self):

		if self.isEmpty():
			raise LookupError("Operation stopped. There are no nodes in the linked list")

		if self.head == self.back:
			temp = self.head
			self.head = None
			self.back = None
			return temp.value

		temp = self.head
		self.head = temp.next
		temp.next = None
		return temp.value 


	def isEmpty(self):

		if self.head is None and self.back is None:
			return True
		else:
			return False


