class Node:
  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None

# return min(arr)
def get_cheapest_cost(rootNode):
  arr = []

  output = get_cheapest_cost_helper(rootNode,arr,0)

  return min(arr)  # your code goes here

def get_cheapest_cost_helper(node,arr,count):
  count = count + node.cost

  if terminating_condition_has_reached(node):
    arr.append(count)
    return

  for child_node in node.children:
    get_cheapest_cost_helper(child_node,arr,count)

def terminating_condition_has_reached(node):
  if len(node.children) == 0:
    return True
  return False

