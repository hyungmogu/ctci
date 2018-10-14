#
#
#
#
#
#
#
#
#

class Node:
    def __init__(self, e):
        self.data = e
        self.next = None

class LinkedList:
    def __init__(self, e = None):
        self.head = e

    def insert_first(self, value):
        node = Node(value)
        # insert node to the first of linked list
        #   - when size is 0
        #   - when size is greater than 0
        if self.head == None:
            self.head = node
            return

        node.next = self.head
        self.head = node
        return

    def size(self):
        output = 1
        current_node = self.head

        if self.head == None:
            output = 0
            return output

        while current_node.next != None:
            output += 1
            current_node = current_node.next

        return output

    def get_at(self, position):
        current_index = 0
        current_node = self.head

        if type(position) != int:
            raise TypeError

        if position < 0:
            raise ValueError

        if position >= self.size():
            raise IndexError

        if self.head == None:
            return None

        if position == 0:
            return current_node

        while current_index < position:
            current_node = current_node.next
            current_index += 1

        return current_node

    def insert_at(self, position, value):
        node = Node(value)
        current_index = 0
        current_node = self.head

        if type(position) != int:
            raise TypeError

        if position < 0:
            raise ValueError

        if position > self.size() - 1:
            raise IndexError

        if position == 0:
            node.next = self.head
            self.head = node
            return

        if position != 1:
            while current_index < position -1:
                current_node = current_node.next
                current_index += 1

        node.next = current_node.next
        current_node.next = node

    def remove_at(self, position):
        current_index = 0
        current_node = self.head
        size = self.size()

        if type(position) != int:
            raise TypeError

        if position < 0:
            raise ValueError

        if current_node == None:
            raise ValueError

        if position > size - 1:
            raise IndexError

        if position == 0:
            node_to_be_deleted = self.head
            self.head = self.head.next
            del node_to_be_deleted
            return

        while current_index < (position - 1):
            current_node = current_node.next
            current_index += 1

        node_to_be_deleted = current_node.next
        current_node.next = current_node.next.next
        del node_to_be_deleted

    def remove_last(self):
        current_index = 0
        current_node = self.head

    def get_first(self):
        size = self.size()

        if size == 0:
            return None

        return self.head

    def get_last(self):
        size = self.size()
        last_index = size - 1

        if self.head == None:
            return None

        return self.get_at(last_index)

    def remove_first(self):
        return self.remove_at(0)

    def remove_last(self):
        size = self.size()
        last_index = size - 1
        return self.remove_at(last_index)

    def insert_last(self, e):
        node = Node(e)
        current_node = self.head
        current_index = 0

        if current_node == None:
            self.head = node
            return

        while current_node.next != None:
            current_node = current_node.next

        current_node.next = node

    def clear(self):
        self.head = None

















