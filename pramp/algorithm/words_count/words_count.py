# Word Count Engine
# Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count, they should be sorted according to their order in the original sentence. Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the words 'Perfect' and 'perfect' should be considered the same word.
#
# The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.
#
# Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space complexity.
#
# Examples:
#
# input:  document = "Practice makes perfect. you'll only
#                     get Perfect by practice. just practice!"
#
# output: [ ["practice", "3"], ["perfect", "2"],
#           ["makes", "1"], ["youll", "1"], ["only", "1"],
#           ["get", "1"], ["by", "1"], ["just", "1"] ]
# Important: please convert the occurrence integers in the output list to strings (e.g. "3" instead of 3). We ask this because in compiled languages such as C#, Java, C++, C etc., it's not straightforward to create mixed-type arrays (as it is, for instance, in scripted languages like JavaScript, Python, Ruby etc.). The expected output will simply be an array of string arrays.
#
# Constraints:
#
# [time limit] 5000ms
# [input] string document
# [output] array.array.string



import re
from collections import OrderedDict

# ============= Review 2 ============

def word_count_engine(document):
  temp_dict = OrderedDict()

  document = document.strip()

  document = re.sub('[^a-zA-Z\s]','',document)
  document = re.sub('\s+',' ',document)

  document = document.lower()

  for word in document.split(' '):
    if word in temp_dict:
      temp_dict[word] += 1
    else:
      temp_dict[word] = 1

  output = [[x[0], str(x[1])] for x in temp_dict.items()]
  output = sorted(output,key=lambda x: int(x[1]),reverse=True)

  return output

# ===================================


def words_count_engine_old(document):
  keywords_count = count_keywords(document)
  sort_by_count(keywords_count)
  return keywords_count # your code goes here

def count_keywords_old(document):
    words = document.split()
    output = []
    keywords_count = {}

    for word in words:
        new_word = strip_punctuation(word).lower()
        if (not keywords_count.get(new_word)):

            keywords_count[new_word] = 1
        else:
            keywords_count[new_word] += 1

    for key, value in keywords_count.iteritems():
        keyword_count = [key, str(value)]
        output.append(keyword_count)

    return output

def sort_by_count_old(keywords_count_list):
    keywords_count_list.sort(reverse = True, key = lambda keyword: keyword[1])
    return

def strip_punctuation_old(key):
    output = []
    letters = [ x for x in key]

    for letter in letters:
        # if specialized character exists, then omit it
        if (not letter.isalpha()):
            continue

        output.append(letter)

    return ''.join(output)


if __name__ == "__main__":
  document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
  print(word_count_engine(document))