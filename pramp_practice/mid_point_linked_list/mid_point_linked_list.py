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
        # return the mid point of linked list. If the list
        # has an even number of elements, return the node
        # at the end of the first half of the list.
        # *Do not* use a counter variable, *do not* retrieve
        # the size of the list, and only iterate through the list
        # one time.
        #
        # Input - None
        # Output - None
        #
        # Constraint
        #  - Do not use counter variable (position / index ... any var with int)
        #  - Do not retrieve the size of the list
        #  - Iterate through the list one time
        #
        # ll = l.LinkedList()
        # ll.insert_first(4)
        # ll.insert_first(3)
        # ll.insert_first(2)
        # ll.insert_first(1) {1}->{2}->{3}->{4}
        # ll.get_mid_point() --> 2

        # *
        # 4 3 2 1
        # ~

        #     *
        # 4 3 2 1
        #   ~

        # *
        # 2 1
        # ~

        #     *
        # 6 5 4 3 2 1
        #   ~

        #         *
        # 6 5 4 3 2 1
        #     ~


        # ll = l.LinkedList()
        # ll.insert_first(5)
        # ll.insert_first(4)
        # ll.insert_first(3)
        # ll.insert_first(2)
        # ll.insert_first(1) {1}->{2}->{3}->{4}->{5}
        # ll.get_mid_point() --> {3}

        # *
        # 5 4 3 2 1
        # ~

        #     *
        # 5 4 3 2 1
        #   ~

        #         *
        # 5 4 3 2 1
        #     ~

        # *
        # 7 6 5 4 3 2 1
        # ~

        #     *
        # 7 6 5 4 3 2 1
        #   ~

        #         *
        # 7 6 5 4 3 2 1
        #     ~

        #             *
        # 7 6 5 4 3 2 1
        #       ~



        # ll = l.LinkedList()
        # ll.insert_first(4)
        # ll.get_mid_point() --> 4

        # ll = l.LinkedList()
        # ll.get_mid_point() --> None

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
