import types as t

def insertion_sort(arr, size):
  if type(arr) != t.ListType or type(size) != t.IntType:
    raise TypeError("The argument has wrong type. They must be in the format (array, int)")

  if arr:
    if size == 1:
      return arr

    i = 1

    while i < size:
      index_element_to_sort = i
      while index_element_to_sort > 0:
        if arr[index_element_to_sort] >= arr[index_element_to_sort - 1]:
          break
        else:
          temp = arr[index_element_to_sort]
          arr[index_element_to_sort] = arr[index_element_to_sort - 1]
          arr[index_element_to_sort - 1] = temp
          index_element_to_sort -= 1

      i += 1

    return arr
    
  else:
    raise LookupError("Array must have more than one element")