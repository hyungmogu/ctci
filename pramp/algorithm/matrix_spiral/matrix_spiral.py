# goal: given 2d array of integers, create an algorithm that walks over the matrix in a spiral manner in ccw direction. also, generate a list that shows all of the
# traveled elements
#
#
# [[x, 2, 3, 4, 5],
#  [6, 7, 8, 9, 10],
#  [11,12,13,14,15],
#  [16,17,18,19,20]]
#
# [1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12]
#
#
# input: array.array of integers
# output: array of integers

def spiral_copy(inputMatrix):

    output = []

    get_elements(0,0,inputMatrix,output)

    return output

def get_elements(i,j,inputMatrix,output):
    output.append(inputMatrix[j][i])
    inputMatrix[j][i] = 'x'

    if terminating_condition_has_reached(i,j,inputMatrix):
        return

    if can_travel_to_right(i,j,inputMatrix) and not can_travel_to_top(i,j,inputMatrix):
        get_elements(i+1,j,inputMatrix,output)

    if can_travel_to_bottom(i,j,inputMatrix):
        get_elements(i,j+1,inputMatrix,output)

    if can_travel_to_left(i,j,inputMatrix):
        get_elements(i-1,j,inputMatrix,output)

    if can_travel_to_top(i,j,inputMatrix):
        get_elements(i,j-1,inputMatrix,output)

def terminating_condition_has_reached(i,j,inputMatrix):
    if (not can_travel_to_right(i,j,inputMatrix) and
        not can_travel_to_bottom(i,j,inputMatrix) and
        not can_travel_to_left(i,j,inputMatrix) and
        not can_travel_to_top(i,j,inputMatrix)):
        return True
    return False

def can_travel_to_right(i,j,inputMatrix):
    try:
        if (i+1) >= len(inputMatrix[0]) or type(inputMatrix[j][i+1]) != int:
            return False
        return True
    except:
        return False

def can_travel_to_bottom(i,j,inputMatrix):
    try:
        if (j+1) >= len(inputMatrix) or type(inputMatrix[j+1][i]) != int:
            return False
        return True
    except:
        return False

def can_travel_to_left(i,j,inputMatrix):
    try:
        if (i-1) < 0 or type(inputMatrix[j][i-1]) != int:
            return False
        return True
    except:
        return False

def can_travel_to_top(i,j,inputMatrix):
    try:
        if (j-1) < 0 or type(inputMatrix[j-1][i]) != int:
            return False
        return True
    except:
        return False




if __name__ == '__main__':
    output = []
    input_matrix =  [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
    print(spiral_copy(input_matrix))