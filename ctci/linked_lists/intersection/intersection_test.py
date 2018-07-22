import unittest
from intersection import Node, LinkedList

class TestIntersection(unittest.TestCase):
    def setUp(self):
        h1 = Node(1)
        h2 = Node(2)

        nodes = [Node("a"), Node("b"), Node("c")]

        self.l1 = LinkedList(h1)
        self.l2 = LinkedList(h2)

        for i in range(0,3):
            self.l1.add(nodes[i])

        self.l2.add(nodes[0])

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
        LinkedList.findIntersection(self.l1.head, self.l2.head)
        print("The value of intersecting Node is {0}".format(LinkedList.intersectingNode.value))
        self.assertEqual(LinkedList.intersectingNode.value, "a")


if __name__ == "__main__":
    unittest.main()