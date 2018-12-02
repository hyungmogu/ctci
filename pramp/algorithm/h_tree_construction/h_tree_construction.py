# H-Tree Construction
# An H-tree is a geometric shape that consists of a repeating pattern resembles the letter “H”.

# It can be constructed by starting with a line segment of arbitrary length, drawing two segments of the same length at right angles to the first through its endpoints, and continuing in the same vein, reducing (dividing) the length of the line segments drawn at each stage by √2.

# Here are some examples of H-trees at different levels of depth:

# alt depth = 1

# alt depth = 2

# alt depth = 3

# Write a function drawHTree that constructs an H-tree, given its center (x and y coordinates), a starting length, and depth. Assume that the starting line is parallel to the X-axis.

# Use the function drawLine provided to implement your algorithm. In a production code, a drawLine function would render a real line between two points. However, this is not a real production environment, so to make things easier, implement drawLine such that it simply prints its arguments (the print format is left to your discretion).

# Analyze the time and space complexity of your algorithm. In your analysis, assume that drawLine's time and space complexities are constant, i.e. O(1).

# Constraints:

# [time limit] 5000ms

# [input] double x

# [input] double y

# [input] double length

# [input] double depth

def drawHTree_(x_c,y_c,length,depth):

  current_depth = 1

  drawHTreeHelper(x_c,y_c,length,depth,current_depth)

def drawHTreeHelper(x_c,y_c,length,depth, cureent_depth):

  if depth < current_depth:
    return

  drawLine((x_c - length/2.0, y_c), (x_c + length/2.0, y_c)) # drawing horizontal line
  drawLine((x_c - length/2.0, y_c - length/2.0), (x_c - length/2.0, y_c + length/2.0)) # vertical bar on left
  drawLine((x_c + length/2.0, y_c - length/2.0), (x_c + length/2.0, y_c + length/2.0)) # vertical bar on right

  drawHTreeHelper (x_c - length/2.0, y_c + length/2.0, updateLength(length),depth,cureent_depth+1)
  drawHTreeHelper (x_c - length/2.0, y_c - length/2.0,updateLength(length),depth,cureent_depth+1 )
  drawHTreeHelper (x_c + length/2.0, y_c - length/2.0, updateLength(length),depth,cureent_depth+1 )
  drawHTreeHelper (x_c + length/2.0, y_c + length/2.0, updateLength(length),depth,cureent_depth+1)

def updateLength(length):
  return length / float(sqrt(length))

# ================ Review 2 =====================

def printHTree(x,y,length,current_depth,depth):
  if terminating_condition_has_reached(current_depth,depth):
    return

  hrzt_left_pt_x = x - (length / 2.0)
  hrzt_left_pt_y = y

  hrzt_right_pt_x = x + (length / 2.0)
  hrzt_right_pt_y = y

  drawLine(hrzt_left_pt_x,hrzt_left_pt_y,hrzt_right_pt_x,hrzt_right_pt_y)

  # 2.2 draw left vertical line
  vert_left_top_pt_x =  x - (length / 2.0)
  vert_left_top_pt_y = y + (length / 2.0)

  vert_left_bottom_pt_x = x - (length / 2.0)
  vert_left_bottom_pt_y = y - (length / 2.0)

  drawLine(vert_left_top_pt_x,vert_left_top_pt_y,vert_left_bottom_pt_x,vert_left_bottom_pt_y)

  # 2.3 draw right vertical line
  vert_right_top_pt_x =  x + (length / 2.0)
  vert_right_top_pt_y = y + (length / 2.0)

  vert_right_bottom_pt_x = x + (length / 2.0)
  vert_right_bottom_pt_y = y - (length / 2.0)

  drawLine(vert_right_top_pt_x,vert_right_top_pt_y,vert_right_bottom_pt_x,vert_right_bottom_pt_y)

  # 3. if currentDepth < depth / terminating condition is not satisfied, then perform recursion on each endpoint of H of current depth
  updated_length = length**(1/2.0)
  updated_depth = current_depth + 1
  printHTree(vert_right_top_pt_x,vert_right_top_pt_y,updated_length,updated_depth,depth)
  printHTree(vert_left_top_pt_x,vert_left_top_pt_y,updated_length,updated_depth,depth)
  printHTree(vert_right_bottom_pt_x,vert_right_bottom_pt_y,updated_length,updated_depth,depth)
  printHTree(vert_left_bottom_pt_x,vert_left_bottom_pt_y,updated_length,updated_depth,depth)

def terminating_condition_has_reached(current_depth,depth):
  if current_depth > depth:
    return True
  return False

def drawHTree(x,y,length,depth):
  if depth == 0:
    return

  currentDepth = 1

  printHTree(x,y,length,current_depth,depth)
