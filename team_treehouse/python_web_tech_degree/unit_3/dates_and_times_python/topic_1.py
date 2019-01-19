# ============= Part 1 =============
# Task 1
# Import the datetime library

import datetime

# Task 2
# Create a variable named now that holds the results of datetime.datetime.now()

import datetime
now = datetime.datetime.now()

# Task 3
# Create a new variable called two that holds the value of now with the hour
# set to 14. Use the .replace() method.

import datetime
now = datetime.datetime.now()
two = now.replace(hour=14,minute=0,second=0,microsecond=0)

# Task 4
# Finally, change two so its minute is 30.

import datetime
now = datetime.datetime.now()
two = now.replace(hour=14,minute=0,second=0,microsecond=0)
two = two.replace(minute=30) # This doesn't modify the same datetime object. two.replace(minute=30) alone is not enough

# ============= Part 2 =============
# Task 1
# Write a function called far_away that takes one argument, a timedelta.
# Add that timedelta to datetime.datetime.now() and return the resulting
# datetime object.

import datetime

def far_away(timedelta):
    return datetime.datetime.now() + timedelta


# ============== Part 3 =============
# Task 1
# Write a function named minutes that takes two datetimes and, using
# timedelta.total_seconds() to get the number of seconds, returns the
# number of minutes, rounded, between them. The first will always be
# older and the second newer. You'll need to subtract the first from the second.

import datetime

def minutes(datetime1,datetime2):
    timedelta = datetime2 - datetime1
    output = timedelta.total_seconds() / 60.0
    return round(output)

# ============== Part 4 =============
# Task 1
# Create a function named to_string that takes a datetime and gives back
# a string in the format "24 September 2012".

import datetime

def to_string(datetime):
    return datetime.strftime('%d %B %Y')

# Task 2
# Create a new function named from_string that takes two arguments: a
# date as a string and an strftime-compatible format string, and returns
# a datetime created from them.

import datetime

def to_string(datetime):
    return datetime.strftime('%d %B %Y')

def from_string(date,date_format):
    return datetime.datetime.strptime(date, date_format)

# ============== Part 4 =============
# Write a function named time_tango that takes a date and a time. It should
# combine them into a datetime and return it.

import datetime

def time_tango(date, time):
    return datetime.datetime.combine(date,time)

