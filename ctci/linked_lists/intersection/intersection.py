# Intersection: Given two Singly linked lists, determine if the two lists intersects.
# Return the inersecting node. Note that the intersection is defined based on reference, not value.
# That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node
# of the second linked list, then they are intersecting

# example

# 1 -> 2 -> 3 --> 4 --> 5
#        /
# b --> a


# THIS ATTEMPT IS FAILURE.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def setNext(node):
        self.next = node


class LinkedList:
    intersectingNode = None

    def __init__(self, node):
        self.head = node

    def add(self, node):
        current = self.head

        # if head is null, then return
        if (current is None): return

        # trasverse to the end of the linked list
        while (current.next != None):
            current = current.next

        current.next = node

    @staticmethod
    def findIntersection(head1, head2):
        current1 = head1
        current2 = head2

        if current1.next != None:
            LinkedList.findIntersection(current1.next, current2)

        if current2.next != None:
            LinkedList.findIntersection(current1, current2.next)

        if (current1 == current2):
            LinkedList.intersectingNode = current1
            print(current1.value)


