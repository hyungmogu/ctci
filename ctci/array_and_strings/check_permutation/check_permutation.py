import types as t

import insertion_sort as i

def is_permutation(str1, str2): 
  if type(str1) != t.StringType or type(str2) != t.StringType:
    raise TypeError("Both arguements must be string")

  str1 = str1.rstrip()
  str2 = str2.rstrip()

  if str1 == "" or str2 == "":
    raise ValueError("Both of the arguements must be non-emtpy")

  arr1 = [x for x in str1]
  arr2 = [y for y in str2]

  size1 = len(arr1)
  size2 = len(arr2)

  if size1 != size2:
    return False

  arr1 = i.insertion_sort(arr1, size1)
  arr2 = i.insertion_sort(arr2, size2)

  j = 0
  k = 0

  while j < size1:
    if arr1[j] != arr2[k]:
      return False

    j += 1
    k += 1

  return True
