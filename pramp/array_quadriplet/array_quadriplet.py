# Array Quadruplet
# Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.
#
# Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).
#
# Explain and code the most efficient solution possible, and analyze its time and space complexities.
#
# Example:
#
# input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20
#
# output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
#                      # whose sum is 20. Notice that there
#                      # are two other quadruplets whose sum is 20:
#                      # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
#                      # asked to return the just one quadruplet (in an
#                      # ascending order)
# Constraints:
#
# [time limit] 5000ms
#
# [input] array.integer arr
#
# 1 <= arr.length <= 100
# [input] integer s
#
# [output] array.integer

def find_array_quadruplet(arr, s):
  if len(arr) < 4:
    return []

i = 0
  arr = sorted(arr)
  while (i < len(arr) - 3):
    j = i + 1
    while (j < len(arr) - 2):
      l = j + 1
      r = len(arr)-1
      while (l <r ):
        temp = arr[i] + arr[j]  + arr[l] + arr[r]

        if (temp == s):
          return [arr[i],arr[j],arr[l],arr[r]]

        if temp > s:
          r -= 1
        else:
          l += 1
      j += 1
    i += 1

  return []

