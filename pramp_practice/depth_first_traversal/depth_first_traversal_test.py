import unittest
import depth_first_traversal as b


class TestTraverseDF(unittest.TestCase):
    def setUp(self):
        self.example1 = b.Tree()

        example2_root_node = b.Node(1)
        self.example2 = b.Tree(example2_root_node)

        example3_root_node = b.Node(1)

        example3_l1_node1 = b.Node(2)
        example3_l2_node1 = b.Node(5)
        example3_l2_node2 = b.Node(6)
        example3_l2_node3 = b.Node(7)

        example3_l1_node2 = b.Node(3)

        example3_l1_node3 = b.Node(4)
        example3_l2_node4 = b.Node(8)
        example3_l2_node5 = b.Node(9)

        example3_l1_node1.children = [example3_l2_node1, example3_l2_node2, example3_l2_node3]
        example3_l1_node3.children = [example3_l2_node4, example3_l2_node5]
        example3_root_node.children = [example3_l1_node1, example3_l1_node2, example3_l1_node3]

        self.example3 = b.Tree(example3_root_node)

    def test_return_none_if_ll_is_empty(self):
        expected = None

        result = self.example1.traverse_by_bf()

        self.assertEqual(expected, result)

    def test_return_root_node_if_ll_has_size_one(self):
        expected = 1

        result = self.example2.traverse_by_bf().data

        self.assertEqual(expected ,result)

    def test_return_nodes_in_bf_order(self):
        expected = "1,2,5,6,7,3,4,8,9"
        result = ''

        traveled_nodes = self.example3.traverse_by_df()

        for idx,node in enumerate(traveled_nodes):
            if idx != len(traveled_nodes) - 1:
                result += str(node.data) + ','
            else:
                result += str(node.data)

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()