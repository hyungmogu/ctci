import types as t

class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList(object):
	def __init__(self, head = None):
		# self.end = head because __init__ method is designed with consideration to take single node

		self.head = head
		self.end = head

	def insert(self, node):

		if not isinstance(node, Node):
			raise TypeError("Operation stopped. The arguement must be an instance of Node object.")

		if self.head == None:
			self.head = node
			self.end = node
			return

		self.end.next = node
		self.end = node



def partition(head, partition_value):

	if not isinstance(head, Node) or type(partition_value) != t.IntType:
		raise TypeError("Operation stopped. The arguement must be an instance of Node object.")

	if head.next == None:
		return head

	# separating each elements in linked list (divide)
	x = partition_value
	smaller_than_x = LinkedList()
	equal_to_x = LinkedList()
	greater_than_x = LinkedList()

	current = head

	while current != None:
		e = Node(current.value)

		if current.value < x:
			smaller_than_x.insert(e)
		elif current.value == x:
			equal_to_x.insert(e)
		else:
			greater_than_x.insert(e)

		current = current.next

	# combining components together (conquer)
	if smaller_than_x.head == None and greater_than_x.head == None:
		return equal_to_x.head
	
	elif equal_to_x.head == None and greater_than_x.head == None:
		return smaller_than_x.head

	elif smaller_than_x.head == None and equal_to_x.head == None:
		return greater_than_x.head

	elif greater_than_x.head == None:
		smaller_than_x.end.next = equal_to_x.head
		return smaller_than_x.head

	elif equal_to_x.head == None:
		smaller_than_x.end.next = greater_than_x.head
		return smaller_than_x.head

	elif smaller_than_x.head == None:
		equal_to_x.end.next = greater_than_x.head

	else:
		# this case is when all of the above are present
		smaller_than_x.end.next = equal_to_x.head
		smaller_than_x.end = equal_to_x.end
		smaller_than_x.end.next = greater_than_x.head

		return smaller_than_x.head







