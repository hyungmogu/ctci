# ============= Part 1 =============

# Challenge Task 1 of 3
# Import everything from the Peewee library. Create a new model named User. Give User an email attribute that is a CharField(). email should be unique.


from peewee import *

class User(Model):
    email = CharField(unique=True)


# Challenge Task 2 of 3
# Now add two more attributes/fields to User. The password field should be a CharField with a max_length of 100. And the join_date field should be a DateTimeField with a default value of datetime.datetime.now.

import datetime

from peewee import *

class User(Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)


# Challenge Task 3 of 3
# Finally, add a last field named bio that is a TextField. It should have an empty string for its default value. This makes it optional.

import datetime

from peewee import *

class User(Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = TextField(default='')


# ============= Part 2 =============

# Challenge Task 1 of 2
# Import the UserMixin from Flask-Login. Remember that Flask extensions usually have import paths that start with flask.ext.

import datetime

from peewee import *
from flask.ext.login import UserMixin

class User(Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = TextField(default='')


# Challenge Task 2 of 2
# Now add UserMixin to the inheritance chain of the User model.

import datetime

from peewee import *
from flask.ext.login import UserMixin

class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = TextField(default='')


# ============= Part 3 =============
# Challenge Task 1 of 3
# Import both generate_password_hash and check_password_hash from Flask-Bcrypt.


from flask.ext.bcrypt import generate_password_hash, check_password_hash


# Challenge Task 2 of 3
# Now create a function named set_password that takes a User and a string for their password. Hash the password, set the User.password attribute to the hashed password, and return the User.

from flask.ext.bcrypt import generate_password_hash, check_password_hash

def set_password(User, password):
    User.password = generate_password_hash(password)
    return User


# Challenge Task 3 of 3
# Finally write a function named validate_password that takes a user and a password. It should return True if the provided password, when hashed, matches the user's password. Otherwise, return False.

from flask.ext.bcrypt import generate_password_hash, check_password_hash

def set_password(User, password):
    User.password = generate_password_hash(password)
    return User

def validate_password(User, password):
    return True if check_password_hash(User.password, password) else False



# ============= Part 4 =============

# Challenge Task 1 of 2
# Add a @classmethod to User named new. It should take two arguments, email and password. The body of the method can be pass for now. Remember, @classmethods take cls as the first argument.

import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

database = SqliteDatabase(':memory:')

class User(Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = CharField(default='')

    class Meta:
        database = database

    @classmethod
    def new(cls, email,password):
        pass

# Challenge Task 2 of 2
# Now, replace the pass in your method with a cls.create() call, using the provided email and a hash of the password.


import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

database = SqliteDatabase(':memory:')

class User(Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = CharField(default='')

    class Meta:
        database = database

    @classmethod
    def new(cls, email,password):
        cls.create(
            email = email,
            password = generate_password_hash(password)
        )