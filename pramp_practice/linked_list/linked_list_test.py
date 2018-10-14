import unittest
import linked_list as l

class TestInsertFirstMethod(unittest.TestCase):
    def setUp(self):
        self.example1 = l.LinkedList()

        self.example2 = l.LinkedList()

    def test_return_ll_with_head_being_the_inserted_node(self):
        expected = 1

        self.example1.insert_first(1)
        result = self.example1.head.data

        self.assertEqual(expected, result)

    def test_return_ll_with_previous_head_node_when_next_is_called(self):
        expected = 1

        self.example2.insert_first(1)
        self.example2.insert_first(2)
        result = self.example2.head.next.data

        self.assertEqual(expected, result)

class TestSizeMethod(unittest.TestCase):
    def setUp(self):
        self.example1 = l.LinkedList()

        self.example2 = l.LinkedList()
        self.example2.insert_first(1)
        self.example2.insert_first(2)
        self.example2.insert_first(3)
        self.example2.insert_first(4)

    def test_return_size_0_if_ll_is_empty(self):
        expected = 0
        result = self.example1.size()
        self.assertEqual(expected, result)

    def test_return_size_of_4_with_ll_of_4_nodes(self):
        expected = 4
        result = self.example2.size()
        self.assertEqual(expected, result)

class TestGetAtMethod(unittest.TestCase):
    def setUp(self):
        self.example1 = l.LinkedList()

        self.example2 = l.LinkedList()
        self.example2.insert_first(5)
        self.example2.insert_first(4)
        self.example2.insert_first(3)
        self.example2.insert_first(2)
        self.example2.insert_first(1)

    def test_return_type_error_if_input_is_not_integer(self):
        with self.assertRaises(TypeError):
            self.example1.get_at('hello')

    def test_return_value_error_if_input_is_negative(self):
        with self.assertRaises(ValueError):
            self.example1.get_at(-10 )

    def test_return_index_error_if_out_of_bound(self):
        with self.assertRaises(IndexError):
            self.example1.get_at(10)

    def test_return_node_if_exists(self):
        expected = 4

        returned_node = self.example2.get_at(3)
        result = returned_node.data

        self.assertEqual(expected, result)

class TestInsertAtMethod(unittest.TestCase):
    def setUp(self):
        self.example1 = l.LinkedList()
        self.example1.insert_first(1)
        self.example1.insert_first(2)
        self.example1.insert_first(3)
        self.example1.insert_first(4)

        self.example2 = l.LinkedList()
        self.example2.insert_first(1)
        self.example2.insert_first(2)
        self.example2.insert_first(3)
        self.example2.insert_first(4)

        self.example3 = l.LinkedList()
        self.example3.insert_first(1)
        self.example3.insert_first(2)
        self.example3.insert_first(3)
        self.example3.insert_first(4)

    def test_return_type_error_if_position_is_not_integer(self):
        with self.assertRaises(TypeError):
            self.example1.insert_at('hello', 10)

    def test_return_value_error_if_position_is_negative(self):
        with self.assertRaises(ValueError):
            self.example1.insert_at(-20,10)

    def test_return_index_error_if_out_of_bound(self):
        with self.assertRaises(IndexError):
            self.example2.insert_at(10,2)

    def test_ll_has_inserted_node_at_position_if_insertion_successful(self):
        expected = 10

        self.example2.insert_at(1, 10)
        returned_node = self.example2.get_at(1)
        result = returned_node.data

        self.assertEqual(expected, result)

    def test_ll_has_head_of_inserted_node_if_insertion_is_at_position_0(self):
        expected = 11

        self.example2.insert_at(0, 11)
        returned_node = self.example2.get_at(0)
        result = returned_node.data

        self.assertEqual(expected, result)

    def test_ll_has_last_node_being_the_inserted_node_if_insertion_is_at_last_position(self):
        expected = 12

        self.example1.insert_at(3, 12)
        returned_node = self.example1.get_at(3)
        result = returned_node.data

        self.assertEqual(expected, result)

class TestRemoveAtMethod(unittest.TestCase):
    def setUp(self):
        self.example1 = l.LinkedList()

        self.example2 = l.LinkedList()
        self.example2.insert_first(5)
        self.example2.insert_first(4)
        self.example2.insert_first(3)
        self.example2.insert_first(2)
        self.example2.insert_first(1)

        self.example3 = l.LinkedList()
        self.example3.insert_first(5)
        self.example3.insert_first(4)
        self.example3.insert_first(3)
        self.example3.insert_first(2)
        self.example3.insert_first(1)

    def test_return_type_error_if_input_is_not_integer(self):
        with self.assertRaises(TypeError):
            self.example1.remove_at('hello')

    def test_return_value_error_if_ll_is_empty(self):
        with self.assertRaises(ValueError):
            self.example1.remove_at(2)

    def test_return_index_error_if_out_of_bound(self):
        with self.assertRaises(IndexError):
            self.example2.remove_at(10)

    def test_return_ll_with_size_1_less_than_previous_after_removal(self):
        expected = 4

        self.example2.remove_at(2)
        result = self.example2.size()

        self.assertEqual(expected, result)

    def test_return_ll_with_next_node_occupying_the_position_after_removal(self):
        expected = 3

        self.example3.remove_at(1)
        returned_node = self.example3.get_at(1)
        result = returned_node.data

        self.assertEqual(expected, result)

class TestGetFirstMethod(unittest.TestCase):
    def setUp(self):
        self.example1 = l.LinkedList()

        self.example2 = l.LinkedList()
        self.example2.insert_first(5)
        self.example2.insert_first(4)
        self.example2.insert_first(3)
        self.example2.insert_first(2)
        self.example2.insert_first(1)

    def test_return_none_if_ll_empty(self):
        expected = None

        result = self.example1.get_first()

        self.assertEqual(expected, result)

    def test_return_node_if_exists(self):
        expected = 1

        returned_node = self.example2.get_first()
        result = returned_node.data

        self.assertEqual(expected, result)

class TestGetLastMethod(unittest.TestCase):
    def setUp(self):
        self.example1 = l.LinkedList()

        self.example2 = l.LinkedList()
        self.example2.insert_first(5)
        self.example2.insert_first(4)
        self.example2.insert_first(3)
        self.example2.insert_first(2)
        self.example2.insert_first(1)

    def test_return_none_if_ll_empty(self):
        expected = None

        result = self.example1.get_last()

        self.assertEqual(expected, result)

    def test_return_last_node_if_ll_not_empty(self):
        expected = 5

        returned_node = self.example2.get_last()
        result = returned_node.data

        self.assertEqual(expected, result)

class TestRemoveFirstMethod(unittest.TestCase):
    def setUp(self):
        self.example1 = l.LinkedList()

        self.example2 = l.LinkedList()
        self.example2.insert_first(5)
        self.example2.insert_first(4)
        self.example2.insert_first(3)
        self.example2.insert_first(2)
        self.example2.insert_first(1)

        self.example3 = l.LinkedList()
        self.example3.insert_first(5)
        self.example3.insert_first(4)
        self.example3.insert_first(3)
        self.example3.insert_first(2)
        self.example3.insert_first(1)

        self.example4 = l.LinkedList()
        self.example4.insert_first(5)
        self.example4.insert_first(4)
        self.example4.insert_first(3)
        self.example4.insert_first(2)
        self.example4.insert_first(1)

    def test_return_value_error_if_ll_empty(self):
        with self.assertRaises(ValueError):
            self.example1.remove_first()

    def test_return_ll_with_head_being_the_next_node(self):
        expected = 2

        self.example3.remove_first()
        result = self.example3.head.data

        self.assertEqual(expected, result)

    def test_return_ll_with_size_one_less_than_previous(self):
        expected = 4

        self.example4.remove_first()
        result = self.example4.size()

        self.assertEqual(expected, result)

class TestRemoveLastMethod(unittest.TestCase):
    def setUp(self):
        self.example1 = l.LinkedList()

        self.example2 = l.LinkedList()
        self.example2.insert_first(5)
        self.example2.insert_first(4)
        self.example2.insert_first(3)
        self.example2.insert_first(2)
        self.example2.insert_first(1)

        self.example3 = l.LinkedList()
        self.example3.insert_first(5)
        self.example3.insert_first(4)
        self.example3.insert_first(3)
        self.example3.insert_first(2)
        self.example3.insert_first(1)

    def test_return_value_error_if_ll_empty(self):
        with self.assertRaises(ValueError):
            self.example1.remove_last()

    def test_return_ll_with_size_1_minus_previous(self):
        expected = 4

        self.example2.remove_last()
        result = self.example2.size()

        self.assertEqual(expected, result)

    def test_return_ll_with_the_last_being_prev_node(self):
        expected = 4

        self.example3.remove_last()
        returned_node = self.example3.get_at(3)
        result = returned_node.data

        self.assertEqual(expected, result)

class TestInsertLastMethod(unittest.TestCase):
    def setUp(self):
        self.example1 = l.LinkedList()

        self.example2 = l.LinkedList()
        self.example2.insert_first(5)
        self.example2.insert_first(4)
        self.example2.insert_first(3)
        self.example2.insert_first(2)
        self.example2.insert_first(1)

        self.example3 = l.LinkedList()
        self.example3.insert_first(5)
        self.example3.insert_first(4)
        self.example3.insert_first(3)
        self.example3.insert_first(2)
        self.example3.insert_first(1)

    def test_return_ll_with_head_being_the_node_if_empty(self):
        expected = 1

        self.example1.insert_last(1)
        result = self.example1.head.data

        self.assertEqual(expected, result)

    def test_return_ll_with_size_being_1_more_than_previous(self):
        expected = 6

        self.example2.insert_last(10)
        result = self.example2.size()

        self.assertEqual(expected, result)

    def test_return_ll_with_the_last_being_the_inserted_node(self):
        expected = 10

        self.example3.insert_last(10)
        returned_node = self.example3.get_at(5)
        result = returned_node.data

        self.assertEqual(expected, result)

class TestClearMethod(unittest.TestCase):
    def setUp(self):
        self.example1 = l.LinkedList()

        self.example2 = l.LinkedList()
        self.example2.insert_first(5)
        self.example2.insert_first(4)
        self.example2.insert_first(3)
        self.example2.insert_first(2)
        self.example2.insert_first(1)

        self.example3 = l.LinkedList()
        self.example3.insert_first(5)
        self.example3.insert_first(4)
        self.example3.insert_first(3)
        self.example3.insert_first(2)
        self.example3.insert_first(1)

    def test_return_ll_with_size_0(self):
        expected = 0

        self.example1.clear()
        self.example2.clear()

        result1 = self.example1.size()
        result2 = self.example2.size()

        self.assertEqual(expected, result1)
        self.assertEqual(expected, result2)

    def test_return_ll_with_head_being_none(self):
        expected = None

        self.example3.clear()
        result = self.example3.head

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

