class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.visited = False
		self.leftChild = None
		self.rightChild = None


class BreadthFirstSearch:
	@staticmethod
	def list_of_depth(startNode):
		output = []
		queue = []
		adjacencyList = []

		if (startNode is None):
			return output

		queue.append(startNode)
		output.append(startNode)

		while queue:			
			current = queue.pop(0)


			# adding child of each node to adjacency list
			if (current.visited is not True):
				current.visited = True

				if (current.leftChild != None):
					adjacencyList.append(current.leftChild) 
				if (current.rightChild != None):
					adjacencyList.append(current.rightChild)

			if (len(queue) == 0 and len(adjacencyList) > 0): 

				# form link list when reaching the end of depth D 
				for i in range(0,len(adjacencyList)):
					try:
						adjacencyList[i].next = adjacencyList[i+1]
					except Exception:
						pass
				output.append(adjacencyList[0])


				for i in range(0, len(adjacencyList)):
					queue.append(adjacencyList[i])

				adjacencyList = []

		return output
