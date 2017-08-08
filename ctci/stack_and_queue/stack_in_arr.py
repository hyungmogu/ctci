class StackInArray(object):

	def __init__(self, size):

		self.arr = [None] * size
		self.size = size
		self.top = -1

	def push(self,value):
		if self.isFull():
			raise IndexError("[Error]: Operation stopped. Arr is full")

		self.top = self.top + 1
		self.arr[self.top] = value

	def pop(self):

		if self.isEmpty():
			raise LookupError("[Error]: Operation stopped. Arr is empty.")

		output = self.arr[self.top]
		self.top = self.top - 1

		return output

	def isEmpty(self):

		if self.top == -1:
			return True

		else:
			return False

	def isFull(self):

		if self.top == self.size - 1:
			return True
		else:
			return False
