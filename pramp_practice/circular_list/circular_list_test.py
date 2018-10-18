import unittest
import circular_list as c


class TestIsCircularMethod(unittest.TestCase):
    def setUp(self):
        self.example1 = c.LinkedList()

        self.example2 = c.LinkedList()
        self.example2.insert_first(1)

        self.example3 = c.LinkedList()
        self.example3.insert_first(1)
        self.example3.insert_first(2)

        self.example4 = c.LinkedList()
        self.example4.insert_first(5)
        self.example4.insert_first(4)
        self.example4.insert_first(3)
        self.example4.insert_first(2)
        self.example4.insert_first(1)

        node1 = c.Node(1)
        node2 = c.Node(2)
        node3 = c.Node(3)
        node4 = c.Node(4)
        node5 = c.Node(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node2

        self.example5 = c.LinkedList(node1)

    def test_return_false_if_linked_list_is_empty(self):
        expected = False

        result = self.example1.is_circular()

        self.assertEqual(expected, result)

    def test_return_false_if_linked_list_has_less_than_two_nodes(self):
        expected1 = False
        expected2 = False

        result1 = self.example2.is_circular()
        result2 = self.example3.is_circular()

        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)

    def test_return_false_if_linked_list_is_linear(self):
        expected = False
        result = self.example4.is_circular()

        self.assertEqual(expected, result)

    def test_return_true_if_circular_list_exists(self):
        expected = True
        result = self.example5.is_circular()

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()