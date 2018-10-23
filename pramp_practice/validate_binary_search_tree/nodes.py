class NodeLinkedList:
    def __init__(self, e):
        self.data = e
        self.next = None

class NodeTree:
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

class NodeBinaryTree:
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