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

def find_duplicates(arr1, arr2):
  output = []
  set_arr1 = set(arr1)
  set_arr2 = set(arr2)
  intersection = set_arr1.intersection(set_arr2)

  for element in arr1:
    if element in intersection:
      output.append(element)

  return output

if __name__ == '__main__':
  arr1 = [1, 2, 3, 5, 6, 7]
  arr2 = [3, 6, 7, 8, 20]
  print(find_duplicates(arr1,arr2))