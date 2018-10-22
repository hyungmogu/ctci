# Binary Search Tree
# -- Direction
# 1) Implement the Node class to create
# a binary search tree. The constructor
# should initialize values 'data', 'left',
# and 'right'
#
# 2) Implement the 'insert' method for the
# Node class. Insert should accept an arguement
# 'data', then create an insert a new node at the
# appropriate location in the tree

class Node:
    def __init__(self, value):
        self.data = value
        self.lchild = None
        self.rchild = None

    def insert(self, value):

        if type(value) not in [str, int, bool, float]:
            raise TypeError

        node = Node(value)
        still_travelling = True
        current_node = None

        if self.lchild == None and self.rchild == None:
            if value > self.data:
                self.rchild = node
            else:
                self.lchild = node
            return

        if value > self.data:
            if self.rchild != None:
                current_node = self.rchild
            else:
                self.rchild = node
                return
        else:
            if self.lchild != None:
                current_node = self.lchild
            else:
                self.lchild = node
                return

        while still_travelling:
            if value > current_node.data:
                if current_node.rchild != None:
                    current_node = self.rchild
                else:
                    current_node.rchild = node
                    still_travelling = False
            else:
                if current_node.lchild != None:
                    current_node = self.lchild
                else:
                    current_node.lchild = node
                    still_travelling = False


class Tree:
    def __init__(self, node):
        self.root = node

    @staticmethod
    def in_order_traversal(node, output):
        if node == None:
            return

        Tree.in_order_traversal(node.lchild, output)
        output.append(node.data)
        Tree.in_order_traversal(node.rchild, output)