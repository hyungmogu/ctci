# Pancake Sort
# Given an array of integers arr:
#
# Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
# Write a function pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.
# Example:
#
# input:  arr = [1, 5, 4, 3, 2]
#
# output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
# Analyze the time and space complexities of your solution.
#
# Note: it's called pancake sort because it resembles sorting pancakes on a plate with a spatula, where you can only use the spatula to flip some of the top pancakes in the plate. To read more about the problem, see the Pancake Sorting Wikipedia page.
#
# Constraints:
#
# [time limit] 5000ms
#
# [input] array.integer arr
#
# [input] integer k
#
# 0 <= k
# [output] array.integer

import sys

def pancake_sort(arr):

  if len(arr) == 0 or len(arr) == 1:
    return arr

  i = len(arr) - 1

  while not terminating_condition_has_reached(i):

    position_max_e = get_position_max_value_arr(arr,i)
    if position_max_e != i:
      flip(arr,position_max_e+1)
      flip(arr,i+1)

    i -= 1

  return arr

def terminating_condition_has_reached(i):
  if i == 0:
    return True
  return False

def get_position_max_value_arr(arr,i):
  current_best = -sys.maxint
  current_best_index = 0

  for idx in range(i+1):
    if current_best < arr[idx]:
      current_best = arr[idx]
      current_best_index = idx

  return current_best_index

def flip(arr,k):
  for i in range(k/2):
    temp_e = arr[i]
    arr[i] = arr[(k-1) - i]
    arr[(k-1) - i] = temp_e

  return arr


if __name__ == '__main__':
  arr = [2,1]
  print(pancake_sort(arr))