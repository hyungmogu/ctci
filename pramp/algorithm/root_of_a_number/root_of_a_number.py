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

  mid = (low + high) / 2.0

  if abs(x - mid**n) < 0.001:
    result['value'] = mid
    return mid

  if mid**n > x:
    get_nth_root(low, mid, x, n, result)
  if mid**n < x:
    get_nth_root(mid, high, x, n, result)


# ================== Review 2 ======================
def root(x,n):
    low = 0
    high = 0
    result = {'value': 0}

    if n == 1 or x == 0:
        return x

    if n == 0 or x == 1:
        return 1

    if x > 0 and x < 1:
        high = 1
    else:
        high = x

    get_nth_root(low,high,x,n,result)
    output = result['value']

    return round(output,3)

def get_nth_root(low,high,solution,n,output):
    mid_point = (low + high) / 2.0

    if terminating_condition_is_reached(mid_point,solution,n):
        output['value'] = mid_point
        return

    if mid_point**n > solution:
        get_nth_root(low,mid_point,solution,n,output)
    else:
        get_nth_root(mid_point,high,solution,n,output)

def terminating_condition_is_reached(mid_point,solution,n):
    if abs(solution - mid_point**n) < 0.001:
        return True
    return False

# =============== Review 5 ===================
def root(x,n):
    output = 0
    lower_bnd = 0
    upper_bnd = 0

    if x == 0 or x == 1:
        return x

    if x < 1:
        lower_bnd = x
        upper_bnd = 1
    else:
        lower_bnd = 1
        upper_bnd = x

    output = _root(x,n,lower_bnd,upper_bnd)

    return round(output,3)

def _root(x,n,lower_bnd,upper_bnd):
    middle_point = (lower_bnd + upper_bnd) / 2.0

    if abs(middle_point**n - x) < 0.001:
        output = middle_point
        return output

    if middle_point**n >  x:
        output = _root(x,n,lower_bnd,middle_point)
    else:
        output = _root(x,n,middle_point, upper_bnd)

    return output


if __name__ == '__main__':
  print(root(27,3))


