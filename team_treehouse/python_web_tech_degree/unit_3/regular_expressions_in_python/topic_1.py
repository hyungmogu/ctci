# ============== Part 1 =============
# Task 1
# Use open() to load the file "basics.txt" into the variable file_object.

file_object = open('basics.txt','r')

# Task 2
# Read the contents of file_object into a new variable named data.

file_object = open('basics.txt','r')
data = file_object.read()


# Task 3
# Now close the file_object file so it isn't taking up memory.

file_object = open('basics.txt','r')
data = file_object.read()
file_object.close() # this is done to conserve memory

# Task 4
# Import re. Create an re.match() for the word "Four" in the data variable.
# Assign this to a new variable named first.

import re

file_object = open('basics.txt','r')
data = file_object.read()
file_object.close()

first = re.match(r'Four', data) # this returns the first match in string or data

# Task 5
# Finally, make a new variable named liberty that is an re.search()
# for the word "Liberty" in our data variable.

import re

file_object = open('basics.txt','r')
data = file_object.read()
file_object.close()

first = re.match(r'Four', data) # this returns the front-most match in string or data
liberty = re.search(r'Liberty', data) # this returns the first match in string or data

# ============== Part 2 =============

# Task 1
# Write a function named first_number that takes a string as an argument.
# The function should search, with a regular expression, the first number
# in the string and return the match object.

import re

def first_number(string):
	return re.search(r'\d', string)

# Task 2
# Now, write a function named numbers() that takes two arguments: a count
# as an integer and a string. Return an re.search for exactly count numbers
# in the string. Remember, you can multiply strings and integers to create
# your pattern.
#
# For example: r"\w" * 5 would create r"\w\w\w\w\w".

import re

def first_number(string):
	return re.search(r'\d', string)

def numbers(count,string):
    return re.search(r'\d' * count, string)


# ============== Part 3 =============
# Task 1
# Create a function named phone_numbers that takes a string and returns
# all of the phone numbers in the string using re.findall(). The phone
# numbers will all be in the format 555-555-5555.

import re

def phone_numbers(string):
    return re.findall(r'\d{3}\-\d{3}\-\d{4}', string)

# ============== Part 4 =============
# Task 1
# Create a function named find_words that takes a count and a string.
# Return a list of all of the words in the string that are count word
# characters long or longer.

import re

def find_words(count, string):
    return re.findall(r'\w{' + str(count) + ',}', string)


# ============== Part 5 =============
# Task 1
# Create a function named find_emails that takes a string. Return a
# list of all of the email addresses in the string.

import re

def find_emails(string):
    return re.findall(r'\b[^\@\,]+\@[\w\d\.]+\b', string)

# ============== Part 6 =============
# Task 1
# Create a variable named good_numbers that is an re.findall() where
# the pattern matches anything in string except the numbers 5, 6, and 7.

import re

string = '1234567890'

good_numbers = re.findall(r'[^567]', string)

# ============== Part 7 =============
# Task 1
# Create a variable names that is an re.match() against string. The
# pattern should provide two groups, one for a last name match and
# one for a first name match. The name parts are separated by a comma
# and a space.

import re

string = 'Perotto, Pier Giorgio'

names = re.match(r'(?P<first>\w+)\,\s(?P<last>[\w\s]+)',string)

# ============== Part 8 =============
# Task 1
# Create a new variable named contacts that is an re.search() where
# the pattern catches the email address and phone number from string.
# Name the email pattern email and the phone number pattern phone.
# The comma and spaces * should not* be part of the groups.

import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''


contacts = re.search(r'(?P<email>\b[^\@\,]+\@[\w\d\.]+\b)\,\s(?P<phone>\d{3}\-\d{3}\-\d{4})', string)

# Task 2
# Great! Now, make a new variable, twitters that is an re.search() where the
# pattern catches the Twitter handle for a person. Remember to mark it as being
# at the end of the string. You'll also want to use the re.MULTILINE flag.

import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'(?P<email>\b[^\@\,]+\@[\w\d\.]+\b)\,\s(?P<phone>\d{3}\-\d{3}\-\d{4})', string)
twitters = re.search(r'(\@[\w\d]+)$',string, re.M) #re.M allows the usage of multiline regex expressions

# ============== Part 9 =============
# Task 1
# Create a variable named players that is an re.search() or re.match() to capture three
# groups: last_name, first_name, and score. It should include re.MULTILINE.

import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'^(?P<last_name>[\w\s]+)\,\s(?P<first_name>[\w\s]+)\:\s(?P<score>\d+)$',string,re.M)

# Task #2
# Wow! OK, now, create a class named Player that has those same three attributes,
# last_name, first_name, and score. I should be able to set them through __init__.

import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'^(?P<last_name>[\w\s]+)\,\s(?P<first_name>[\w\s]+)\:\s(?P<score>\d+)$',string,re.M)

class Player:
    def __init__(self,**kwargs):
        for name,value in kwargs.items():
            setattr(self,name,value)