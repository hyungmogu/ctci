# Get Your Vowels
# Write a function that returns the number of voewls
# used in a string. Vowels are the characters 'a', 'e', 'i', 'o', 'u'

# examples
# get_your_vowels('hello world!') -> 3
# get_your_vowels('') -> valuError
# get_your_vowels(0) -> TypeError

def get_your_vowels(words):
    vowels_count = 0

    if type(words) != str:
        raise TypeError

    words = words.strip()

    if words == '':
        raise ValueError

    arr_char = [x for x in words]

    for char in arr_char:
        if char in ['a','e','i','o','u']:
            vowels_count += 1

    return vowels_count