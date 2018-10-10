import unittest
import two_become_one as t


class TestTwoBecomeOneInitialization(unittest.TestCase):
    def setUp(self):
        self.example1 = t.Queue()

    def test_return_two_stacks_on_initialization(self):
        expected = True

        result =  (hasattr(self.example1, 'stack1') and
                    hasattr(self.example1, 'stack2'))

        self.assertEqual(expected, result)

class TestTwoBecomeOnePeek(unittest.TestCase):
    def setUp(self):
        self.example1 = t.Queue()

        self.example2 = t.Queue()
        self.example2.enqueue(1)
        self.example2.enqueue(2)

    def test_return_none_if_empty(self):
        expected = None
        result = self.example1.peek()
        self.assertEqual(expected, result)

    def test_return_first_added_element_if_not_empty(self):
        expected = 1

        result = self.example2.peek()

        self.assertEqual(expected, result)

class TestTwoBecomeOneEnqueue(unittest.TestCase):
    def setUp(self):
        self.example1 = t.Queue()

    def test_return_queue_containing_first_added_element_after_enqueue(self):
        expected = 1

        self.example1.enqueue(1)
        result = self.example1.peek()

        self.assertEqual(expected, result)

    def test_return_first_added_element_if_two_elements_are_added(self):
        expected = 1

        self.example1.enqueue(1)
        self.example1.enqueue(2)
        result = self.example1.peek()

        self.assertEqual(expected,result)

class TestTwoBecomeOneDequeue(unittest.TestCase):
    def setUp(self):
        self.example1 = t.Queue()
        self.example1.enqueue(1)
        self.example1.enqueue(2)

        self.example2 = t.Queue()
        self.example2.enqueue(1)
        self.example2.enqueue(2)

        self.example3 = t.Queue()
        self.example3.enqueue(1)
        self.example3.enqueue(2)

    def test_return_none_if_there_is_none_to_dequeue(self):
        expected = None

        self.example1.dequeue()
        self.example1.dequeue()
        result = self.example1.dequeue()

        self.assertEqual(expected, result)

    def test_return_first_registered_value_on_dequeue(self):
        expected =  1
        result = self.example2.dequeue()

        self.assertEqual(expected, result)

    def test_return_second_registered_value_on_secondDequeue(self):
        expected = 2
        self.example3.dequeue()
        result = self.example3.dequeue()

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()