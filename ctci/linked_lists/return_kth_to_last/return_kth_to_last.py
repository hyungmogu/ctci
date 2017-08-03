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

	def display(self):
		current = self.head
		output = ""
		while current != None:
			output = output + "{0} ".format(current.value)
			current = current.next

		output = output.rstrip()
		print(output)
		return output

	def remove_duplicates(self):
		if self.head == None:
			print("The head is empty")
			return

		if self.head.next == None:
			print("There exists only one node")
			return

		node_being_examined = self.head

		while node_being_examined != None:
			node_to_be_deleted_if_duplicate = node_being_examined.next
			parent = node_being_examined

			while node_to_be_deleted_if_duplicate != None:

				if node_being_examined.value != node_to_be_deleted_if_duplicate.value:
					parent = parent.next
					node_to_be_deleted_if_duplicate = node_to_be_deleted_if_duplicate.next
					break;

				node_to_be_deleted_if_duplicate = node_to_be_deleted_if_duplicate.next
				parent.next.next = None
				parent.next = node_to_be_deleted_if_duplicate

			node_being_examined = node_being_examined.next

	def is_empty(self):
		if self.head == None:
			return True
		return False

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

	def get_kth_to_last_element(self, k):

		current = self.head
		n = self.get_size()
		i = 0

		if self.head == None:
			print("Head is empty")
			return None

		if self.head.next == None:
			return self.head

		if k >= n:
			print("Wrong value of k")
			return None

		while i < (n - (k+1)):
			current = current.next
			i += 1

		return current
