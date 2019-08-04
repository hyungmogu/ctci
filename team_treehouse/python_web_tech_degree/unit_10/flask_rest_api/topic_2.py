# ============= Part 1 =============
# Challenge Task 1 of 3
# When users sign up, we want to be sure and hash their passwords securely. We'll use argon2 for this.

# Import the PasswordHasher class from argon2 and then make a new variable, HASHER that's an instantiation of that class.

import datetime
from argon2 import PasswordHasher

from peewee import *

DATABASE = SqliteDatabase('recipes.db')

HASHER = PasswordHasher()

class User(Model):
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls, username, password):
        try:
            cls.get(cls.username**username)
        except cls.DoesNotExist:
            user = cls(username=username)
            # TODO: hash user password here?
            user.save()
            return user
        else:
            raise Exception("User already exists")


class Recipe(Model):
    name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


class Ingredient(Model):
    name = CharField()
    description = CharField()
    quantity = DecimalField()
    measurement_type = CharField()
    recipe = ForeignKeyField(Recipe)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Recipe, Ingredient], safe=True)
    DATABASE.close()


# Challenge Task 2 of 3
# Great! Now, add a staticmethod to User that returns a hashed password. Name it hash_password and have it take a single argument, the password to hash.

# Hash the password using HASHER's 'hash' method and return it.

import datetime
from argon2 import PasswordHasher

from peewee import *

DATABASE = SqliteDatabase('recipes.db')

HASHER = PasswordHasher()

class User(Model):
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE

    @staticmethod
    def hash_password(password):
        return HASHER.hash(password)

    @classmethod
    def create_user(cls, username, password):
        try:
            cls.get(cls.username**username)
        except cls.DoesNotExist:
            user = cls(username=username)
            # TODO: hash user password here?
            user.save()
            return user
        else:
            raise Exception("User already exists")


class Recipe(Model):
    name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


class Ingredient(Model):
    name = CharField()
    description = CharField()
    quantity = DecimalField()
    measurement_type = CharField()
    recipe = ForeignKeyField(Recipe)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Recipe, Ingredient], safe=True)
    DATABASE.close()


# Challenge Task 3 of 3
# Almost done!

# Now I need you to update the create_user method so that it sets the User instance's password using the User.hash_password method you just created. You should see the TODO for where to add this.

import datetime
from argon2 import PasswordHasher

from peewee import *

DATABASE = SqliteDatabase('recipes.db')

HASHER = PasswordHasher()

class User(Model):
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE

    @staticmethod
    def hash_password(password):
        return HASHER.hash(password)

    @classmethod
    def create_user(cls, username, password):
        try:
            cls.get(cls.username**username)
        except cls.DoesNotExist:
            user = cls(username=username)
            # TODO: hash user password here?
            user.password = User.hash_password(password)
            user.save()
            return user
        else:
            raise Exception("User already exists")


class Recipe(Model):
    name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


class Ingredient(Model):
    name = CharField()
    description = CharField()
    quantity = DecimalField()
    measurement_type = CharField()
    recipe = ForeignKeyField(Recipe)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Recipe, Ingredient], safe=True)
    DATABASE.close()


#============= PART 2 ===============

# Challenge Task 1 of 2
# I've set up most of a User resource for you but I want you to finish it.

# Add two new requirements to the RequestParser for "password" and "confirm_password". Both should be required and in either "form" or "json" locations.


from flask import Blueprint

from flask.ext.restful import Resource, Api, reqparse, marshal_with, fields

import models

user_fields = {
    'username': fields.String
}


class UserList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'password',
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'confirm_password',
            required=True,
            location=['form', 'json']
        )
        super().__init__()

    @marshal_with(user_fields)
    def post(self):
        args = self.reqparse.parse_args()
        user = models.User.create(**args)
        return user, 201


users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(UserList, '/api/v1/users')



# Challenge Task 2 of 2
# Now, inside of UserList.post, check that the "password" and "confirm_password" args are equal to each other. If they're not, raise an Exception. If they are equivalent, go ahead and create the user and send it back.


from flask import Blueprint

from flask.ext.restful import Resource, Api, reqparse, marshal_with, fields

import models

user_fields = {
    'username': fields.String
}


class UserList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'password',
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'confirm_password',
            required=True,
            location=['form', 'json']
        )
        super().__init__()

    def post(self):
        args = self.reqparse.parse_args()
        if args.get('password') == args.get('confirm_password'):
            user = models.User.create(**args)
            return marshal(user, userfields), 201
        else:
            raise Exception




users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(UserList, '/api/v1/users')
