# Array Quadruplet
# Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn't exist, return an empty array.
#
# Note that there may be more than one quadruplet in arr whose sum is s. You're asked to return the first one you encounter (considering the results are sorted).
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
#                      # (7, 9, 1, 3) and (2, 4, 9, 5), but again you're
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

def find_array_quadruplet_old(arr, s):
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


#============ Review =====================
def find_array_quadruplet(arr, s):

  if len(arr) < 4:
    return []

  temp_arr = sorted(arr)
  i = 0
  j = 1
  r = 2
  l = len(arr) - 1

  while not i_reached_terminating_condition(i,arr):
    while not j_reached_terminating_condition(j,arr):
      while not r_and_l_cross(l,r):
        guess = temp_arr[i] + temp_arr[j] + temp_arr[r] + temp_arr[l]

        if guess == s:
          output = [temp_arr[i], temp_arr[j], temp_arr[r], temp_arr[l]]
          return output

        if guess < s:
          r += 1
        elif guess > s:
          l -= 1

      l = len(arr) - 1
      j += 1
      r = j + 1

    i += 1
    j = i + 1
    r = j + 1

  return []

def r_and_l_cross(l,r):
  if r >= l:
    return True
  return False

def j_reached_terminating_condition(j,arr):
  if j == len(arr) - 2:
    return True
  return False

def i_reached_terminating_condition(i,arr):
  if i == len(arr) - 3:
    return True
  return False

# ===================== review 3 ========================

def find_array_quadruplet(arr, s):

    if len(arr) < 4:
        return []

    i = 0
    j = i + 1
    l = j + 1
    r = len(arr) - 1
    arr = sorted(arr)

    while i < len(arr) - 3:
        while j < len(arr) - 2:
            while l < r:
                temp_sum = arr[i] + arr[j] + arr[l] + arr[r]

                if temp_sum == s:
                    return [arr[i],arr[j],arr[l],arr[r]]

                if temp_sum < s:
                    l += 1
                else:
                    r -= 1

            j += 1
            l = j + 1
            r = len(arr) - 1

        i += 1
        j = i + 1
        l = j + 1
        r = len(arr) - 1
    return []
