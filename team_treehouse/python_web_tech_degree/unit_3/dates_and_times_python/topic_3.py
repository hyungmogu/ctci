# ============= Part 1 =============
# Task 1
# Create a variable named moscow that holds a datetime.timezone object at +4 hours.

import datetime

moscow = datetime.timezone(datetime.timedelta(hours=4))

# Task 2
# Now create a timezone variable named pacific that holds a timezone at UTC-08:00.

import datetime

moscow = datetime.timezone(datetime.timedelta(hours=4))
pacific = datetime.timezone(datetime.timedelta(hours=-8))

# Task 3
# Finally, make a third variable named india that hold's a timezone at UTC+05:30.

import datetime

moscow = datetime.timezone(datetime.timedelta(hours=4))
pacific = datetime.timezone(datetime.timedelta(hours=-8))
india = datetime.timezone(datetime.timedelta(hours=5,minutes=30))

# ============= Part 2 =============
# Task 1
# naive is a datetime with no timezone.
# Create a new timezone for US/Pacific, which is 8 hours behind UTC (UTC-08:00).
#
# Then make a new variable named hill_valley that is naive with its tzinfo attribute
# replaced with the US/Pacific timezone you made.

import datetime

naive = datetime.datetime(2015, 10, 21, 4, 29)
pacific = datetime.timezone(datetime.timedelta(hours=-8))
hill_valley = datetime.datetime(2015, 10, 21, 4, 29, tzinfo=pacific)

# solution 2

import datetime
import copy

naive = datetime.datetime(2015, 10, 21, 4, 29)

timezone = datetime.timezone(datetime.timedelta(hours=-8))
hill_valley = naive.replace(tzinfo=timezone)


# Task 2
# Great, but replace just sets the timezone, it doesn't move the datetime to the new
# timezone. Let's move one.
#
# Make a new timezone that is UTC+01:00.
#
# Create a new variable named paris that uses your new timezone and the astimezone
# method to change hill_valley to the new timezone.

import datetime

naive = datetime.datetime(2015, 10, 21, 4, 29)
pacific = datetime.timezone(datetime.timedelta(hours=-8))
new_timezone = datetime.timezone(datetime.timedelta(hours=1))

hill_valley = datetime.datetime(2015, 10, 21, 4, 29, tzinfo=pacific)
paris = hill_valley.astimezone(new_timezone) # astimezone moves time in a timezone to another (i.e from pacific to eastern)

# solution 2

import datetime
import copy

naive = datetime.datetime(2015, 10, 21, 4, 29)

timezone = datetime.timezone(datetime.timedelta(hours=-8))
new_timezone = datetime.timezone(datetime.timedelta(hours=1))
hill_valley = naive.replace(tzinfo=timezone)
paris = hill_valley.astimezone(new_timezone)


# ============= Part 3 =============
# Task 1
# starter is a naive datetime. Use pytz to make it a "US/Pacific" datetime
# instead and assign this converted datetime to the variable local.

import datetime
import pytz

fmt = '%m-%d %H:%M %Z%z'
starter = datetime.datetime(2015, 10, 21, 4, 29)
pacific = pytz.timezone('US/Pacific')
local = pacific.localize(starter)


# Task 2
# Now create a variable named pytz_string by using strftime with the local
# datetime. Use the fmt string for the formatting.

import datetime
import pytz

fmt = '%m-%d %H:%M %Z%z'
starter = datetime.datetime(2015, 10, 21, 4, 29)
pacific = pytz.timezone('US/Pacific')
local = pacific.localize(starter) # this is datetime object with tzinfo containing values of pytz object

pytz_string = local.strftime(fmt)


# ============= Part 4 =============
# Task 1
# Create a function named to_timezone that takes a timezone name as a string.
# Convert starter to that timezone using pytz's timezones and return the new
# datetime.

import datetime

import pytz

starter = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))

def to_timezone(timezone_name):
    utc = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))
    # convert starter to that timezone using pytz's timezone
    timezone = pytz.timezone(timezone_name)
    new_time = utc.astimezone(timezone)

    return new_time