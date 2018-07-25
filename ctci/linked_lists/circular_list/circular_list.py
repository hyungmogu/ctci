class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, node):
        self.head = node

    def add(self, node):
        current = self.head

        if (self.head is None):
            self.head = node
        else:
            while (current.next != None):
                current = current.next

            current.next = node


    def get_size(self):
        output = 0
        current = self.head

        if (current == None):
            return output

        while current != None:
            output += 1
            current = current.next

        return output

    def get_ith_node(self, step_size):
        output = None
        current = self.head

        if (current == None):
            return output

        i = 0
        while i < step_size:
            if current != None:
                current = current.next

            i += 1

        output = current

        return output

    # Brute force method
    # pros - quick, easy and dirty. very brute-force like
    # cons - very hard to clean up afterwards. works only when we know it has circular linkedlist. Limited to small cases as it has O(n) space complexity
    def find_circular_node (self):
        output = None
        current = self.head

        finished = False
        while not finished:
            try:
                current.next.traveled
                finished = True
            except AttributeError:
                current.traveled = True
                current = current.next

        output = current.next
        return output



