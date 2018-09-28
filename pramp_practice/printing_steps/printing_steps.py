# printing steps
#
# Write a function that accepts a positive number N.
# The function should console log a step shape with N levels using the '#' character.
# Make sure the step has spaces on the right hand side.

# print_steps(1) --> '#  '
# print_steps(3) --> '#  '
#                    '## '
#                    '###'
# ['#', '##', '###']

# print_steps(0) --> ValueError
# print_steps('') --> TypeError


def print_steps(steps):

    if type(steps) != int:
        raise TypeError

    if steps == 0:
        raise ValueError

    output = get_steps(steps)

    for step in output:
        print('{0}'.format(step))


def get_steps(steps):
    output = []

    for idx in range(steps):
        step = ''
        for idx_shap in range(idx+1):
            step += '#'

        for idx_shape in range(idx, steps):
            step += ' '

        output.append(step)

    return output

if __name__ == "__main__":
    print_steps(3)
