def pancake_sort(arr):

  if len(arr) == 0 or len(arr) == 1:
    return arr

  arr_length = len(arr)
  i_arr = []

  for i in range(arr_length-1, 0, -1):
    idx_max_value = get_max_index_value(arr , i)

    if idx_max_value == i:
      continue

    flip(arr, idx_max_value + 1)
    flip(arr, i + 1)

  return arr


def get_max_index_value(arr, i):
  idx_current_max = i
  for j in range(i - 1, -1, -1):
    if arr[j] > arr[idx_current_max]:
      idx_current_max = j

  return idx_current_max


def flip(arr, k):
  idx = k - 1
  temp = 0

  temp = arr[0]
  arr[0] = arr[idx]
  arr[idx] = temp

  return arr