class Element(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def append(self, new_element):
		current = self.head
		if self.head:
			while current.next:
				current = current.next
			current.next = new_element
		else:
			self.head = new_element

	def get_node(self, position):
		current = self.head
		i = 0
		if self.head == None:
			print("Head is empty.")
			return None

		if self.head.next == None:
			print("There is only one node")
			return self.head

		while current:
			if i == position:
				return current

			current = current.next
			i += 1

		print("The value of position is greater than n")
		return None

	def insert(self, new_element, position):
		current_element = self.head

		i = 1
		while i < (position - 1):
			current_element = current_element.next
			i += 1

		new_element.next = current_element.next
		current_element.next = new_element

	def get_size(self):
		n = 0

		current = self.head

		if self.head == None:
			return 0

		while current:
			n += 1
			current = current.next

		return n

	def is_palindrome(self):
		i = 0
		n = 0
		current = self.head

		if self.head == None:
			return False

		if self.head.next == None:
			print("Palindrome has only one element")
			return True

		n = self.get_size();

		while i < (n-(i+1)):
			opposing_node = self.get_node(n-(i+1))

			if opposing_node.value != current.value:
				print("The list is not palindrome")
				return False

			current = current.next
			i += 1

		print("The list is palindrome")
		return True 