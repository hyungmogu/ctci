# Find The Duplicates
# Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

# Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions: M ~ N - the array lengths are approximately the same M >> N - arr2 is much bigger than arr1.

# Example:

# input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

# output: [3, 6, 7] # since only these three values are both in arr1 and arr2
# Constraints:

# [time limit] 5000ms

# [input] array.integer arr1

# 1 <= arr1.length <= 100
# [input] array.integer arr2

# 1 <= arr2.length <= 100
# [output] array.integer

#===========================================

def find_duplicates_pramp_solution(arr1, arr2):
  output = []
  set_arr1 = set(arr1)
  set_arr2 = set(arr2)
  intersection = set_arr1.intersection(set_arr2)

  for element in arr1:
    if element in intersection:
      output.append(element)

  return output

# ============= Review 1 ===================

def find_duplicates(arr1, arr2):

  output = []
  size_arr1 = len(arr1)
  size_arr2 = len(arr2)

  if size_arr1 <= size_arr2:
    temp_arr_smaller = arr1
    temp_arr_bigger = arr2
  else:
    temp_arr_smaller = arr2
    temp_arr_bigger = arr1

  for element in temp_arr_smaller:
    duplicate_index = get_index_duplicate(element,temp_arr_bigger,0,len(temp_arr_bigger)-1)

    if duplicate_index > -1 and not element_included_in_output(element,output):
      output.append(element)

  return output


def get_index_duplicate(element,temp_arr_bigger,i,j):
  if i > j:
    return -1

  middle_index = (i + j) / 2

  if temp_arr_bigger[middle_index] == element:
    output = middle_index

  else:
    if temp_arr_bigger[middle_index] > element:
      output = get_index_duplicate(element,temp_arr_bigger,i,middle_index - 1)
    else:
      output = get_index_duplicate(element,temp_arr_bigger,middle_index + 1,j)

  return output

def find_duplicates_old(arr1, arr2):
  output = []

  size_arr1 = len(arr1)
  size_arr2 = len(arr2)

  if size_arr1 >= size_arr2:
    temp_set = set(arr2)
    temp_arr = arr1
  else:
    temp_set = set(arr1)
    temp_arr = arr2

  for element in temp_arr:
    if element in temp_set and not element_included_in_output(element,output):
      output.append(element)

  return output

def element_included_in_output(element, output):
  last_index = len(output) - 1

  if len(output) == 0:
    return False

  if output[last_index] != element:
    return False

  return True

  # ============== Review 2 =================

  def find_duplicates_sol1(arr1, arr2):
  size_arr1 = len(arr1)
  size_arr2 = len(arr2)
  output = []

  if size_arr1 > size_arr2:
    temp_set = set(arr1)
    temp_arr = arr2
  else:
    temp_set = set(arr2)
    temp_arr = arr1

  for element in temp_arr:
    if element in temp_set:
      output.append(element)

  return output


def find_duplicates_sol2(arr1,arr2):
  if len(arr1) > len(arr2):
    arr_smaller = arr2
    arr_bigger = arr1
  else:
    arr_smaller = arr1
    arr_bigger = arr2

  size_arr_smaller = len(arr_smaller)
  size_arr_bigger = len(arr_bigger)
  idx_arr_smaller = 0
  idx_arr_bigger = 0
  output = []

  while idx_arr_smaller < size_arr_smaller and idx_arr_bigger < size_arr_bigger:
    if arr_smaller[idx_arr_smaller] != arr_bigger[idx_arr_bigger] and arr_smaller[idx_arr_smaller] > arr_bigger[idx_arr_bigger]:
      idx_arr_bigger += 1

    elif arr_smaller[idx_arr_smaller] != arr_bigger[idx_arr_bigger] and arr_smaller[idx_arr_smaller] < arr_bigger[idx_arr_bigger]:
      idx_arr_smaller +=1

    elif arr_smaller[idx_arr_smaller] == arr_bigger[idx_arr_bigger]:
      output.append(arr_smaller[idx_arr_smaller])
      idx_arr_smaller +=1

  return output

def find_duplicates_sol3(arr1,arr2):
  output = []

  if len(arr1) > len(arr2):
    smaller_arr = arr2
    bigger_arr = arr1
  else:
    smaller_arr = arr1
    bigger_arr = arr2

  for element in small_arr:
    if common_element_exists(bigger_arr,solution,lower_bnd,upper_bnd):
      output.append(element)

  return output

def common_element_exists(bigger_arr,solution,lower_bnd,upper_bnd):

  if upper_bnd < lower_bnd:
    return False

  middle_idx = (lower_bnd + upper_bnd) / 2
  guess = bigger_arr[middle_idx]

  if solution == guess:
    return True

  if guess > solution:
    common_element_exists(bigger_arr,solution,lower_bnd, middle_idx - 1)
  else:
    common_element_exists(bigger_arr,solution, middle_idx + 1, upper_bnd)