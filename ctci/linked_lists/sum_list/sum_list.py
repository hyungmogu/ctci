class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList(object):
	def __init__(self, head = None):
		self.head = head

	def insert(self, node):
		if not isinstance(node, Node):
			raise TypeError("Operation stopped. Make sure the input variable 'node' is an instance of 'Node' object")

		if self.head == None:
			self.head = node
			return

		current = self.head

		while current.next != None:
			current = current.next

		current.next = node

	def display(self): 

		if self.head == None:
			return ""

		output = ""
		current = self.head

		while current != None:
			output = output + str(current.value) + " "
			current = current.next

		return output.rstrip()



def sum_list(number1, number2):

	if not isinstance(number1, LinkedList) or not isinstance(number2, LinkedList):
		raise TypeError("Operations stopped. The data type of one or more args is incorrect. Make sure both are instance of 'Node' object.")

	if number1.head == None or number2.head == None:
		raise ValueError("Operation stoppped. Make sure both linked list have at least one node.")

	output = LinkedList()
	current1 = number1.head
	current2 = number2.head
	current3 = output.head
	carry_over = 0

	while current1 != None:

		summed_value = current1.value + current2.value + carry_over
		if summed_value > 10:
			summed_value -= 10
			carry_over = 1
		else:
			carry_over = 0

		value_of_digit_for_the_output = Node(summed_value)

		if output.head == None:
			output.insert(value_of_digit_for_the_output)
			current3 = output.head

		else:
			current3.next = value_of_digit_for_the_output
			current3 = current3.next

		current1 = current1.next
		current2 = current2.next

	return output

