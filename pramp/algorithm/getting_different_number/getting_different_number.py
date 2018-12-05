# Getting a Different Number
# Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.
#
# Even if your programming language of choice doesn't have that restriction (like Python), assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance, the operation MAX_INT + 1 would be undefined in our case.
#
# Your algorithm should be efficient, both from a time and a space complexity perspectives.
#
# Solve first for the case when you're NOT allowed to modify the input arr. If successful and still have time, see if you can come up with an algorithm with an improved space complexity when modifying arr is allowed. Do so without trading off the time complexity.
#
# Analyze the time and space complexities of your algorithm.
#
# Example:
#
# input:  arr = [0, 1, 2, 3]
#
# output: 4
# Constraints:
#
# [time limit] 5000ms
#
# [input] array.integer arr
#
# 1 <= arr.length <= MAX_INT
# 0 <= arr[i] <= MAX_INT for every i, 0 <= i < MAX_INT
# [output] integer

import sys

# ============== Pramp Mock Interview ====================
def get_different_number_old(arr):

  max_value = max(arr)

  temp_set_integers = set(range(max_value+1))
  temp_set_arr = set(arr)

  diff = temp_set_integers.difference(temp_set_arr)

  if len(diff) > 0:
    output = min(diff)
  else:
    output = max_value + 1

  return output

# ================= Review 2 ======================

def get_different_number(arr):
  temp_set = set(arr)

  i = 0
  biggest_element_in_arr = max(arr)

  while i <= biggest_element_in_arr:
    if i not in temp_set:
      return i
    i += 1
  if biggest_element_in_arr < sys.maxint:
    return biggest_element_in_arr + 1

  return None

# ================= Review 3 ======================

def get_different_number(arr):
    temp_set = set(arr)
    index = 0
    while index < sys.maxint:
        if index not in temp_set:
            return index
        index += 1

    return -1