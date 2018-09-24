# capitalize letter
#
# write a function that acppets a string. The function
# should capitalize the first letter of each word in the
# string then return the capitalized string
#
# capitalize_letter('  hello  world   ') --> 'Hello World'
# capitalize_letter('Abc') --> 'Abc'
# capitalize_letter('!heloo') --> '!heloo'
# capitalize_letter('!hello abc #def') --> '!hello Abc #def'
# capitalize_letter('') --> ValueError
# capitalize_letter(0) --> TypeError

def capitalize_letter(words):
    output = ''

    if type(words) != str:
        raise TypeError

    words = words.strip()

    if words == '':
        raise ValueError

    chars_words = [x for x in words]

    for idx, char in enumerate(chars_words):

        if idx == 0 and is_lower_case_letter(char):
            chars_words[idx] = chr(ord(char) - 32)

        if ord(char) == 32 and is_lower_case_letter(chars_words[idx+1]):
            chars_words[idx+1] = chr(ord(chars_words[idx+1]) - 32)

    output = ''.join(chars_words)

    return output


def is_lower_case_letter(char):
    try:
        if ord(char) <= 122 and ord(char) >= 97:
            return True
        else:
            return False
    except:
        return False




