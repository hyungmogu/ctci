# Bracket Match
# A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a later closing bracket, and vice versa. For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.
#
# Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched.
#
# Explain the correctness of your code, and analyze its time and space complexities.
#
# Examples:
#
# input:  text = “(()”
# output: 1
#
# input:  text = “(())”
# output: 0
#
# input:  text = “())(”
# output: 2
# Constraints:
#
# [time limit] 5000ms
#
# [input] string text
#
# 1 <= text.length <= 5000
# [output] integer
def bracket_match(text):

  # evaluate number of brackets required to complete the incomplete set of brackets

  temp_arr = [x for x in text]
  num_left_brackets = 0
  num_right_brackets = 0
  output = 0

  for index, bracket in enumerate(temp_arr):
    if the_end_of_set_reached(temp_arr,index):
      num_right_brackets += 1
      output += abs(num_left_brackets - num_right_brackets)

      num_left_brackets = 0
      num_right_brackets = 0
    else:
      if bracket == "(":
        num_left_brackets += 1
      elif bracket == ")":
        num_right_brackets += 1

  return output

def the_end_of_set_reached(temp_arr,index):
  if (index == len(temp_arr) - 1) or (index < (len(temp_arr) - 1) and temp_arr[index] == ")" and temp_arr[index+1] == "("):
    return True
  return False