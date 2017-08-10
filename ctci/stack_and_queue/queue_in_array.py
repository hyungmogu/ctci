class QueueInArray(object):

	def __init__(self, size):
		self.front = -1
		self.rear = -1
		self.arr = [None] * size
		self.size = size


	def enqueue(self, value):
		if self.rear == self.size - 1:
			raise IndexError("Operation stopped. Array is full")

		if self.rear == -1 and self.front == -1:

			self.rear += 1
			self.arr[self.rear] = value
			self.front += 1
			return

		self.rear += 1
		self.arr[self.rear] = value


	def dequeue(self):
		# This is not necessary. The below code covers it.
		# if self.rear == self.size:
		# 	raise IndexError("Operation stopped. Index out of bounds")

		if self.rear < self.front:
			raise LookupError("Operation stopped. There are no values to dequeue")

		temp = self.arr[self.front]
		self.front += 1
		return temp