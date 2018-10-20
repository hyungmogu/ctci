import unittest
import tree_node as t

class TestAddMethod(unittest.TestCase):

    def setUp(self):
        self.example1 = t.Node(1)

    def test_return_node_with_children_containing_added_value(self):
        expected = 2

        self.example1.add(2)
        result = self.example1.children[0].data

        self.assertEqual(expected, result)


class TestRemoveMethod(unittest.TestCase):
    def setUp(self):
        self.example1 = t.Node(1)

        self.example2 = t.Node(1)
        self.example2.add(2)
        self.example2.add(3)
        self.example2.add(4)
        self.example2.add(4)
        self.example2.add(5)
        self.example2.add(4)

    def test_return_type_error_if_value_is_not_basic_data_type(self):
        with self.assertRaises(TypeError):
            self.example1.remove([])
        with self.assertRaises(TypeError):
            self.example1.remove(t.Node(2))

    def test_return_node_with_children_without_ones_with_target_value(self):
        expected = "2,3,5"
        result = ''

        filtered_children = self.example2.remove(4)

        for idx,node in enumerate(self.example2.children):
            if idx != len(self.example2.children) - 1:
                result += str(node.data) + ','
            else:
                result += str(node.data)

        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()