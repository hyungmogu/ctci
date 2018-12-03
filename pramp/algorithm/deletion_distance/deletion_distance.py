# Deletion Distance
# The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

# By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
# We cannot get the same string from both strings by deleting 2 letters or fewer.
# Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.

# Examples:

# input:  str1 = "dog", str2 = "frog"
# output: 3

# input:  str1 = "some", str2 = "some"
# output: 0

# input:  str1 = "some", str2 = "thing"
# output: 9

# input:  str1 = "", str2 = ""
# output: 0
# Constraints:

# [input] string str1
# [input] string str2
# [output] integer

def deletion_distance(str1, str2):

  if str1 == str2:
    return 0

  output = get_deletion_distance(str1,str2)

  return output


def get_deletion_distance(str1,str2):
  size_str1 = len(str1)
  size_str2 = len(str2)

  prev = [0 for x in range(size_str2+1)]
  curr = [0 for x in range(size_str2+1)]

  for idx_i in range(size_str1+1):
    for idx_j in range(size_str2+1):
      if idx_i == 0:
        curr[idx_j] = idx_j
      elif idx_j == 0:
        curr[idx_j] = idx_i
      elif str1[idx_i-1] != str2[idx_j-1]:
        curr[idx_j] = 1 + min(curr[idx_j-1],prev[idx_j])
      elif str1[idx_i-1] == str2[idx_j-1]:
        curr[idx_j] = prev[idx_j-1]

    print(curr)

    curr,prev = prev,curr
    curr = [0 for x in range(size_str2+1)]


  output = prev[-1]
  return output

if __name__ == "__main__":
  str1 = "some"
  str2 = "thing"
  print(get_deletion_distance(str1,str2))