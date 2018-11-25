# Smallest Substring of All Characters
# Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn't exist.
#
# Come up with an asymptotically optimal solution and analyze the time and space complexities.
#
# Example:
#
# input:  arr = ['x','y','z'], str = "xyyzyzyx"
#
# output: "zyx"
# Constraints:
#
# [time limit] 5000ms
#
# [input] array.character arr
#
# 1 <= arr.length <= 30
# [input] string str
#
# 1 <= str.length <= 500
# [output] string


def get_shortest_unique_substring(arr, string):
  output = ""

  temp_arr_str = [x for x in string]
  temp_set = set(arr)
  if len(temp_arr_str) == 1:
    size_arr = len(arr)

    if len(temp_arr_str) == size_arr and string in arr:
      return string
    else:
      return output

  chrs_count = get_chrs_count(temp_arr_str,temp_set)
  if not substring_does_exist(arr,chrs_count):
    return ""

  index_start = get_substring_index_start(temp_arr_str, chrs_count)

  index_end = get_substring_index_end(temp_arr_str, chrs_count)

  output = "".join(temp_arr_str[index_start:index_end+1])

  return output

def substring_does_exist(temp_arr,chrs_count):
  for character in temp_arr:
    if not character in chrs_count or chrs_count[character] < 1:
      return False

  return True


def get_chrs_count(temp_arr,temp_set):
  output = {}
  for character in temp_arr:
    if character in temp_set and character in output:
      output[character] += 1
    elif (character in temp_set) and (not character in output):
      output[character] = 1
  return output

def get_substring_index_start(temp_arr, chrs_count):
  idx = 0
  element =  temp_arr[idx]
  while idx < len(temp_arr):
    if element in chrs_count and chrs_count[element] - 1 >= 1:
      chrs_count[element] -= 1
    elif element in chrs_count and chrs_count[element] - 1 < 1:
      break
    idx += 1
    element =  temp_arr[idx]

  return idx

def get_substring_index_end(temp_arr, chrs_count):
  idx = len(temp_arr) - 1
  element =  temp_arr[idx]
  while idx > 0:
    if element in chrs_count and chrs_count[element] - 1 >= 1:
      chrs_count[element] -= 1
    elif element in chrs_count and chrs_count[element] - 1 < 1:
      break
    idx -= 1
    element =  temp_arr[idx]

  return idx

#===============================================================

def get_shortest_unique_substring_old(arr, string):
  temp_dict = {}

  temp_set = set(arr)

  temp_arr = [x for x in string]

  i = 0
  j = len(temp_arr) - 1

  for item in temp_arr:
    if not item in temp_set:
      continue

    if item in temp_dict:
      temp_dict[item] += 1
    else:
      temp_dict[item] = 1

  for key in temp_set:
    if key not in temp_dict:
      return ''

  while not terminating_condition_has_reached(temp_arr, temp_set, temp_dict, i, j):
    if temp_arr[i] in temp_set:
      temp_dict[temp_arr[i]] -= 1
    i += 1

  while not terminating_condition_has_reached(temp_arr, temp_set, temp_dict, j, i):
    if temp_arr[j] in temp_set:
      temp_dict[temp_arr[j]] -= 1
    j -= 1

  output = string[i:j+1]

  return output

def terminating_condition_has_reached_old(temp_arr, temp_set, temp_dict, index, index_another):
  if (temp_arr[index] in temp_set and temp_dict[temp_arr[index]] == 1) or index == index_another:
    return True
  return False

if __name__ == '__main__':
  get_shortest_unique_substring(
["A","B","C"],"ADOBECODEBANCDDD")