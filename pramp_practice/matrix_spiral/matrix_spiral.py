# matrix spiral
#
# write a function that acceps integer N and returns N X N spiral matrix
#
# Example
# matrix_spiral(1) --> [[1]]
# matrix_spiral(2) --> [[1,2],[4,3]]
# matrix_spiral(3) --> [[1,2,3],[8,9,4],[7,6,5]]
# matrix_spiral(0) --> ValueError
# matrix_spiral('') --> TypeError

def matrix_spiral(n):

    if type(n) != int:
        raise TypeError

    if n <= 0:
        raise ValueError

    if n == 1:
        return [[1]]

    # generate N x N list
    matrix = [ [0 for x in range(n)] for x in range(n)]
    coordinate = [0,0]
    index = 1

    # initialize
    matrix[0][0] = index
    index += 1

    # travel until all elements in the matrix are filled (there are no places for the pointer to go)
    while (can_still_travel(coordinate, matrix, n)):
        # travel to the right
        newIndex = travel_to_the_right(coordinate, matrix, n, index)
        newIndex = travel_to_the_bottom(coordinate, matrix, n, newIndex)
        newIndex = travel_to_the_left(coordinate, matrix, n, newIndex)
        newIndex = travel_to_the_top(coordinate, matrix, n, newIndex)
        index = newIndex
    return matrix

def can_still_travel(coord, matrix, n):
    # cannot travel if all direction is blocked off

    if (not can_still_travel_right(coord, matrix, n) and
        not can_still_travel_bottom(coord, matrix, n) and
        not can_still_travel_left(coord, matrix, n) and
        not can_still_travel_top(coord, matrix, n)):
        return False
    return True

def can_still_travel_right(coord, matrix, n):
    if (coord[1] + 1 >= n) or (matrix[coord[0]][coord[1] + 1] != 0):
        return False
    return True

def can_still_travel_bottom(coord, matrix, n):
    if (coord[0] + 1 >= n) or (matrix[coord[0] + 1][coord[1]] != 0):
        return False
    return True

def can_still_travel_left(coord, matrix, n):
    if (coord[1] - 1 < 0) or (matrix[coord[0]][coord[1] - 1] != 0):
        return False
    return True

def can_still_travel_top(coord, matrix, n):
    if (coord[0] - 1 < 0) or (matrix[coord[0] - 1][coord[1]] != 0):
        return False
    return True

def travel_to_the_right(coord, matrix, n, index):
    while can_still_travel_right(coord, matrix, n):
        coord[1] += 1
        matrix[coord[0]][coord[1]] = index
        index += 1
    return index


def travel_to_the_bottom(coord, matrix, n, index):
    while can_still_travel_bottom(coord, matrix, n):
        coord[0] += 1
        matrix[coord[0]][coord[1]] = index
        index += 1
    return index

def travel_to_the_left(coord, matrix, n, index):
    while can_still_travel_left(coord, matrix, n):
        coord[1] -= 1
        matrix[coord[0]][coord[1]] = index
        index += 1
    return index

def travel_to_the_top(coord, matrix, n, index):
    while can_still_travel_top(coord, matrix, n):
        coord[0] -= 1
        matrix[coord[0]][coord[1]] = index
        index += 1
    return index

