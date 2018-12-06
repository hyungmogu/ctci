# Shifted Array Search
# A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don't have a pre-shifted copy of it. For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.
#
# Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. If num isn't in shiftArr, return -1. Assume that the offset doesn't equal to 0 (i.e. assume the array is shifted at least once) or to arr.length - 1 (i.e. assume the shifted array isn't fully reversed).
#
# Explain your solution and analyze its time and space complexities.
#
# Example:
#
# input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
#                                                  # outcome of shifting
#                                                  # [2, 4, 5, 9, 12, 17]
#                                                  # three times to the left
#
# output: 3 # since it's the index of 2 in arr
# Constraints:
#
# [time limit] 5000ms
# [input] array.integer arr
# [input] integer num
# [output] integer

# =============== review 1 ====================

def shifted_arr_search_review1(shiftArr, num):
  temp_set = set(shiftArr)
  if not num in temp_set:
    return -1

  shifts = 0
  for idx,item in enumerate(shiftArr):
    if not item == num:
      shifts += 1
    else:
      break

  return shifts


#  ============ review 2 =======================

def get_shifted_arr_search_review2(idx_low,idx_high,num,shifted_arr,output):
    if terminating_condition_is_reached_review2(idx_low,idx_high):
        output['value'] = -1
        return

    idx_middle_point = (idx_low + idx_high) / 2

    if shifted_arr[idx_middle_point] == num:
        output['value'] = idx_middle_point
        return idx_middle_point

    if num < shifted_arr[idx_middle_point] and num >= shifted_arr[idx_low]:
        get_shifted_arr_search_review2(idx_low,idx_middle_point-1,num,shifted_arr,output)
    else:
        get_shifted_arr_search_review2(idx_middle_point+1,idx_high,num,shifted_arr,output)

def terminating_condition_is_reached_review2(idx_low,idx_high):
    if idx_low > idx_high:
        return True
    return False


def shifted_arr_search_review2(shiftArr, num):
    result = {'value': -1}
    size_shiftArr = len(shiftArr) -1
    get_shifted_arr_search_review2(0, size_shiftArr, num, shiftArr, result)

    output = result['value']
    return output

