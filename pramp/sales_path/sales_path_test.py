import unittest
import sales_path as s

class TestGetCheapestCost(unittest.TestCase):
    def setUp(self):
        self.rootNode = s.Node(0)

        node1 = s.Node(5)
        node2 = s.Node(3)
        node3 = s.Node(6)

        self.rootNode.children = [node1,node2,node3]

        node4 = s.Node(4)
        node5 = s.Node(2)
        node6 = s.Node(0)
        node7 = s.Node(1)
        node8 = s.Node(5)

        node1.children = [node4]
        node2.children = [node5, node6]
        node3.children = [node7, node8]

        node9 = s.Node(1)
        node10 = s.Node(10)

        node5.children = [node9]
        node6.children = [node10]

        node11 = s.Node(1)

        node9.children = [node11]

    def test_return_minimal_sales_path(self):
        expected = 7
        result = s.get_cheapest_cost(self.rootNode)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()