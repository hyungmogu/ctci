class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList(object):
	def __init__(self, node = None):
		self.head = node

	def insert(self, node):

		if not isinstance(node, Node):
			raise TypeError("The arguement mustbe an instance of an object named node.")

		if self.head == None:
			self.head = node
			return

		current_node = self.head

		while current_node.next != None:
			current_node = current_node.next

		current_node.next = node

	def delete_middle_node(self, middle_node):

		if not isinstance(middle_node, Node):
			raise TypeError("The arguemenet must be an instance of an object named node.")

		if middle_node.next == None:
			raise ValueError("The node cannot be the last node in the linked list")

		current_node = middle_node

		while current_node.next.next != None:
			current_node.value = current_node.next.value
			current_node = current_node.next

		current_node.value = current_node.next.value
		current_node.next = None


	def display(self):

		values = ""

		current = self.head

		if current == None:
			return ""

		while current != None:
			values = values + str(current.value) + " " 
			current = current.next

		return values.rstrip()