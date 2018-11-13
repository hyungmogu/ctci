# Flatten a Dictionary
# A dictionary is a type of data structure that is supported natively in all major interpreted languages such as JavaScript, Python, Ruby and PHP, where it's known as an Object, Dictionary, Hash and Array, respectively. In simple terms, a dictionary is a collection of unique keys and their values. The values can typically be of any primitive type (i.e an integer, boolean, double, string etc) or other dictionaries (dictionaries can be nested). However, for this exercise assume that values are either an integer, a string or another dictionary.
#
# Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .
#
# If you're using a compiled language such Java, C++, C#, Swift and Go, you may want to use a Map/Dictionary/Hash Table that maps strings (keys) to a generic type (e.g. Object in Java, AnyObject in Swift etc.) to allow nested dictionaries.
#
# If a certain key is empty, it should be excluded from the output (see e in the example below).
#
# Example:
#
# input:  dict = {
#             "Key1" : "1",
#             "Key2" : {
#                 "a" : "2",
#                 "b" : "3",
#                 "c" : {
#                     "d" : "3",
#                     "e" : {
#                         "" : "1"
#                     }
#                 }
#             }
#         }
#
# output: {
#             "Key1" : "1",
#             "Key2.a" : "2",
#             "Key2.b" : "3",
#             "Key2.c.d" : "3",
#             "Key2.c.e" : "1"
#         }
# Important: when you concatenate keys, make sure to add the dot character between them. For instance concatenating Key2, c and d the result key would be Key2.c.d.
#
# Constraints:
#
# [time limit] 5000ms
# [input] Dictionary dict
# [output] Dictionary


def flatten_dictionary(dictionary):
  flattened_dict_list = []

  for key in dictionary.keys():
    temp_arr = get_flatten_dictionary(dictionary[key], key)
    flattened_dict_list += temp_arr

  output = dict(flattened_dict_list)

  return output

def get_flatten_dictionary(dict_value, current_key):
  output = []

  if type(dict_value) != dict:
    return [[current_key, dict_value]]

  for child_key in dict_value.keys():
    flattened_key_value_pairs = get_flatten_dictionary(dict_value[child_key], child_key)
    output += flattened_key_value_pairs

  for key_value_pair in output:
    child_key = key_value_pair[0]

    if current_key == '' and child_key == '':
      continue
    elif current_key != '' and child_key == '':
      key_value_pair[0] = current_key
    elif current_key == '' and child_key != '':
      key_value_pair[0] = child_key
    else:
      key_value_pair[0] = '{0}.{1}'.format(current_key,child_key)

  # 3. return the output
  return output



