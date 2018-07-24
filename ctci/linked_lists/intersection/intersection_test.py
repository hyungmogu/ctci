import unittest
from intersection import Node, LinkedList

class TestIntersection(unittest.TestCase):
    def setUp(self):
        nodes = [Node("a"), Node("b"), Node("c")]

        h1 = Node(1)
        h2 = Node(2)

        self.l1 = LinkedList(h1)
        self.l2 = LinkedList(h2) 

        for i in range(0,3):
            self.l1.add(nodes[i])

        self.l2.add(nodes[0])

    def test_get_ith_node(self):
        current_node1 = self.l1.get_ith_node(0)
        current_node2 = self.l1.get_ith_node(1)
        current_node3 = self.l1.get_ith_node(2)
        
        self.assertEqual(current_node1.value, 1)
        self.assertEqual(current_node2.value, "a")
        self.assertEqual(current_node3.value, "b")

    def test_get_size(self):
        self.assertEqual(self.l1.get_size(), 4)
        self.assertEqual(self.l2.get_size(), 4)


    def test_linkedList(self):
        nodes = ["a", "b", "c"]

        self.assertEqual(self.l1.head.value, 1)
        self.assertEqual(self.l2.head.value, 2)

        current1 = self.l1.head.next
        current2 = self.l2.head.next

        i = 0
        while (current1.next != None):
            self.assertEqual(current1.value, nodes[i])
            current1 = current1.next
            i += 1

        j = 0
        while (current2.next != None):
            self.assertEqual(current2.value, nodes[j])
            current2 = current2.next
            j += 1

    def test_intersection(self):
        intersecting_node = LinkedList.find_intersection(self.l1, self.l2)
        self.assertEqual(intersecting_node.value, "a")


if __name__ == "__main__":
    unittest.main()