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
        # -- Directions
        # Given a linked list, return true if the list
        # is circular, false if it is not
        #
        #
        #     -------------
        #     |           |
        #     v           ^
        # 1-->2-->3-->4-->5
        #
        #
        # constraint
        #   - None
        #
        # Input
        #  - None
        # Output
        #  - Boolean (True if circular node exists / False if not)
        #
        #
        # node1 = Node(1)
        # node2 = Node(2)
        # node3 = Node(3)
        # node4 = Node(4)
        # node5 = Node(5)
        # node1.next = node2
        # node2.next = node3
        # node3.next = node4
        # node4.next = node5
        # node5.next = node2
        #
        # ll = LinkedList(node1)
        # ll.is_cirular() --> True
        #
        #     -------------
        #     |           |
        #     v           ^
        # 1-->2-->3-->4-->5
        #
        #
        #     -------------
        #     |           |
        #     v           ^
        #     *
        # 1-->2-->3-->4-->5
        # ~
        #
        #     -------------
        #     |           |
        #     v           ^
        #         *
        # 1-->2-->3-->4-->5
        #     ~
        #
        #
        #     -------------
        #     |           |
        #     v           ^
        #                 *
        # 1-->2-->3-->4-->5
        #         ~
        #
        #     -------------
        #     |           |
        #     v           ^
        #         *
        # 1-->2-->3-->4-->5
        #             ~
        #
        #     -------------
        #     |           |
        #     v           ^
        #                 *
        # 1-->2-->3-->4-->5
        #                 ~
        #
        # node1 = Node(1)
        # node2 = Node(2)
        # node3 = Node(3)
        # node4 = Node(4)
        # node5 = Node(5)
        # node1.next = node2
        # node2.next = node3
        # node3.next = node4
        # node4.next = node5
        #
        #
        #
        # *
        # 1-->2-->3-->4-->5
        # ~
        #
        #         *
        # 1-->2-->3-->4-->5
        #     ~
        #
        #                 *
        # 1-->2-->3-->4-->5
        #         ~
        #
        # ll = LinkedList(node1)
        # ll.is_cirular() --> False
        #
        #
        #                 *
        # 1-->2-->3-->4-->5
        #         ~
        #
        #
        #
        # ll = LinkedList()
        # ll.is_circular() --> False
        #

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
