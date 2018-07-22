def rotateCCW(matrix):
	# Dealing Edge cases
	if (len(matrix) == 0 or len(matrix) == 1):
		return matrix

	# Evaluate the level of depth of the matrix (number of inner matrices) 
	depthTotal = getDepth(matrix);

	# Rotate matrices starting from the outermost level
	for depth in range(0, depthTotal):
		# Harvest elements from the top
		temp = getTopElements(matrix, depth)

		# Rotate elements (ordering is important)
		rotateRight(matrix, depth)
		rotateBottom(matrix, depth)
		rotateLeft(matrix, depth)
		rotateTop(matrix, depth, temp)

	return matrix


def getDepth(matrix):
	output = 0
	n = len(matrix[0])

	if (n % 2 == 0):
		output = n / 2
	else:
		output = (n - 1) / 2

	return output

def getTopElements(matrix, depth):
	n = len(matrix[0])
	e_start = inner_matrix_top_pos = depth
	e_end = n-1-depth

	output = matrix[inner_matrix_top_pos][e_start:e_end+1]

	return output

def rotateRight (matrix, depth):
	n = len(matrix[0])
	e_start = depth
	e_end = inner_matrix_right_pos = n-1-depth
	temp = []

	# Harvest elements from right
	for i in range(e_start, e_end + 1):
		temp.append(matrix[i][inner_matrix_right_pos])

	# Place elements to top
	for i in range (e_start, e_end + 1):
		temp_index = i-e_start
		matrix[depth][i] = temp[temp_index] # i-e_start to position first element on right to first element on top

def rotateBottom (matrix, depth):
	n = len(matrix[0])
	e_start = depth
	e_end = inner_matrix_bottom_pos = inner_matrix_right_pos = n-1-depth

	# Harvest elements from bottom
	temp = matrix[inner_matrix_bottom_pos][e_start:e_end+1]
	temp_size = len(temp)

	# Place elements to right
	for i in range(e_start, e_end + 1):
		temp_index = i-e_start
		matrix[i][inner_matrix_right_pos] = temp[(temp_size-1) - temp_index] # e_end-i to make first element of bottom to be the last element of right


def rotateLeft (matrix, depth):
	n = len(matrix[0])
	e_start = inner_matrix_left_pos = depth
	e_end = inner_matrix_bottom_pos = n-1-depth
	temp = []

	# Harvest elements from left
	for i in range(e_start, e_end + 1):
		temp.append(matrix[i][inner_matrix_left_pos])

	# Place elements to bottom
	for i in range(e_start, e_end + 1):
		temp_index = i-e_start
		matrix[inner_matrix_bottom_pos][i] = temp[temp_index] #i-e_start to position first element on left to first element on bottom

def rotateTop (matrix, depth, temp):
	n = len(matrix[0])
	e_start = inner_matrix_left_pos = depth
	e_end = n-1-depth
	temp_size = len(temp)

	for i in range (e_start, e_end+1):
		temp_index = i-e_start
		matrix[i][inner_matrix_left_pos] = temp[(temp_size-1) - temp_index] #e_end-i to position first element of top to last of bottom



