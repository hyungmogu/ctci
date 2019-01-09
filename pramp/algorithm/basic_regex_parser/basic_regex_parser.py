# Basic Regex Parser
# Implement a regular expression function isMatch that supports the '.' and '*' symbols. The function receives two strings - text and pattern - and should return true if the text matches the pattern as a regular expression. For simplicity, assume that the actual symbols '.' and '*' do not appear in the text string and are used as special symbols only in the pattern string.
#
# In case you aren't familiar with regular expressions, the function determines if the text and pattern are the equal, where the '.' is treated as a single a character wildcard (see third example), and '*' is matched for a zero or more sequence of the previous letter (see fourth and fifth examples). For more information on regular expression matching, see the Regular Expression Wikipedia page.
#
# Explain your algorithm, and analyze its time and space complexities.
#
# Examples:
#
# input:  text = "aa", pattern = "a"
# output: false
#
# input:  text = "aa", pattern = "aa"
# output: true
#
# input:  text = "abc", pattern = "a.c"
# output: true
#
# input:  text = "abbb", pattern = "ab*"
# output: true
#
# input:  text = "acd", pattern = "ab*c."
# output: true
# Constraints:
#
# [time limit] 5000ms
# [input] string text
# [input] string pattern
# [output] boolean

def is_match(text, pattern):

  if text.strip() == '' and pattern.strip() == '':
    return True


  temp_arr_text = [x for x in text]
  temp_arr_pattern = [x for x in pattern]

  output = get_is_match(0,0,temp_arr_text,temp_arr_pattern)

  return output

def get_is_match(i,j,temp_arr_text,temp_arr_pattern):
  output = False
  if i >= len(temp_arr_text) and j >= len(temp_arr_pattern):
    return True

  if i < len(temp_arr_text) and j >= len(temp_arr_pattern):
    return False

  if i >= len(temp_arr_text) and j < len(temp_arr_pattern):
    if is_asterisk(temp_arr_pattern,j) and j == len(temp_arr_pattern) - 1:
      return True

  if is_letter(temp_arr_pattern,j):
    if not letters_do_match(temp_arr_text,i,temp_arr_pattern,j) and not is_asterisk(temp_arr_pattern,j+1):
      return False
    elif not letters_do_match(temp_arr_text,i,temp_arr_pattern,j) and is_asterisk(temp_arr_pattern,j+1):
      output = get_is_match(i,j+1,temp_arr_text,temp_arr_pattern)
    elif letters_do_match(temp_arr_text,i,temp_arr_pattern,j):
      output = get_is_match(i+1,j+1,temp_arr_text,temp_arr_pattern)

  elif is_wildcard(temp_arr_pattern,j):
    if is_asterisk(temp_arr_pattern,j+1):
      output = get_is_match(i,j+1,temp_arr_text,temp_arr_pattern)
    else:
      output = get_is_match(i+1,j+1,temp_arr_text,temp_arr_pattern)

  elif is_asterisk(temp_arr_pattern,j):
    if is_wildcard(temp_arr_pattern,j-1) and letters_do_match(temp_arr_text,i+1,temp_arr_pattern,j+1):
      output = get_is_match(i+1,j+1,temp_arr_text,temp_arr_pattern)
    elif is_wildcard(temp_arr_pattern,j-1) and not letters_do_match(temp_arr_text,i+1,temp_arr_pattern,j+1):
      output = get_is_match(i+1,j,temp_arr_text,temp_arr_pattern)
    elif is_letter(temp_arr_pattern,j-1) and not letters_do_match(temp_arr_text,i,temp_arr_pattern,j-1):
      output = get_is_match(i,j+1,temp_arr_text,temp_arr_pattern)
    elif is_letter(temp_arr_pattern,j-1) and letters_do_match(temp_arr_text,i,temp_arr_pattern,j-1):
      output = get_is_match(i+1,j,temp_arr_text,temp_arr_pattern)

  return output

def is_letter(temp_arr_pattern,j):
  try:
    if 97 <= ord(temp_arr_pattern[j].lower()) <= 122:
      return True
  except:
    return False

def is_asterisk(temp_arr_pattern,j):
  try:
    if ord(temp_arr_pattern[j]) == 42:
      return True
  except:
    return False

def is_wildcard(temp_arr_pattern,j):
  try:
    if ord(temp_arr_pattern[j]) == 46:
      return True
  except:
    return False

def letters_do_match(temp_arr_text,i,temp_arr_pattern,j):
  try:
    if temp_arr_text[i] == temp_arr_pattern[j]:
      return True
    return False
  except:
    return False

# ================== interview 2 =======================

def is_match(text, pattern):

  if text.strip() == '' and pattern.strip() == '':
    return True


  temp_arr_text = [x for x in text]
  temp_arr_pattern = [x for x in pattern]

  output = get_is_match(0,0,temp_arr_text,temp_arr_pattern)

  return output

def get_is_match(i,j,temp_arr_text,temp_arr_pattern):
  output = False
  if i >= len(temp_arr_text) and j >= len(temp_arr_pattern):
    return True

  if i < len(temp_arr_text) and j >= len(temp_arr_pattern):
    return False

  if i >= len(temp_arr_text) and j < len(temp_arr_pattern):
    if is_asterisk(temp_arr_pattern,j) and j == len(temp_arr_pattern) - 1:
      return True

  if is_letter(temp_arr_pattern,j):
    if not letters_do_match(temp_arr_text,i,temp_arr_pattern,j) and not is_asterisk(temp_arr_pattern,j+1):
      return False
    elif not letters_do_match(temp_arr_text,i,temp_arr_pattern,j) and is_asterisk(temp_arr_pattern,j+1):
      output = get_is_match(i,j+1,temp_arr_text,temp_arr_pattern)
    elif letters_do_match(temp_arr_text,i,temp_arr_pattern,j):
      output = get_is_match(i+1,j+1,temp_arr_text,temp_arr_pattern)

  elif is_wildcard(temp_arr_pattern,j):
    if is_asterisk(temp_arr_pattern,j+1):
      output = get_is_match(i,j+1,temp_arr_text,temp_arr_pattern)
    else:
      output = get_is_match(i+1,j+1,temp_arr_text,temp_arr_pattern)

  elif is_asterisk(temp_arr_pattern,j):
    if is_wildcard(temp_arr_pattern,j-1) and letters_do_match(temp_arr_text,i+1,temp_arr_pattern,j+1):
      output = get_is_match(i+1,j+1,temp_arr_text,temp_arr_pattern)
    elif is_wildcard(temp_arr_pattern,j-1) and not letters_do_match(temp_arr_text,i+1,temp_arr_pattern,j+1):
      output = get_is_match(i+1,j,temp_arr_text,temp_arr_pattern)
    elif is_letter(temp_arr_pattern,j-1) and not letters_do_match(temp_arr_text,i,temp_arr_pattern,j-1):
      output = get_is_match(i,j+1,temp_arr_text,temp_arr_pattern)
    elif is_letter(temp_arr_pattern,j-1) and letters_do_match(temp_arr_text,i,temp_arr_pattern,j-1):
      output = get_is_match(i+1,j,temp_arr_text,temp_arr_pattern)

  return output

def is_letter(temp_arr_pattern,j):
  try:
    if 97 <= ord(temp_arr_pattern[j].lower()) <= 122:
      return True
  except:
    return False

def is_asterisk(temp_arr_pattern,j):
  try:
    if ord(temp_arr_pattern[j]) == 42:
      return True
  except:
    return False

def is_wildcard(temp_arr_pattern,j):
  try:
    if ord(temp_arr_pattern[j]) == 46:
      return True
  except:
    return False

def letters_do_match(temp_arr_text,i,temp_arr_pattern,j):
  try:
    if temp_arr_text[i] == temp_arr_pattern[j]:
      return True
    return False
  except:
    return False

if __name__ == "__main__":
  text = "abaa"
  pattern = "a.*a*"
  print(is_match(text,pattern))