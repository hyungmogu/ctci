# Largest Smaller BST Key
# Given a root of a Binary Search Tree (BST) and a number num, implement an efficient function findLargestSmallerKey that finds the largest key in the tree that is smaller than num. If such a number doesn't exist, return -1. Assume that all keys in the tree are nonnegative.
#
# Analyze the time and space complexities of your solution.
#
# For example:
#
# For num = 17 and the binary search tree below:
#
# alt
#
# Your function would return:
#
# 14 since it's the largest key in the tree that is still smaller than 17.
#
# Constraints:
#
# [time limit] 5000ms
# [input] Node rootNode
# [output] integer
#
#          20
#         /   \
#       9      25
#     /   \
#    5      12
#          /  \
#       11     14
#

##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
# 2) Use the helper code below to implement it.          #
# 3) In a nutshell, the helper code allows you to        #
#    to build a Binary Search Tree.                      #
# 4) Jump to line 71 to see an example for how the       #
#    helper code is used to test findLargestSmallerKey.  #
##########################################################


# A node
class Node:

# Constructor to create a new node
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.parent = None

# A binary search tree
class BinarySearchTree:

  # Constructor to create a new BST
  def __init__(self):
    self.root = None

  def get_elements_in_order(self,node,output):

    if node == None:
      return

    self.get_elements_in_order(node.left, output)
    output.append(node)
    self.get_elements_in_order(node.right,output)


  # 2. walk over each element in array
  def find_largest_smaller_key(self, num):

    temp_arr = []

    self.get_elements_in_order(self.root,temp_arr)

    if num <= temp_arr[0].key:
      return -1

    for idx,element in enumerate(temp_arr):
      if self.is_solution(temp_arr,idx,num):
        return element.key

    return -1

  def is_solution(self,temp_arr,idx,num):
    try:
      if temp_arr[idx+1].key >= num:
        return True
      return False
    except:
      return True

  def find_largest_smaller_key_improved(self, num):

    current_best = -1
    node = self.root
    while node != None:
      if self.is_solution(node,num):
        current_best = node.key
        node = node.right
      else:
        node = node.left

    return current_best

  def is_solution_improved(self,node,num):
    if node.key < num:
      return True
    else:
      return False

  # Given a binary search tree and a number, inserts a
  # new node with the given number in the correct place
  # in the tree. Returns the new root pointer which the
  # caller should then use(the standard trick to avoid
  # using reference parameters)
  def insert(self, key):

      # 1) If tree is empty, create the root
      if (self.root is None):
          self.root = Node(key)
          return

      # 2) Otherwise, create a node with the key
      #    and traverse down the tree to find where to
      #    to insert the new node
      currentNode = self.root
      newNode = Node(key)

      while(currentNode is not None):
        if(key < currentNode.key):
          if(currentNode.left is None):
            currentNode.left = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.left
        else:
          if(currentNode.right is None):
            currentNode.right = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.right

#########################################
# Driver program to test above function #
#########################################

bst  = BinarySearchTree()

# Create the tree given in the above diagram
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)

result = bst.find_largest_smaller_key(30)

print ("Largest smaller number is %d " %(result))
