# Array of Array Products
# Given an array of integers arr, you're asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.
#
# Solve without using division and analyze your solution's time and space complexities.
#
# Examples:
#
# input:  arr = [8, 10, 2]
# output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]
#
# input:  arr = [2, 7, 3, 4]
# output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]
# Constraints:
#
# [time limit] 5000ms
#
# [input] array.integer arr
#
# 0 <= arr.length <= 20
# [output] array.integer

def array_of_array_products(arr):

  if len(arr) == 0 or len(arr) == 1:
    return []

  temp_value = 1
  ans = []
  for element in arr:
    ans.append(temp_value)
    temp_value *= element

  temp_value = 1
  last_idx = len(arr) - 1
  for idx,element in enumerate(arr[::-1]):
    ans[last_idx - idx] *= temp_value
    temp_value *= element

  return ans

def array_of_array_products_brute_force(arr):
  ans = [1 for x in arr]

  if len(arr) == 0 or len(arr) == 1:
    return []

  for idx_x, arr_x in enumerate(arr):
    for idx_i, arr_i in enumerate(arr):
      if idx_x != idx_i:
        ans[idx_x] *= arr_i

  return ans


if __name__ == '__main__':
  arr = [8, 10, 2]
  print(array_of_array_products(arr))