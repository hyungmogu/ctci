import unittest
import stack as s

class TestStackPush(unittest.TestCase):
    def setUp(self):
        self.example1 = s.Stack()

    def test_return_stack_array_with_elements_after_push(self):
        expected = [1,2,3]

        self.example1.push(1)
        self.example1.push(2)
        self.example1.push(3)

        result = self.example1.stack

        self.assertEqual(expected, result)

class TestStackPop(unittest.TestCase):
    def setUp(self):
        self.example1 = s.Stack()

        self.example2 = s.Stack()
        self.example2.push(1)
        self.example2.push(2)
        self.example2.push(3)
        self.example2.push(4)
        self.example2.push(5)

        self.example3 = s.Stack()
        self.example3.push(1)
        self.example3.push(2)
        self.example3.push(3)
        self.example3.push(4)
        self.example3.push(5)

    def test_return_none_if_array_is_empty(self):
        expected = None

        result = self.example1.pop()

        self.assertEqual(expected, result)

    def test_return_popped_value_after_operation(self):
        expected = 5

        result = self.example2.pop()

        self.assertEqual(expected, result)

    def test_return_array_without_popped_value_after_operation(self):
        expected = [1,2,3,4]

        self.example3.pop()
        result = self.example3.stack

        self.assertEqual(expected, result)

class TestStackPeek(unittest.TestCase):
    def setUp(self):
        self.example1 = s.Stack()

        self.example2 = s.Stack()
        self.example2.push(1)
        self.example2.push(2)
        self.example2.push(3)
        self.example2.push(4)
        self.example2.push(5)

    def test_return_none_if_length_is_zero(self):
        expected = None
        result = self.example1.peek()
        self.assertEqual(expected, result)

    def test_return_value_if_length_is_non_zero(self):
        expected = 5
        result = self.example2.peek()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()