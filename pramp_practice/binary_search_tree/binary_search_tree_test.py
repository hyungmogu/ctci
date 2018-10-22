import unittest
import binary_search_tree as b

class TestInsertMethod(unittest.TestCase):
    def setUp(self):
        self.example1 = b.Node(1)

        self.example2 = b.Node(2)
        self.example2.insert(1)
        self.example2.insert(4)
        self.example2.insert(3)
        self.example2.insert(5)

    def test_return_type_error_if_value_is_not_basic_data_type(self):
        with self.assertRaises(TypeError):
            self.example1.insert([])

        with self.assertRaises(TypeError):
            self.example1.insert(b.Node(3))

    def test_return_values_in_ascending_order_when_travsersed_in_order(self):
        expected = "1,2,3,4,5"
        output = []

        b.Tree.in_order_traversal(self.example2, output)
        output = [str(x) for x in output]
        result = ",".join(output)

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()