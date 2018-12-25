# Decrypt Message
# An infamous gang of cyber criminals named “The Gray Cyber Mob”, which is behind many hacking attacks and drug trafficking, has recently become a target for the FBI. After intercepting some of their messages, which looked like complete nonsense, the agency learned that they indeed encrypt their messages, and studied their method of encryption.
#
# Their messages consist of lowercase latin letters only, and every word is encrypted separately as follows:
#
# Convert every letter to its ASCII value. Add 1 to the first letter, and then for every letter from the second one to the last one, add the value of the previous letter. Subtract 26 from every letter until it is in the range of lowercase letters a-z in ASCII. Convert the values back to letters.
#
# For instance, to encrypt the word “crime”
#
# Decrypted message:	c	r	i	m	e
# Step 1:	99	114	105	109	101
# Step 2:	100	214	319	428	529
# Step 3:	100	110	111	116	113
# Encrypted message:	d	n	o	t	q
# The FBI needs an efficient method to decrypt messages. Write a function named decrypt(word) that receives a string that consists of small latin letters only, and returns the decrypted word.
#
# Explain your solution and analyze its time and space complexities.
#
# Examples:
#
# input:  word = "dnotq"
# output: "crime"
#
# input:  word = "flgxswdliefy"
# output: "encyclopedia"
# Since the function should be used on messages with many words, make sure the function is as efficient as possible in both time and space. Explain the correctness of your function, and analyze its asymptotic runtime and space complexity.
#
# Note: Most programing languages have built-in methods of converting letters to ASCII values and vica versa. You may search the internet for the appropriate method.
#
# Constraints:
#
# [time limit] 5000ms
#
# [input] string word
#
# The ASCII value of every char is in the range of lowercase letters a-z.
# [output] string


def decrypt(word):

  # separate word into arr of characters
  encrypted_chars = [x for x in word]
  decrypted_chars = []
  middle_char = 0

  if word == '':
    return word

  # decrypt characters in word
  for idx,char in enumerate(encrypted_chars):
    if idx == 0:
      decrypted_char = chr(ord(char) - 1)
      decrypted_chars.append(decrypted_char)
      middle_char = ord(char)
    else:
      temp = ord(char) - middle_char

      while not is_a_lower_case_letter(temp):
        temp += 26

      decrypted_char = chr(temp)

      decrypted_chars.append(decrypted_char)

      middle_char += temp

  # put together array of decrypted characters into string
  output = ''.join(decrypted_chars)

  return output

def is_a_lower_case_letter(temp):
  if temp < 97 or temp > 122:
    return False
  return True

# ============ Review 4 ================

def decrypt(word):
    temp_arr = [x for x in word]
    output = []
    m = 1

    if word.strip() == '':
        return ''

    for idx, character in enumerate(word):
        temp_val = ord(character) - m

        while not (temp_val <= 122 and temp_val >= 97):
            temp_val += 26

        m += temp_val

        output.append(chr(temp_val))

    return "".join(output)