import unittest
import queue_in_array as q


class TestEnqueueMethod(unittest.TestCase):

	def setUp(self):
		self.queue_in_arr = q.QueueInArray(3)


	def test_when_arr_is_empty(self):
		self.queue_in_arr.enqueue(1)
		self.assertEqual(self.queue_in_arr.rear, 0)
		self.assertEqual(self.queue_in_arr.front, 0)
		self.assertEqual(self.queue_in_arr.arr[0], 1)


	def test_when_arr_is_not_empty(self): 
		self.queue_in_arr.enqueue(1)
		self.queue_in_arr.enqueue(2)
		self.assertEqual(self.queue_in_arr.rear, 1)
		self.assertEqual(self.queue_in_arr.front, 0)
		self.assertEqual(self.queue_in_arr.arr[1], 2)

		self.queue_in_arr.enqueue(3)

		self.assertEqual(self.queue_in_arr.rear, 2)
		self.assertEqual(self.queue_in_arr.front, 0)
		self.assertEqual(self.queue_in_arr.arr[2], 3)

	def test_when_arr_is_full(self):
		self.queue_in_arr.enqueue(1)
		self.queue_in_arr.enqueue(2)
		self.queue_in_arr.enqueue(3)

		with self.assertRaises(IndexError):
			self.queue_in_arr.enqueue(4)


class TestDequeueMethod(unittest.TestCase):

	def setUp(self):
		self.queue_in_arr = q.QueueInArray(3)


	def test_when_rear_is_gt_front(self):

		self.queue_in_arr.enqueue(1)
		self.queue_in_arr.enqueue(2)

		self.queue_in_arr.dequeue()
		self.queue_in_arr.dequeue()

		with self.assertRaises(LookupError):
			self.queue_in_arr.dequeue()

	def test_when_rear_is_out_of_bounds(self):

		self.queue_in_arr.enqueue(1)
		self.queue_in_arr.enqueue(2)
		self.queue_in_arr.enqueue(3)

		self.queue_in_arr.dequeue()
		self.queue_in_arr.dequeue()
		self.queue_in_arr.dequeue()

		with self.assertRaises(LookupError):
			self.queue_in_arr.dequeue()

	def test_normal_case(self):

		self.queue_in_arr.enqueue(1)
		self.queue_in_arr.enqueue(2)

		val1 = self.queue_in_arr.dequeue()
		val2 = self.queue_in_arr.dequeue()

		self.assertEqual(val1, 1)
		self.assertEqual(val2, 2)

if __name__ == "__main__":
	unittest.main()
