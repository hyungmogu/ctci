# fibonacci number
#   - print out the n-th entry in the fibonacci series.
#     The fibonacci series is an ordering of numbers where
#     each number is the sum of the preecding two.
#
# example
#   - fibonacci_number(0) --> 0
#   - fibonacci_number(1) --> 1
#   - fibonacci_number(2) --> 1 = fibonacci_number(1) + fibonacci_number(0)
#   - fibonacci_number(4) --> 3

import time

def fibonacci_number_old(n):
    if type(n) != int:
        raise TypeError

    if n < 0:
        raise ValueError

    if n == 0 or n == 1:
        return n

    return fibonacci_number_old(n - 1) + fibonacci_number_old(n - 2)

def fibonacci_number(n, memo):
    if type(n) != int:
        raise TypeError

    if n < 0:
        raise ValueError

    if n == 0 or n == 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci_number(n - 1, memo) + fibonacci_number(n - 2, memo)

    return memo[n]

if __name__ == '__main__':
    memo = {}
    start_time1 = time.time()
    print(fibonacci_number(100, memo))
    print(time.time() - start_time1)

    start_time2 = time.time()
    print(fibonacci_number_old(100))
    print(time.time() - start_time2)



