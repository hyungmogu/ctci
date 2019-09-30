# ============= Part 1 =============
# Task 1
# Write a function named delorean that takes an integer.
# Return a datetime that is that many hours ahead from starter.

import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def delorean(integer):
    return datetime.datetime(2015,10,21,16,29) + datetime.timedelta(hours=integer)


# solution 2

import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def delorean(value):
    return starter + datetime.timedelta(hours=value)

# ============= Part 2 =============
# Task 1
# Write a function named time_machine that takes an integer and a string of "minutes",
# "hours", "days", or "years". This describes a timedelta. Return a datetime that is
# the timedelta's duration from the starter datetime.
#
# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.
#
## Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)

import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def time_machine(integer, time_type):
    kwarg = {time_type: integer} if time_type != 'years' else {"days": integer * 365}
    return datetime.datetime(2015, 10, 21, 16, 29) + datetime.timedelta(**kwarg)

# ============= Part 3 =============
# Task 1
# Create a function named timestamp_oldest that takes any number of POSIX timestamp
# arguments. Return the oldest one as a datetime object.
#
# Remember, POSIX timestamps are floats and lists have a .sort() method.

import datetime

def timestamp_oldest(*timestamps):
    oldest_timestamp = -1

    for timestamp in timestamps:
        if oldest_timestamp > timestamp:
            oldest_timestamp = timestamp

    return datetime.datetime.fromtimestamp(oldest_timestamp)

