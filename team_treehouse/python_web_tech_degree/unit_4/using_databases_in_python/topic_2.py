# ============= Part 1 =============
# Task 1 of 3
# Create a variable named db that is an SqliteDatabase with a filename of challenges.db.

from peewee import *


db = SqliteDatabase('challenges.db')

class Challenge(Model):
    name = CharField(max_length=100)
    language = CharField(max_length=100)
    steps = IntegerField(default=1)


# Task 2 of 3
# Now add db as the database attribute in the Meta class for Challenge.

from peewee import *


db = SqliteDatabase('challenges.db')

class Challenge(Model):
    name = CharField(max_length=100)
    language = CharField(max_length=100)
    steps = IntegerField(default=1)

    class Meta:
        database = db

# Task 3 of 3
# Finally, create a function named initialize. Your initialize() function should connect to the database and then create the Challenge table. Make sure it creates the table safely.

from peewee import *


db = SqliteDatabase('challenges.db')

class Challenge(Model):
    name = CharField(max_length=100)
    language = CharField(max_length=100)
    steps = IntegerField(default=1)

    class Meta:
        database = db

def initialize():
    db.connect()
    db.create_tables([Challenge], safe=True)


# ============= Part 1 =============
# Task 1 of 2
# Import OrderedDict from the collections module.

## Menu Items:
# 'n', 'new challenge'
# 's', 'new step'
# 'd', 'delete a challenge'
# 'e', 'edit a challenge'

from collections import OrderedDict

# Task 2 of 2
# Now create an OrderedDict named menu that has the menu items exactly as listed in the comment. Both keys and values will be strings.

from collections import OrderedDict

menu = OrderedDict([
    ('n', 'new challenge'),
    ('s', 'new step'),
    ('d', 'delete a challenge'),
    ('e', 'edit a challenge')
])

