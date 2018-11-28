# Merging 2 Packages
# Given a package with a weight limit limit and an array arr of item weights, implement a function getIndicesOfItemWeights that finds two items whose sum of weights equals the weight limit limit. Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j. If such a pair doesn't exist, return an empty array.
#
# Analyze the time and space complexities of your solution.
#
# Example:
#
# input:  arr = [4, 6, 10, 15, 16],  lim = 21
#
# output: [3, 1] # since these are the indices of the
#                # weights 6 and 15 whose sum equals to 21
# Constraints:
#
# [time limit] 5000ms
#
# [input] array.integer arr
#
# 0 <= arr.length <= 100
# [input] integer limit
#
# [output] array.integer


def get_indices_of_item_wights_old(arr, limit):

  if len(arr) == 0 or len(arr) == 1:
    return []

  temp_dict = get_temp_dict(arr)

  for idx_i,arr_i in enumerate(arr):
    arr_j = limit - arr_i

    if arr_j in temp_dict:
      current_best = -1
      for idx_j in temp_dict[arr_j]:
        if idx_i > idx_j :
          current_best = idx_j

      if current_best > -1:
        return [idx_i, current_best]
  return []

def get_temp_dict_old(arr):
  output = {}

  for idx, element in enumerate(arr):
    if not element in output:

      output[element] = [idx]
    else:
      output[element].append(idx) # {4: [0,1]}
  return output


#===================== Review 2 =====================

def get_indices_of_item_wights(arr, limit):

  if len(arr) == 0 or len(arr) == 1:
    return []

  temp_dict = get_maps(arr)

  for idx_i, arr_i in enumerate(arr):
    arr_j = limit - arr_i

    if arr_j in temp_dict:

      current_best = -1
      for idx_j in temp_dict[arr_j]:
        if idx_i > idx_j:
          current_best = idx_j

      if current_best > -1:
        return [idx_i, current_best]

  return []

def get_maps(arr):
  output = {}
  for idx, element in enumerate(arr):
    if element in output:
      output[element].append(idx)
    else:
      output[element] = [idx]

  return output

if __name__ == '__main__':
  arr = [4,4]
  limit = 8
  print(get_indices_of_item_wights(arr, limit))