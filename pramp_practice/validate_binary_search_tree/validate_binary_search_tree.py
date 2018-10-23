# Validating Binary Search Tree
#
# Given a node, validate the binary search tree.
# Ensure that every node's left hand child is
# less than the parent node's value, and that
# every node's right hand child is greater than
# the parent.

import nodes as n

class Tree:
    def __init__(self, node = None):
        self.root = node

    @staticmethod
    def validate_bst(root_node):
        nodes_in_order = []

        if (hasattr(root_node, 'lchild') and root_node.lchild == None) and (hasattr(root_node, 'lchild') and root_node.rchild == None):
            return True

        try:
            Tree.in_order_traversal(root_node, nodes_in_order)
        except AttributeError:
            return False

        for i in range(1, len(nodes_in_order)):
            if nodes_in_order[i-1].data > nodes_in_order[i].data:
                return False

        return True


    @staticmethod
    def in_order_traversal(node, output):
        if not hasattr(node, 'lchild') or not hasattr(node, 'rchild'):
            raise AttributeError

        if node == None:
            return

        Tree.in_order_traversal(node.lchild, output)
        output.append(node)
        Tree.in_order_traversal(node.rchild, output)