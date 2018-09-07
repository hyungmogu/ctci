#
# nth_root of a number
#
#   implement a root function that calculates nth root of a number. without using built-in function
#
#   known
#     - input number x is positive float
#     - nth root is integer (n >= 0)
#     - output is float
#     - | y - root(x,n) | < 0.001
#     - output should be rounded to three decial degits
#
# 1. x = 4 n =2
# root(x, n) -> 2
#
# 2. x = 7 n = 3
# root(x, n) -> 1.913
#
# 3. x = 0.2 n =2
# root(x, n) -> 0.447
#
# 4. x = 0 n = any
# root(x, n) -> 0
#
# 5. x = 1 n = any
# root(x, n) -> 1
#
# x = any n = 0
# root(x,n) -> 1

def root(x, n):
    output = 0

    if x == 0:
        return 0

    if x == 1:
        return 1

    if n == 0:
        return 1

    if x > 1:
        output = round(get_nth_root(0, x, x, n), 3)
    if x < 1:
        output = round(get_nth_root(0, 1, x, n), 3)

    return output

def get_nth_root(lower_x, upper_x, x, n):
    mid_point = x

    while abs(x - pow(mid_point, n)) >= 0.001:
        mid_point = get_mid_point(lower_x, upper_x)

        if abs(x - pow(mid_point, n)) < 0.001:
            break

        if pow(mid_point, n) > x:
            upper_x = mid_point
        if pow(mid_point, n) < x:
            lower_x = mid_point

    return mid_point

def get_mid_point(lower_x, upper_x):
    return (lower_x + upper_x) / 2.0
