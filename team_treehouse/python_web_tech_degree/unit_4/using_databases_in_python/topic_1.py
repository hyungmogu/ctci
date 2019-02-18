# ============= Part 1 =============
# Task 1 of 4
# Import everything from the peewee library.

from peewee import *

# Task 2 of 4
# Now we need to make a database connection. Make an SqliteDatabase() named "challenges.db". Assign it to the variable db.

from peewee import *

db = SqliteDatabase('challenges.db')

# Task 3 of 4
# Alright, now for the biggest part. Make a model named Challenge that has two fields, name and language. Both fields should be of the type CharField with a max_length of 100.

from peewee import *

db = SqliteDatabase('challenges.db')

class Challenge(Model):
    name = CharField(max_length=100)
    language = CharField(max_length=100)


# Task 4 of 4
# Now add a Meta class to Challenge and set the database attribute equal to db.

from peewee import *

db = SqliteDatabase('challenges.db')

class Challenge(Model):
    name = CharField(max_length=100)
    language = CharField(max_length=100)

    class Meta:
        database = db


# ============= Part 2 =============

# Task 1 of 4
# Import the Challenge class from models.py.

from models import Challenge

# Task 2 of 4
# Now, create a variable named all_challenges. It should select all of the available challenges from the database.

from models import Challenge

all_challenges = Challenge.select()

# Task 3 of 4
# Next, create a new Challenge. The language should be "Ruby", the name should be "Booleans".

from models import Challenge

all_challenges = Challenge.select()

Challenge.create(language="Ruby",name="Booleans")