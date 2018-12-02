# Root of Number
# Many times, we need to re-implement basic functions without using any standard library functions already implemented. For example, when designing a chip that requires very little memory space.
#
# In this question we'll implement a function root that calculates the n'th root of a number. The function takes a nonnegative number x and a positive integer n, and returns the positive n'th root of x within an error of 0.001 (i.e. suppose the real root is y, then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).
#
# Don't be intimidated by the question. While there are many algorithms to calculate roots that require prior knowledge in numerical analysis (some of them are mentioned here), there is also an elementary method which doesn't require more than guessing-and-checking. Try to think more in terms of the latter.
#
# Make sure your algorithm is efficient, and analyze its time and space complexities.
#
# Examples:
#
# input:  x = 7, n = 3
# output: 1.913
#
# input:  x = 9, n = 2
# output: 3
# Constraints:
#
# [time limit] 5000ms
#
# [input] float x
#
# 0 <= x
# [input] integer n
#
# 0 < n
# [output] float
#
# =========================================================
# goal
#   - nth root of a number
#
# input
#   - x >= 0
#   - n > 0
#
# output
#   - float
#
# n = 1
#     |---|---|---|---|---|---|---|---|
# x   0  0.1 0.2 0.5  1   2 . 3   4 . 5
#f(x) 0  0.1 0.2 0.5  1   2   3   4   5
#
# n = 2

#     |----|----|----|----|----|----|----|----|
# x   0   0.1  0.2   0.5   1    2    3    4    5
#f(x) 0   0.1  0.2  0.70   1   1.41 1.73  2    5

#=================================

#
#
#

# case
#   - x == 0
#   - x == 1 or n == 0
#   - x < 1, x > 1

# known
#   - x == 0 --> root(x,n) == 0
#   - x == 1 --> root(x,n) == 1
#   - x > 1 --> root(x,n) < x
#   - x < 1 --> root(x,n) > x
#   - this is a search problem
#     - binary search should be used
output = 0

def root(x,n):
  result = {'value': 0}
  low = 0
  high = 0

  if x == 0:
    return 0

  if x == 1:
    return 1

  if x > 1:
    low = 0
    high = x
  else:
    low = x
    high = 1

  get_nth_root(low, high, x, n, result)
  output = round(result['value'], 3)
  return output

def get_nth_root(low, high, x, n, result):
  # n = 2
  #     |----|----|----|----|----|----|----|----|
  # x   0                   2                   4

  # n = 3
  #     |----|----|----|----|----|----|----|----|
  # x   0.5                0.75   ^   0.875     1
  #
  # cases
  # 1. x < 1
  # 2. x > 1
  #
  # known
  #   - using binary search tree
  #   - travel to the left --> middle_point**n > x
  #   - travel to the right --> middle_point**n < x
  #   - terminating condition --> abs(x - middle_point**n) < 0.001

  mid = (low + high) / 2.0

  if abs(x - mid**n) < 0.001:
    result['value'] = mid
    return mid

  if mid**n > x:
    get_nth_root(low, mid, x, n, result)
  if mid**n < x:
    get_nth_root(mid, high, x, n, result)

if __name__ == '__main__':
  print(root(27,3))


