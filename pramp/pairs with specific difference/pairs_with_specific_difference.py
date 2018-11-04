# Pairs with Specific Difference
# Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

# Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

# Examples:

# input:  arr = [0, -1, -2, 2, 1], k = 1
# output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

# input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
# output: []
# Constraints:

# [time limit] 5000ms

# [input] array.integer arr

# 0 <= arr.length <= 100
# [input]integer k

# k >= 0
# [output] array.array.integer

def find_pairs_with_given_difference_brute_force(arr, k):
  output = []

  if len(arr) == 0 or len(arr) == 1:
    return []

  for i in range(len(arr)):
    for j in range(len(arr)):
      if i == j:
        continue

      if (arr[j] - arr[i]) == k:
        output.append([arr[j],arr[i]])

  return output

def find_pairs_with_given_difference_improved(arr, k):
  output = []
  _set = set()

  if len(arr) == 0 or len(arr) == 1:
    return []

  for i in range(len(arr)):
    _set.add(arr[i])

  for i in range(len(arr)):
    arr_j = arr[i] + k

    if arr_j in _set:
      output.append([arr_j, arr[i]])

  return output

