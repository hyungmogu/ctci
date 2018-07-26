class Node:
	def __init__(self, name):
		self.name = name
		self.visited = False
		self.adjacencyList = []
	

class BreadthFirstSearch:
	@staticmethod
	def bfs(self, startNode):
		queue = []
		startNode.visited = True
		queue.append(startNode)

		while queue:
			current = queue.pop(0)

			for n in current.adjacencyList:
				if (n.visited is not True):
					n.visited = True
					queue.append(n)


	@staticmethod
	def find_route(startNode, endNode):
		output = False

		queue = []
		startNode.visitied = True
		queue.append(startNode)

		while queue:
			current = queue.pop(0)

			for n in current.adjacencyList:

				if (n == endNode):
					output = True
					return output

				if (n.visited is not True):
					n.visited = True
					queue.append(n)

		return output