import unittest
import from_last as l


class TestFromLastMethod(unittest.TestCase):
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

    def test_return_type_error_if_n_is_not_integer(self):
        with self.assertRaises(TypeError):
            self.example1.from_last('hello world')

    def test_return_index_error_if_n_is_negative(self):
        with self.assertRaises(IndexError):
            self.example1.from_last(-1)

    def test_return_index_error_if_linked_list_is_empty(self):
        with self.assertRaises(IndexError):
            self.example1.from_last(0)

    def test_return_head_node_if_linked_list_has_only_one_node(self):
        expected = 1

        result = self.example2.from_last(0).data

        self.assertEqual(expected, result)

    def test_return_last_node_when_n_is_0(self):
        expected = 5

        result = self.example3.from_last(0).data

        self.assertEqual(expected, result)

    def test_return_2nd_node_from_last(self):
        expected = 3

        result = self.example3.from_last(2).data

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

