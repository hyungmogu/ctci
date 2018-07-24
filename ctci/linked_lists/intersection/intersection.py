# Intersection: Given two Singly linked lists, determine if the two lists intersects.
# Return the inersecting node. Note that the intersection is defined based on reference, not value.
# That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node
# of the second linked list, then they are intersecting

# example

# 1 -> 2 -> 3 --> 4 --> 5
#        /
# b --> a




########################################
#
# ATTEMPT 1
#
########################################


# THIS ATTEMPT IS FAILURE.

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

#     def setNext(node):
#         self.next = node


# class LinkedList:
#     intersectingNode = None

#     def __init__(self, node):
#         self.head = node

#     def add(self, node):
#         current = self.head

#         # if head is null, then return
#         if (current is None): return

#         # trasverse to the end of the linked list
#         while (current.next != None):
#             current = current.next

#         current.next = node

#     @staticmethod
#     def findIntersection(head1, head2):
#         current1 = head1
#         current2 = head2

#         if current1.next != None:
#             LinkedList.findIntersection(current1.next, current2)

#         if current2.next != None:
#             LinkedList.findIntersection(current1, current2.next)

#         if (current1 == current2):
#             LinkedList.intersectingNode = current1
#             print(current1.value)



########################################
#
# ATTEMPT 2
#
########################################


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


    @staticmethod
    def find_intersection(l1, l2):
        output = None

        size1 = l1.get_size()
        size2 = l2.get_size()


        if (size1 == 0 and size2 == 0):
            return output

        step_size = abs(size1 - size2)

        if (size1 > size2):
            current1 = l1.get_ith_node(step_size)
            current2 = l2.head

        elif (size1 < size2):
            current1 = l1.head
            current2 = l2.get_ith_node(step_size)
        
        else:
            current1 = l1.head
            current2 = l2.head

        if (current1 == current2):
            output = current2
            return output

        while current2.next != None:
            if (current1.next == current2.next):
                output = current2.next
                break

            current2 = current2.next
            current1 = current1.next
        
        return output

