import unittest
import weave as w
import queue as q

class TestWeave(unittest.TestCase):
    def setUp(self):
        self.queue1_example1 = q.Queue()
        self.queue1_example1.queue = [1,2,3]
        self.queue2_example1 = ""

        self.queue1_example2 = q.Queue()
        self.queue2_example2 = q.Queue()

        self.queue1_example3 = q.Queue()
        self.queue1_example3.enqueue(3)
        self.queue1_example3.enqueue(2)
        self.queue1_example3.enqueue(1)
        self.queue2_example3 = q.Queue()
        self.queue2_example3.enqueue(6)
        self.queue2_example3.enqueue(5)
        self.queue2_example3.enqueue(4)

        self.queue1_example4 = q.Queue()
        self.queue1_example4.enqueue(2)
        self.queue1_example4.enqueue(1)
        self.queue2_example4 = q.Queue()
        self.queue2_example4.enqueue(6)
        self.queue2_example4.enqueue(5)
        self.queue2_example4.enqueue(4)
        self.queue2_example4.enqueue(3)

    def test_return_type_error_if_inputs_are_not_of_object_Queue(self):
        with self.assertRaises(TypeError):
            w.weave(self.queue1_example1, self.queue2_example1)

        with self.assertRaises(TypeError):
            w.weave(self.queue2_example1, self.queue1_example1)

    def test_return_value_error_if_one_of_two_arrays_are_empty(self):
        with self.assertRaises(ValueError):
            w.weave(self.queue1_example2, self.queue2_example2)

        with self.assertRaises(ValueError):
            w.weave(self.queue2_example2, self.queue1_example2)

    def test_return_array_of_alternating_values_if_two_arrays_have_same_size(self):
        expected = [4,1,5,2,6,3]

        result = w.weave(self.queue1_example3, self.queue2_example3)

        for i in range(len(expected)):
            self.assertEqual(expected[-1 * (i + 1)], result.dequeue())

    def test_return_array_of_alternating_values_if_two_arrays_have_same_size_2(self):
        expected = [1,4,2,5,3,6]

        result = w.weave(self.queue2_example3, self.queue1_example3)

        for i in range(len(expected)):
            self.assertEqual(expected[-1 * (i + 1)], result.dequeue())

    def test_return_array_of_alternating_values_with_tails_from_lengthier_array_if_uneven(self):
        expected = [3,4,5,1,6,2]

        result = w.weave(self.queue1_example4, self.queue2_example4)

        for i in range(len(expected)):
            self.assertEqual(expected[-1 * (i + 1)], result.dequeue())

    def test_return_array_of_alternating_values_with_tails_from_lengthier_array_if_uneven_2(self):
        expected = [3,4,1,5,2,6]

        result = w.weave(self.queue2_example4, self.queue1_example4)

        for i in range(len(expected)):
            self.assertEqual(expected[-1 * (i + 1)], result.dequeue())

if __name__ == '__main__':
    unittest.main()