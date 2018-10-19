# From Last
#
# Given a linked list and integer n, return the element n
# spaces from the last node in the list. Do not call the
# 'Size' method of the linked list. Assume that n will always
# be less than the length of the list.

class Node:
    def __init__(self, e):
        self.data = e
        self.next = None

class LinkedList:
    def __init__(self, e = None):
        self.head = e

    def insert_first(self, value):
        node = Node(value)

        if self.head == None:
            self.head = node
            return

        node.next = self.head
        self.head = node

    def size(self):
        count = 0
        current_node = self.head

        if self.head == None:
            return 0

        while current_node != None:
            count += 1
            current_node = current_node.next

        return count

    def insert_at(self, position, value):
            size = self.size()
            node = Node(value)
            current_index = 0
            current_node = self.head

            if type(position) != int:
                raise TypeError

            if position < 0:
                raise IndexError

            if position >= size:
                raise IndexError

            if position == 0:
                node.next = self.head
                self.head = node
                return

            while current_index < position - 1:
                current_node = current_node.next
                current_index += 1

            node.next = current_node.next
            current_node.next = node


    def insert_last(self, e):
        node = Node(e)
        current_node = self.head

        if self.head == None:
            self.head = node
            return

        while current_node.next != None:
            current_node = current_node.next

        current_node.next = node

    def get_at(self, position):
        size = self.size()
        current_index = 0
        current_node = self.head

        if type(position) != int:
            raise TypeError

        if position < 0 or position >= size:
            raise IndexError

        if position == 0:
            return self.head

        while current_index < position - 1:
            current_node = current_node.next
            current_index += 1

        return current_node.next

    def get_first(self):
        return self.get_at(0)

    def get_last(self):
        size = self.size()
        return self.get_at(size - 1)

    def remove_at(self, position):
        size = self.size()
        current_node = self.head
        current_index = 0

        if type(position) != int:
            raise TypeError

        if position < 0 or position >= size:
            raise IndexError

        if position == 0:
            self.head = self.head.next
            return

        while current_index < position - 1:
            current_node = current_node.next
            current_index += 1

        current_node.next = current_node.next.next

    def remove_first(self):
        self.remove_at(0)


    def remove_last(self):
        size = self.size()
        self.remove_at(size - 1)

    def clear(self):
        self.head = None

    def get_mid_point(self):

        runner = self.head
        walker = self.head

        if self.head == None:
            return None

        if self.head.next == None:
            return self.head

        while runner.next is not None and runner.next.next is not None:
            runner = runner.next.next
            walker = walker.next

        return walker

    def is_circular(self):
        runner = self.head
        walker = self.head

        if self.head == None:
            return False

        if runner.next == None or runner.next.next == None:
            return False

        runner = runner.next.next
        walker = walker.next

        while runner != walker:
            if runner.next == None or runner.next.next == None:
                return False
            runner = runner.next.next
            walker = walker.next

        return True

    def from_last(self, n):
        # Given a linked list and integer n, return the element n
        # spaces from the last node in the list. Do not call the
        # 'size' method of the linked list. Assume that n will always
        # be less than the length of the list.
        #
        #
        # 1-->2-->3-->4-->5
        # 4   3   2   1   0
        #
        # constraint
        #  - 'size' method cannot be called
        #  - n will always be less than the length of the list
        #
        # input
        #  - integer n
        # output
        #  - ith node from last
        #
        # -- Examples
        # const list = new LinkedList()
        # list.insert_first(5)
        # list.insert_first(4)
        # list.insert_first(3)
        # list.insert_first(2)            2    1    0
        # list.insert_first(1) {1}->{2}->{3}->{4}->{5}
        # list.from_last(2) --> 3
        # list.from_last(0) --> 5
        # list.from_last(4) --> 1
        # list.from_last(-10) --> IndexError
        # list.from_last(10) --> IndexError
        #
        # ~
        # 1-->2-->3-->4-->5
        # *
        #
        # 1-->2-->3-->4-->5
        #         *
        #
        # const list = new LinkedList()
        # list.insert_first(1)
        # list.from_last(0) --> 1 otherwise return index error
        #
        #
        # const list = new LinkedList()
        # list.from_last(-1) --> IndexError
        #
        # const list = new LinkedList()
        # list.from_last('hello world') --> TypeError

        runner = self.head
        walker = self.head

        if type(n) != int:
            raise TypeError

        if n < 0:
            raise IndexError

        if self.head == None:
            raise IndexError

        if self.head.next == None and (n != 0):
            raise IndexError

        if self.head.next == None:
            return self.head

        i = 0
        while i < n:
            if runner.next == None:
                raise IndexError
            runner = runner.next
            i += 1


        while runner.next != None:
            runner = runner.next
            walker = walker.next

        return walker





