# Array Index & Element Equality
# Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.
#
# Examples:
#
# input: arr = [-8,0,2,5]
# output: 2 # since arr[2] == 2
#
# input: arr = [-1,0,3,6]
# output: -1 # since no index in arr satisfies arr[i] == i.
# Constraints:
#
# [time limit] 5000ms
#
# [input] array.integer arr
#
# 1 <= arr.length <= 100
# [output] integer

def index_equals_value_search(arr):
  result = {'value': -1}
  low = 0
  high = len(arr) - 1

  get_index_equals_value(low,high,arr,result)
  output = result['value']
  return output


def get_index_equals_value(low, high, arr, result):
    if low > high:
      return

    middle_point = (low + high) / 2

    diff = arr[middle_point] - middle_point
    diff_prev = arr[middle_point - 1] - (middle_point - 1)

    if (diff == 0 and middle_point == 0) or (diff == 0 and diff_prev < 0):
      result['value'] = middle_point
      return

    if diff > 0:
      high = middle_point - 1
    elif diff == 0 and diff_prev == 0:
      high = middle_point - 1
    else:
      low = middle_point + 1

    get_index_equals_value(low,high,arr,result)
