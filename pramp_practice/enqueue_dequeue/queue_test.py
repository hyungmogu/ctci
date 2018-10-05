import unittest
import queue as q

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.example1 = q.Queue()

    def test_return_head_of_empty_array_on_initialization(self):
        expected = []
        result = self.example1.queue

        self.assertEqual(expected, result)

class TestEnqueue(unittest.TestCase):
    def setUp(self):
        self.example1 = q.Queue()

    def test_return_array_containing_first_added_element_after_enqueue(self):
        expected = [1]

        self.example1.enqueue(1)
        result = self.example1.queue

        self.assertEqual(expected, result)

    def test_return_array_with_last_element_being_first_enqueued_element_if_two_elements_are_added(self):
        expected = 1

        self.example1.enqueue(1)
        self.example1.enqueue(2)
        result = self.example1.queue[-1]

        self.assertEqual(expected,result)

class TestDequeue(unittest.TestCase):
    def setUp(self):
        self.example1 = q.Queue()
        self.example1.enqueue(1)
        self.example1.enqueue(2)

    def test_return_value_error_if_there_is_none_to_dequeue(self):
        with self.assertRaises(ValueError):
            self.example1.dequeue()
            self.example1.dequeue()
            self.example1.dequeue()

    def test_return_first_registered_value_on_dequeue(self):
        expected =  1
        result = self.example1.dequeue()

        self.assertEqual(expected, result)

    def test_return_second_registered_value_on_secondDequeue(self):
        expected = 2
        self.example1.dequeue()
        result = self.example1.dequeue()

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()