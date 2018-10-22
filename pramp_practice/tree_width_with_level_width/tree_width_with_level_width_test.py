import unittest
import tree_with_level_width as t

class TestGetLevelWidth(unittest.TestCase):

    def setUp(self):
        self.example1 = t.Tree()

        example2_root_node = t.Node(1)
        self.example2 = t.Tree(example2_root_node)

        example3_root_node = t.Node(1)

        example3_l1_node1 = t.Node(2)
        example3_l2_node1 = t.Node(5)
        example3_l2_node2 = t.Node(6)
        example3_l2_node3 = t.Node(7)

        example3_l1_node2 = t.Node(3)

        example3_l1_node3 = t.Node(4)
        example3_l2_node4 = t.Node(8)
        example3_l2_node5 = t.Node(9)

        example3_l1_node1.children = [example3_l2_node1, example3_l2_node2, example3_l2_node3]
        example3_l1_node3.children = [example3_l2_node4, example3_l2_node5]
        example3_root_node.children = [example3_l1_node1, example3_l1_node2, example3_l1_node3]

        self.example3 = t.Tree(example3_root_node)

    def test_return_return_empty_array_when_tree_is_empty(self):
        expected = []

        result = self.example1.get_level_width()

        self.assertEqual(expected, result)

    def test_return_return_array_with_value_1_when_only_root_node_exists(self):
        expected = [1]

        result = self.example2.get_level_width()

        self.assertEqual(expected, result)

    def test_return_return_array_of_tree_width_when_tree_has_more_than_1_lvl(self):
        expected = [1,3,5]

        result = self.example3.get_level_width()

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()