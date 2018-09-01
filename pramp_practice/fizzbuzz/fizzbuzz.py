# Fizz_buzz
#
# Write a program that console logs the numbers from 1 to n.
# But for multiple of three print 'fizz' instead of the number and for
# the multiples of five print 'buzz'. For numbers which are multiples of
# both three and five print 'fizzbuzz'
#
# fizzbuzz(15)
# 1
# 2
# fizz
# 4
# buzz
# ...
# fizzbuzz
#
# fizzbuzz("hello") -> throw type error
#
# fizbuzz(0) -> throw value error

def fizzbuzz(number):

    if type(number) != int:
        raise TypeError

    if number < 1:
        raise ValueError

    output = get_fizzbuzz(number)

    for i in output:
        print("{0} \n".format(i))

def get_fizzbuzz(number):
    output = []

    for i in range(1, number+1):
        if (i % 3 == 0) and (i % 5 == 0):
            output.append('fizzbuzz')
        elif i % 3 == 0:
            output.append('fizz')
        elif i % 5 == 0:
            output.append('buzz')
        else:
            output.append(i)

    return output
