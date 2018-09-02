#
# is_palindrome()
#
# Given a string, return true if the string is a palindrome
# or false if it is not. palindrome are strings that form the same word
# if it's reversed. *Do* include spaces and punctuation in determining
# if the string is a palindrome

# is_palindrome("aba") -> true
# is_palindrome("abcdef") -> false

# is_palindrome(0) -> raise TypeError
# is_palindrome('') -> valueError
# is_palindrome('    ') -> should not raise value error

def is_palindrome(letters):
    output = False

    if type(letters) != str:
        raise TypeError

    if letters == '':
        raise ValueError

    arr_chars = [x for x in letters]
    arr_chars_reversed = arr_chars[::-1]
    letters_reversed = ''.join(arr_chars_reversed)

    if letters_reversed == letters:
        output = True

    return output

