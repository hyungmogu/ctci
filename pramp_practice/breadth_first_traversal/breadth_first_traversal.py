# -- Directions
# 1) Create a node class. The constructor should accept an
# arguement that gets assigned to the data property and
# initialize an empty array for storing children. The node class
# should have methods 'add' and 'remove'.
#
# 2) Create a tree class. The tree constructor should initialize a
# 'root' property to null.
#
# 3) Implement 'traverseBF' and 'traverseDF' on the tree class.
# each method should accept a function that gets called with each
# each element in the tree.

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, n):
        self.queue = [n] + self.queue

    def dequeue(self):
        if len(self.queue) == 0:
            raise ValueError

        output = self.queue.pop()
        return output

    def peek(self):
        if len(self.queue) == 0:
            return None

        return self.queue[-1]

class Node:
    def __init__(self, value):
        self.data = value
        self.children = []

    def add(self, value):

        node = Node(value)
        self.children.append(node)

    def remove(self, value):
        output = []

        if type(value) not in [str, int, bool, float]:
            raise TypeError

        if len(self.children) == 0:
            return

        for node in self.children:
            if node.data != value:
                output.append(node)

        self.children = output

class Tree:
    def __init__(self, e = None):
        self.root = e

    def traverse_by_bf(self):
        #
        # Example 1
        #
        #              1
        #              |
        #       ----------------
        #       |      |       |
        #       2      3       4
        #       |              |
        #    -------        -------
        #    |  |  |        |     |
        #    5  6  7        8     9
        #
        #
        # root_node = b.Node(1)
        #
        # l1_node1 = b.Node(2)
        # l2_node1 = b.Node(5)
        # l2_node2 = b.Node(6)
        # l2_node3 = b.Node(7)
        #
        # l1_node2 = b.Node(3)
        #
        # l1_node3 = b.Node(4)
        # l2_node4 = b.Node(8)
        # l2_node5 = b.Node(9)
        #
        # l1_node1.children = [example2_l2_node1, example2_l2_node2, example2_l2_node3]
        # l1_node3.children = [example2_l2_node4, example2_l2_node5]
        # root_node.children = [example2_l1_node1, example2_l1_node2, example2_l1_node3]
        #
        # example1 = Tree(root_node)
        # example1.traverse_by_bf() --> [{1},{2},{3},{4},{5},{6},{7},{8},{9}]
        #
        #
        # Example 2
        #
        #           1
        #
        # root_node = Node(1)
        # example2 = Tree(root_node)
        # example2.traverse_by_bf() --> {1}
        #
        #
        #
        # Example 3
        #
        #        Nothing
        #
        # exmaple3 = Tree()
        # example3.traverse_by_bf() --> None


        # Brainstorming Solution
        #
        # Example 3
        #
        # Example 2
        #
        # Example 1
        #                               queue = [{1}]
        #
        #              1                queue = [{2},{3},{4}]
        #              |                output = [{1}]
        #       ----------------
        #       |      |       |
        #       2      3       4        queue = [{5},{6},{7},{8},{9}]
        #       |              |        output = [{1},{2},{3},{4}]
        #    -------        -------
        #    |  |  |        |     |
        #    5  6  7        8     9     queue = []
        #                               output = [{1},{2},{3},{4},{5},{6},{7},{8},{9}]
        #

        queue = Queue()
        output = []

        if self.root == None:
            return None

        if len(self.root.children) == 0:
            return self.root

        queue.enqueue(self.root)

        while queue.peek() != None:
            node = queue.dequeue()
            output.append(node)

            if len(node.children) == 0:
                continue

            for child in node.children:
                queue.enqueue(child)

        return output