#Sentence Reverse
#You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.
#
#Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.
#
#Explain your solution and analyze its time and space complexities.
#
#Example:
#
#input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
#                'm', 'a', 'k', 'e', 's', '  ',
#                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
#
#output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
#          'm', 'a', 'k', 'e', 's', '  ',
#          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
#Constraints:
#
#[time limit] 5000ms
#
#[input] array.character arr
#
#0 <= arr.length <= 100
#[output] array.character

def reverse_words(arr):

  # reverse the order of each word in arr
  temp_arr_inner = []
  temp_arr = []


  for idx, character in enumerate(arr):
    if idx == len(arr) - 1:
      temp_arr_inner.append(character)
      temp_arr.append(temp_arr_inner)
      break

    if space_is_hit(character):
      if len(temp_arr_inner) > 0:
        temp_arr.append(temp_arr_inner)

      temp_arr.append([' '])
      temp_arr_inner = []
    else:
      temp_arr_inner.append(character)

  reversed_temp_arr = reversed(temp_arr)


  output = sum(reversed_temp_arr, [])

  return output

def space_is_hit(character):
  if character.strip() == '':
    return True
  return False

