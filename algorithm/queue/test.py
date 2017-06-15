import unittest

import queue as q

class TestEnqueue(unittest.TestCase):

	def test_default(self):
		queue = q.Queue(1)
		queue.enqueue(2)
		self.assertEqual(queue.storage,[1,2])

class TestDequeue(unittest.TestCase):

	def test_default(self):
		queue = q.Queue(1)
		queue.enqueue(2)
		queue.dequeue()
		self.assertEqual(queue.storage,[2])

class TestPeek(unittest.TestCase):

	def test_peek(self):
		queue = q.Queue(1)
		queue.enqueue(2)
		queue.enqueue(3)

		self.assertEqual(queue.peek(),1)


if __name__ == '__main__':
	unittest.main()