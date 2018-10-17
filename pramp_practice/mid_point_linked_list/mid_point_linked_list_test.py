import unittest
import mid_point_linked_list as l

class TestMidPointLinkedList(unittest.TestCase):
    def setUp(self):
        self.example1 = l.LinkedList()

        self.example2 = l.LinkedList()
        self.example2.insert_first(1)

        self.example3 = l.LinkedList()
        self.example3.insert_first(5)
        self.example3.insert_first(4)
        self.example3.insert_first(3)
        self.example3.insert_first(2)
        self.example3.insert_first(1)

        self.example4 = l.LinkedList()
        self.example4.insert_first(4)
        self.example4.insert_first(3)
        self.example4.insert_first(2)
        self.example4.insert_first(1)

    def test_return_none_if_linked_list_is_empty(self):
        expected = None

        result = self.example1.get_mid_point()

        self.assertEqual(expected, result)

    def test_return_head_if_size_of_linked_list_is_one(self):
        expected = 1

        result = self.example2.get_mid_point().data

        self.assertEqual(expected, result)

    def test_return_mid_node_if_ll_is_greater_than_one(self):
        expected1 = 3
        expected2 = 2

        result1 = self.example3.get_mid_point().data
        result2 = self.example4.get_mid_point().data

        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)

if __name__ == '__main__':
    unittest.main()