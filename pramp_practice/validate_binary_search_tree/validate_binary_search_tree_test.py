import unittest
import validate_binary_search_tree as v
import nodes as n

class TestValidateBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.example1 = n.NodeTree(1)

        example1_l1_node1 = n.NodeTree(2)
        example1_l2_node1 = n.NodeTree(5)
        example1_l2_node2 = n.NodeTree(6)
        example1_l2_node3 = n.NodeTree(7)

        example1_l1_node2 = n.NodeTree(3)

        example1_l1_node3 = n.NodeTree(4)
        example1_l2_node4 = n.NodeTree(8)
        example1_l2_node5 = n.NodeTree(9)

        example1_l1_node1.children = [example1_l2_node1, example1_l2_node2, example1_l2_node3]
        example1_l1_node3.children = [example1_l2_node4, example1_l2_node5]
        self.example1.children = [example1_l1_node1, example1_l1_node2, example1_l1_node3]

        self.example2 = n.NodeBinaryTree(1)

        self.example2.lchild = n.NodeBinaryTree(2)
        self.example2.rchild = n.NodeBinaryTree(4)

        self.example2.lchild.rchild = n.NodeBinaryTree(10)

    def test_return_false_if_a_node_does_not_have_lchild_and_rchild(self):
        expected = False

        result = v.Tree.validate_bst(self.example1)

        self.assertEqual(expected, result)

    def test_return_false_if_in_order_traversal_of_tree_has_elements_not_in_order(self):
        expected = False

        result = v.Tree.validate_bst(self.example2)

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()