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

# ================ Review 2 ===================

def find_pairs_with_given_difference(arr, k):

  output = []
  temp_set = set(arr)
  for y in arr:
    x = k + y
    if x in temp_set:
      output.append([x,y])

  return output

# ================= Review 3 =====================

def find_pairs_with_given_difference(arr, k):
    output = []
    temp_set = set(arr)

    if len(arr) == 0 or len(arr) == 1:
        return []

    for y in arr:
        x = y + k
        if x in temp_set and x != y:
            output.append([x,y])

    return output


if __name__ == '__main__':
  arr = [1, 7, 5, 3, 32, 17, 12]
  k = 17

  result = find_pairs_with_given_difference(arr, k)
  print(result)
