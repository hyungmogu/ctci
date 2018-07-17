def getType(matrix):
    output = ''
    matrixSize = len(matrix)

    # check if it's matrix running in horizontal directdion
    for i in range(0, matrixSize):
        if ((type(matrix[i]) is list) and len(matrix[i]) == 1):
            output = '1dimVertical'
            return output
        elif ((type(matrix[i]) is list) and len(matrix[i]) > 0):
            output = 'multi'
            return output

    output = '1dimHoriz'
    return output

def setZeros(matrix, position):
    # deep copy matrix to preserve the origianl
    pos_m = position[0]
    pos_n = position[1]

    # determine the type of matrix
    matrixType = getType(matrix)

    # fill zeros
    if (matrixType == '1dimHoriz'):
        # deep copy matrix to preserve the origianl
        output = [x for x in matrix]

        matrixSize = len(output)
        for i in range(0, matrixSize):
            output[i] = 0

    elif (matrixType == '1dimVertical'):
        # deep copy matrix to preserve the origianl
        output = [x[:] for x in matrix]

        matrixSize = len(output)
        for i in range(0, matrixSize):
            output[i][0] = 0

        print(output)

    elif (matrixType == 'multi'):
        # deep copy matrix to preserve the origianl
        output = [x[:] for x in matrix]

        # figure out the size of the matrix in columnwise direction
        sizeCol = len(output[0])

        # figure out the size of matrix in rowwise direction
        sizeRow = len(output)

        # fill column of the corresponding position with 0
        for i in range(0,sizeCol):
            output[pos_m][i] = 0

        # fill row of the corresponding position with 0
        for i in range(0,sizeRow):
            output[i][pos_n] = 0

    return output