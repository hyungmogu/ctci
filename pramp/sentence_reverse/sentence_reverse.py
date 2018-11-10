def reverse_words(arr):

  # reverse the order of words

  temp = []
  temp_inner = []
  output = []
  # elementrify each word inside array
  for idx,item in enumerate(arr):
    if space_is_hit(item):
      if len(temp_inner) > 0:
        temp.append(temp_inner)
        temp.append([' '])
      elif len(temp_inner) == 0:
        temp.append([' '])
      temp_inner = []
    elif is_at_the_end_of_arr(arr,idx):
      temp_inner.append(item)
      temp.append(temp_inner)
    else:
      temp_inner.append(item)

  # reverse the order of words
  temp = temp[::-1]

  # put back the elements elements together
  for idx,item in enumerate(temp):
    if idx != len(temp) - 1:
      output += item
    else:
      output += item

  return output

def space_is_hit(item):
  if item.strip() == '':
    return True
  return False

def is_at_the_end_of_arr(arr,idx):
  if idx != len(arr) - 1:
    return False
  return True