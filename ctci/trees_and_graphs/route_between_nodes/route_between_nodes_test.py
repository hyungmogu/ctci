import unittest
from route_between_nodes import Node, BreadthFirstSearch


class TestRouteBetweenNodes(unittest.TestCase):
	def setUp(self):

		# case where route exists
		self.e0 = Node("a")
		self.e1 = Node(1)
		self.e2 = Node(2)
		self.e3 = Node(3)
		self.e4 = Node("b")

		self.e0.adjacencyList.append(self.e1)
		self.e0.adjacencyList.append(self.e2)
		self.e0.adjacencyList.append(self.e3)

		self.e3.adjacencyList.append(self.e4)

		# case where route doesn't exist
		self.f0 = Node("a")
		self.f1 = Node(1)
		self.f2 = Node(2)
		self.f3 = Node(3)
		self.f4 = Node("b")


		self.f0.adjacencyList.append(self.f1)
		self.f0.adjacencyList.append(self.f2)
		self.f0.adjacencyList.append(self.f3)

	def test_find_route(self):
		self.assertEqual(BreadthFirstSearch.find_route(self.e0, self.e4), True)
		self.assertEqual(BreadthFirstSearch.find_route(self.f0, self.f4), False)



if __name__ == '__main__':
	unittest.main()