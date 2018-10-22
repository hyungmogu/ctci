# tree with level width
# -- direction
# Given the root node of a tree, return an array
# where each element is the width of the tree at
# each level


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

    def get_level_width(self):
        queue = Queue()
        output = []

        if self.root == None:
            return []

        if len(self.root.children) == 0:
            return [1]

        queue.enqueue(self.root)
        output.append(1)

        while queue.peek() != None:
            queue_nxt_lvl = []
            while queue.peek() != None:
                node = queue.dequeue()

                if len(node.children) == 0:
                    continue

                for child in node.children:
                    queue_nxt_lvl.append(child)

            if len(queue_nxt_lvl) == 0:
                continue

            size = len(queue_nxt_lvl)
            output.append(size)

            for node in queue_nxt_lvl:
                queue.enqueue(node)

        return output