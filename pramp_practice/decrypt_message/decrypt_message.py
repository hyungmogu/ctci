def decrypt(word):
  output = []

  # split word into array of characters
  char_arr = [x for x in word]
  # decrypt message
  for index in range(len(char_arr)):
    if index == 0:
      output.append(chr(ord(char_arr[index]) - 1))
      continue

    diff = ord(char_arr[index]) - ord(char_arr[index-1])
    for k in range(0, 6):
      temp_char = diff + (k*26)
      if temp_char <= 122 and temp_char >= 97:
        output.append(chr(temp_char))
        break

  # recombine word into string
  output = ''.join(output)
  return output
