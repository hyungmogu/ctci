# anagram
# Check to see if two provided strings are anagrams of eachother
# One string is an anagram of another if it uses the same characters
# in the same quantity. Only consider characters, not spaces or punctuation.
# Consider capital letters to be the same as lower case.

# example
# anagram('RAIL SAFETY!', 'fairy tales') --> true

import re

def anagram(a, b):
    if type(a) != str or type(b) != str:
        raise TypeError

    if a == '' or b == '':
        raise ValueError

    a = strip_special_characters(a).lower()
    b = strip_special_characters(b).lower()

    if is_anagram(a,b):
        return True
    else:
        return False

def strip_special_characters(word):
    return re.sub(r'[^a-zA-Z]', '', word)

def is_anagram(a, b):
    a_chars = [x for x in a]
    b_chars = [x for x in b]

    dict_a = {}
    dict_b = {}

    # strip out a and b, and place them inside dictionary
    for char in a_chars:
        if char in dict_a:
            dict_a[char] += 1
        else:
            dict_a[char] = 1

    for char in b_chars:
        if char in dict_b:
            dict_b[char] += 1
        else:
            dict_b[char] = 1

    # comapre the dictionary

    for key in dict_a.keys():
        if key not in dict_b:
            return False

        if dict_a[key] != dict_b[key]:
            return False

    return True


