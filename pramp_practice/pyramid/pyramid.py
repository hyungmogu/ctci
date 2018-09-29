
# constraints
#  - the number of spaces, representing maximum number of # should be preserved at all levels

# example1
#  print_pyramid('') --> TypeError
#  print_pyramid(0) --> ValueError
#  print_pyramid(-1) --> ValueError
#  print_pyramid(1) -->  '#'
#  print_pyramid(2) --> ' # '
#                       '###'
#  print_pyramid(3) --> '  #  '
#                       ' ### '
#                       '#####'


def print_pyramid(steps):

    if type(steps) != int:
        raise TypeError

    if steps <= 0:
        raise ValueError

    output = get_pyramid(steps)

    for step in output:
        print(step)


def get_pyramid(numSteps):
    output = []
    totalNumHashTag = 2*(numSteps - 1) + 1

    for stepIndx in range(numSteps):
        step = ''
        numHashtag = 2*(stepIndx) + 1
        numSpaces = totalNumHashTag - numHashtag

        # generate spaces on left hand side
        for lspace in range(numSpaces/2):
            step += ' '

        # generate hash tags
        for hashTag in range(numHashtag):
            step += '#'

        # generate spaces on right hand side
        for rspace in range(numSpaces/2):
            step += ' '

        output.append(step)

    return output


if __name__ == '__main__':
    print_pyramid(4)
    print_pyramid(3)