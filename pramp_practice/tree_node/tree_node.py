# Building a Tree
#
# {1}->{2}->{3}->{4}->{5}
#
#      {A}
#       |
#    -------
#    |  |  |
#   {B}{C}{D}
#
# -- Directions
# 1) Create a node class. The constructor should accept an
# arguement that gets assigned to the data property and
# initialize an empty array for storing children. The node class
# should have methods 'add' and 'remove'.

class Node:
    def __init__(self, value):
        # The constructor should accept an
        # arguement that gets assigned to the data property and
        # initialize an empty array for storing children.
        self.data = value
        self.children = []

    def add(self, value):
        # -- Direction
        # Given some data, create a new node and add it to
        # the current node's children array
        #
        # node = Node(1)
        #
        # node.add(2) --> self.children = [{2}]

        node = Node(value)
        self.children.append(node)

    def remove(self, value):
        # -- Direction
        # Given some data, look at each child of the current node
        # and remove any node with data == data
        #
        # remove 2
        #
        # [{1},{2},{3},{2},{5}]
        #
        #    |
        #    |
        #    v
        # [{1},{3},{5}]
        #
        #
        # remove 2
        #
        #  []
        #  |
        #  |
        #  v
        #  []
        #
        # remove [] --> TypeError
        #
        output = []

        if type(value) not in [str, int, bool, float]:
            raise TypeError

        if len(self.children) == 0:
            return

        for node in self.children:
            if node.data != value:
                output.append(node)

        self.children = output



