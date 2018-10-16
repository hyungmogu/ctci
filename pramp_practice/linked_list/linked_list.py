class Node:
    def __init__(self, e):
        self.data = e
        self.next = None

# Linked List
#
# - complete the following methods for linked list (11 methods)
#   - insert_first
#   - insert_at
#   - insert_last
#   - size
#   - get_at
#   - get_first
#   - get_last
#   - remove_at
#   - remove_first
#   - rmove_last
#   - clear

# ll = LinkedList() --> {}
# insert 1 --> {1}
# insert 2 --> {2}->{1}
# insert 3 --> {3}->{2}->{1}

class LinkedList:
    def __init__(self, e = None):
        self.head = e

    def insert_first(self, value):
        # insert_first
        #     -   Inserts element to the first position
        #         of linked list

        #     -   Example
        #         ll = LinkedList() --> {}
        #         ll.insert_first(1) --> {1}
        #         ll.insert_first(2) --> {2}->{1}

        node = Node(value)

        if self.head == None:
            self.head = node
            return

        node.next = self.head
        self.head = node

    def size(self):
        # -   returns the size of linked list

        #     -   Example
        #         ll = LinkedList()
        #         ll.insert_first(2)
        #         ll.insert_first(1) {1}->{2}
        #         ll.size() --> 2

        #         ll = LinkedList()
        #         ll.insert_first(1)
        #         ll.size() --> 1

        #         ll = LinkedList()
        #         ll.size() --> 0
        count = 0
        current_node = self.head

        if self.head == None:
            return 0

        while current_node != None:
            count += 1
            current_node = current_node.next

        return count

    def insert_at(self, position, value):
        # insert_at
        #     -   Inserts element to nth position
        #         in linked list

        #     -   Example
        #         ll = LinkedList()
        #         ll.insert_first(1) {1}
        #         ll.insert_first(2) {2}->{1}
        #         ll.insert_first(3) {3}->{2}->{1}
        #         ll.insert_at(2, 4) --> {3}[0]->{2}[1]->{4}[2]->{1}[3]

        #         ll.insert_at(0,'hello') --> {'hello'}->{3}->{2}->{4}->{1}

        #         ll.insert_at(4, 'hi!') --> IndexError

        #         ll = LinkedList() -> {}
        #         ll.insert_at(2, 1) -> IndexError!

        #         ll = LinkedList()
        #         ll.insert_at(-1, 'another value') -> ValueError

        #         ll  = LinkedList()
        #         ll.insert_at('hello world', 10) --> TypeError
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
        # insert_last
        # -   Inserts element to the end of Linked List

        # -   Example
        #     ll = LinkedList()
        #     ll.insert_first(5)
        #     ll.insert_first(4)
        #     ll.insert_first(3)
        #     ll.insert_first(2)
        #     ll.insert_first(1) {1}->{2}->{3}->{4}->{5}
        #     ll.insert_last(6) {1}->{2}->{3}->{4}->{5}->{6}

        #     ll = LinkedList()
        #     ll.insert_last(1) {1}

        node = Node(e)
        current_node = self.head

        if self.head == None:
            self.head = node
            return

        while current_node.next != None:
            current_node = current_node.next

        current_node.next = node

    def get_at(self, position):
        # -   returns nth node in linked list

        #         -   Example
        #             ll = LinkedList()
        #             ll.insert_first(5)
        #             ll.insert_first(4)
        #             ll.insert_first(3)
        #             ll.insert_first(2)
        #             ll.insert_first(1) {1}[0]->{2}->{3}[2]->{4}->{5}[4]
        #             ll.get_at(2) --> {3}

        #             ll = LinkedList()
        #             ll.insert_first(1)
        #             ll.get_at(0) -> {1}

        #             ll.get_at(5) --> IndexError

        #             ll.get_at(-1) --> IndexError

        #             ll.get_at('hello') --> TypeError

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
        # -   get the first node in linked list

        #         ll = LinkedList()
        #         ll.insert_first(5)
        #         ll.insert_first(4)
        #         ll.insert_first(3)
        #         ll.insert_first(2)
        #         ll.insert_first(1) --> {1}->{2}->{3}->{4}->{5}
        #         ll.get_first() --> {1}

        #         ll = LinkedList()
        #         ll.get_first() --> IndexError

        return self.get_at(0)


    def get_last(self):
        # - get the last node in linked list

        #     ll = LinkedList()
        #     ll.insert_first(5)
        #     ll.insert_first(4)
        #     ll.insert_first(3)
        #     ll.insert_first(2)
        #     ll.insert_first(1) --> {1}->{2}->{3}->{4}->{5}
        #     ll.get_last() --> {5}

        #     ll = LinkedList()
        #     ll.insert_first(1) -> {1}
        #     ll.get_last() --> {1}

        #     ll = LinkedList()
        #     ll.get_last() --> IndexError

        size = self.size()
        return self.get_at(size - 1)


    def remove_at(self, position):
        # -   removes nth node from linked list

        # -   Example
        #     ll = LinkedList()
        #     ll.insert_first(5)
        #     ll.insert_first(4)
        #     ll.insert_first(3)
        #     ll.insert_first(2)
        #     ll.insert_first(1) {1}->{2}->{3}[2]->{4}->{5}
        #     ll.remove_at(2) --> self.head --> {1}->{2}->{4}->{5}
        #     ll.remove_at(0) --> {2}->{4}->{5}

        #     ll = LinkedList()
        #     ll.insert_first(1)
        #     ll.remove_at(0)

        #     ll = LinkedList()
        #     ll.insert_first(5)
        #     ll.insert_first(4)
        #     ll.insert_first(3)
        #     ll.insert_first(2)
        #     ll.insert_first(1)
        #     ll.remove_at(5) --> IndexError
        #     ll.remove_at(-1) --> IndexError

        #     ll.remove_at('hello') --> TypeError
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
        # - removes the first node from linked list

        #     ll = LinkedList()
        #     ll.insert_first(5)
        #     ll.insert_first(4)
        #     ll.insert_first(3)
        #     ll.insert_first(2)
        #     ll.insert_first(1)
        #     ll.remove_last() --> self.head --> {1}->{2}->{3}->{4}
        self.remove_at(0)


    def remove_last(self):
        # -   removes last node from linked list

        #     ll = LinkedList()
        #     ll.insert_first(5)
        #     ll.insert_first(4)
        #     ll.insert_first(3)
        #     ll.insert_first(2)
        #     ll.insert_first(1)
        #     ll.remove_last() --> self.head --> {1}->{2}->{3}->{4}

        size = self.size()
        self.remove_at(size - 1)

    def clear(self):
        # -   clears current linked list chain

        # -   Example

        #     ll = LinkedList()
        #     ll.insert_first(5)
        #     ll.insert_first(4)
        #     ll.insert_first(3)
        #     ll.insert_first(2)
        #     ll.insert_first(1)
        #     ll.clear() --> self.head --> None
        self.head = None



















