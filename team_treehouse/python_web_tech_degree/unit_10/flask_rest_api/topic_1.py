# ============= Part 1 =============

# Challenge Task 1 of 2
# I need your help to build an API for creating recipes. I have the recipe model done but we need one to represent each of the ingredients in a recipe.
# Make a new Model named Ingredient. I've added comments to the models.py to describe the fields. Feel free to check the models and fields documenation if you need to. Don't forget to set the database attribute in the Meta class.
# Thanks!


import datetime

from peewee import *

DATABASE = SqliteDatabase('recipes.db')


class Recipe(Model):
    name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Ingredient(Model):
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    quantity = DecimalField()
    measurement_type = CharField(max_length=255)
    recipe = ForeignKeyField(Recipe)

    class Meta:
        database = DATABASE


# Challenge Task 2 of 2
# Thanks for making the model! Now, though, I need a resource created for it. Just create two Resource classes, IngredientList and Ingredient. Give them both a get method that just returns a string. You can put anything you want in the string. Remember, the get method for the Ingredient resource will need to take an id argument, too.


from flask.ext.restful import Resource

import models


class IngredientList(Resource):
    def get(self):
        return 'hello'

class Ingredient(Resource):
    def get(self, id):
        return 'hello'


# ============= Part 2 =============
# Challenge Task 1 of 4
# Great job on making the Ingredient model and resources. Now, though, of course, they need to be connected to Apis and turned into blueprints. I think you're the perfect person to do this for me!

# For this first step, import Blueprint from Flask and Api from Flask-RESTful in both resources/ingredients.py and resources/recipes.py.


#api.py
from flask import Flask

app = Flask(__name__)


if __name__ == '__main__':

    app.run()

#resources/ingredients.py
from flask import Blueprint
from flask.ext.restful import Resource, Api

import models


class IngredientList(Resource):
    def get(self):
        return 'IngredientList'


class Ingredient(Resource):
    def get(self, id):
        return 'Ingredient'

#resources/recipes.py

from flask import Blueprint
from flask.ext.restful import Resource, Api

import models


class RecipeList(Resource):
    def get(self):
        return 'RecipeList'


class Recipe(Resource):
    def get(self, id):
        return 'Recipe'


# Challenge Task 2 of 4
# Now I need you to make a Blueprint for each of the resources. Name the one in ingredients.py "ingredients_api" and the one in recipes.py "recipes_api".


#api.py
from flask import Flask

app = Flask(__name__)


if __name__ == '__main__':

    app.run()

#resources/ingredients.py
from flask import Blueprint
from flask.ext.restful import Resource, Api

import models


class IngredientList(Resource):
    def get(self):
        return 'IngredientList'


class Ingredient(Resource):
    def get(self, id):
        return 'Ingredient'

ingredients_api = Blueprint('resources.ingredients', __name__)

#resources/recipes.py

from flask import Blueprint
from flask.ext.restful import Resource, Api

import models


class RecipeList(Resource):
    def get(self):
        return 'RecipeList'


class Recipe(Resource):
    def get(self, id):
        return 'Recipe'


recipes_api = Blueprint('resources.recipes', __name__)


# Challenge Task 3 of 4
# Great! Now that we have the Blueprint, it's time to create the actual Api instance and register the resources for it.

# Create a new variable named api in each of the resources that's an Api instance for the Blueprint. Then add both of the Resources to api. You can use whatever endpoint name you want, but make sure the URL pattern is like "/api/v1/[PLURAL RESOURCE]". Remember to include the id argument in the appropriate URLs.



#api.py
from flask import Flask

app = Flask(__name__)


if __name__ == '__main__':

    app.run()

#resources/ingredients.py
from flask import Blueprint
from flask.ext.restful import Resource, Api

import models


class IngredientList(Resource):
    def get(self):
        return 'IngredientList'


class Ingredient(Resource):
    def get(self, id):
        return 'Ingredient'

ingredients_api = Blueprint('resources.ingredients', __name__)
api = Api(ingredients_api)
api.add_resource(
    IngredientList,
    '/api/v1/ingredients',
    endpoint='ingredients'
)
api.add_resource(
    Ingredient,
    '/api/v1/ingredients/<int:id>',
    endpoint='ingredient'
)

#resources/recipes.py

from flask import Blueprint
from flask.ext.restful import Resource, Api

import models


class RecipeList(Resource):
    def get(self):
        return 'RecipeList'


class Recipe(Resource):
    def get(self, id):
        return 'Recipe'


recipes_api = Blueprint('resources.recipes', __name__)
api = Api(recipes_api)
api.add_resource(
    RecipeList,
    '/api/v1/recipes',
    endpoint='recipes'
)
api.add_resource(
    Recipe,
    '/api/v1/recipes/<int:id>',
    endpoint='recipe'
)


# Challenge Task 4 of 4
# Alright, one last step! You need to import the blueprints into app.py and register them both with app.


#api.py

from flask import Flask
from resources.recipes import recipes_api
from resources.ingredients import ingredients_api

app = Flask(__name__)
app.register_blueprint(ingredients_api)
app.register_blueprint(recipes_api)

if __name__ == '__main__':
    app.run()


#resources/ingredients.py
from flask import Blueprint
from flask.ext.restful import Resource, Api

import models


class IngredientList(Resource):
    def get(self):
        return 'IngredientList'


class Ingredient(Resource):
    def get(self, id):
        return 'Ingredient'

ingredients_api = Blueprint('resources.ingredients', __name__)
api = Api(ingredients_api)
api.add_resource(
    IngredientList,
    '/api/v1/ingredients',
    endpoint='ingredients'
)
api.add_resource(
    Ingredient,
    '/api/v1/ingredients/<int:id>',
    endpoint='ingredient'
)


#resources/recipes.py

from flask import Blueprint
from flask.ext.restful import Resource, Api

import models


class RecipeList(Resource):
    def get(self):
        return 'RecipeList'


class Recipe(Resource):
    def get(self, id):
        return 'Recipe'


recipes_api = Blueprint('resources.recipes', __name__)
api = Api(recipes_api)
api.add_resource(
    RecipeList,
    '/api/v1/recipes',
    endpoint='recipes'
)
api.add_resource(
    Recipe,
    '/api/v1/recipes/<int:id>',
    endpoint='recipe'
)


# ============= Part 3 =============

# Challenge Task 1 of 1
# The API needs to be able to validate input from users. Use reqparse and add arguments for each field in the Ingredient model to the IngredientList resource. Remember to add the RequestParser instance to the resource instance as self.reqparse.

# name, description, and measurement_type should all be strings (the default)
# quantity should be a normal Python float
# recipe should be positive, which you'll get from inputs
# They should all be required and have their location set to ["form", "json"].


from flask import Blueprint

from flask.ext.restful import Resource, Api, reqparse, inputs, reqparse

import models


class IngredientList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=True,
            location=['form','json']
        )
        self.reqparse.add_argument(
            'description',
            required=True,
            location=['form','json']
        )
        self.reqparse.add_argument(
            'measurement_type',
            required=True,
            location=['form','json']
        )
        self.reqparse.add_argument(
            'quantity',
            required=True,
            location=['form','json'],
            type=float
        )
        self.reqparse.add_argument(
            'recipe',
            required=True,
            location=['form','json'],
            type=inputs.positive
        )
        super().__init__()

    def get(self):
        return 'IngredientList'


class Ingredient(Resource):
    def get(self, id):
        return 'Ingredient'

ingredients_api = Blueprint('resources.ingredients', __name__)
api = Api(ingredients_api)
api.add_resource(IngredientList, '/api/v1/ingredients')
api.add_resource(Ingredient, '/api/v1/ingredients/<int:id>')


# ============= Part 4 =============

# Challenge Task 1 of 2
# I've added code for the get and post methods in the IngredientList and the get method for Ingredient. But the resources still need their fields defined and to use marshal or marshal_with.

# For this step, just create the ingredient_fields dictionary with a key for each field. Make the recipe field a string for now. If you need help, check the fields documentation.


from flask import Blueprint

from flask.ext.restful import (
    Resource, Api, reqparse, inputs,
    marshal, marshal_with, fields
)

import models

ingredient_fields = {
    'name': fields.String,
    'description': fields.String,
    'measurement_type': fields.String,
    'quantity': fields.Float,
    'recipe': fields.String
}

class IngredientList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'description',
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'measurement_type',
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'quantity',
            type=float,
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'recipe',
            type=inputs.positive,
            required=True,
            location=['form', 'json']
        )
        super().__init__()

    def get(self):
        ingredients = models.Ingredient.select()
        return ingredients

    def post(self):
        args = self.reqparse.parse_args()
        ingredient = models.Ingredient.create(**args)
        return ingredient


class Ingredient(Resource):
    def __init__(self):
          self.reqparse = reqparse.RequestParser()
          self.reqparse.add_argument(
              'name',
              required=True,
              location=['form', 'json']
          )
          self.reqparse.add_argument(
              'description',
              required=True,
              location=['form', 'json']
          )
          self.reqparse.add_argument(
              'measurement_type',
              required=True,
              location=['form', 'json']
          )
          self.reqparse.add_argument(
              'quantity',
              type=float,
              required=True,
              location=['form', 'json']
          )
          self.reqparse.add_argument(
              'recipe',
              type=inputs.positive,
              required=True,
              location=['form', 'json']
          )
          super().__init__()

    def get(self, id):
        ingredient = models.Ingredient.get(models.Ingredient.id==id)
        return ingredient

ingredients_api = Blueprint('resources.ingredients', __name__)
api = Api(ingredients_api)
api.add_resource(IngredientList, '/api/v1/ingredients')
api.add_resource(Ingredient, '/api/v1/ingredients/<int:id>')


# Challenge Task 2 of 2
# Alright, now all of the methods need to be marshaled. Use marshal or marshal_with along with the ingredient_fields to make each method return a valid response. Make sure IngredientList.get returns a dictionary with a key named ingredients that holds all of the Ingredient instances.

# If you need a refresher, check the marshal docs.


from flask import Blueprint

from flask.ext.restful import (
    Resource, Api, reqparse, inputs,
    marshal, marshal_with, fields
)

import models

ingredient_fields = {
    'name': fields.String,
    'description': fields.String,
    'measurement_type': fields.String,
    'quantity': fields.Float,
    'recipe': fields.String
}

class IngredientList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'description',
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'measurement_type',
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'quantity',
            type=float,
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'recipe',
            type=inputs.positive,
            required=True,
            location=['form', 'json']
        )
        super().__init__()

    def get(self):
        output = [ marshal(ingredient,ingredient_fields) for ingredient in models.Ingredient.select()]
        return {'ingredients': output}

    @marshal_with(ingredient_fields)
    def post(self):
        args = self.reqparse.parse_args()
        ingredient = models.Ingredient.create(**args)

        return ingredient


class Ingredient(Resource):
    def __init__(self):
          self.reqparse = reqparse.RequestParser()
          self.reqparse.add_argument(
              'name',
              required=True,
              location=['form', 'json']
          )
          self.reqparse.add_argument(
              'description',
              required=True,
              location=['form', 'json']
          )
          self.reqparse.add_argument(
              'measurement_type',
              required=True,
              location=['form', 'json']
          )
          self.reqparse.add_argument(
              'quantity',
              type=float,
              required=True,
              location=['form', 'json']
          )
          self.reqparse.add_argument(
              'recipe',
              type=inputs.positive,
              required=True,
              location=['form', 'json']
          )
          super().__init__()

    @marshal_with(ingredient_fields)
    def get(self, id):
        ingredient = models.Ingredient.get(models.Ingredient.id==id)
        return ingredient

ingredients_api = Blueprint('resources.ingredients', __name__)
api = Api(ingredients_api)
api.add_resource(IngredientList, '/api/v1/ingredients')
api.add_resource(Ingredient, '/api/v1/ingredients/<int:id>')


# ============= Part 5 =============

# Challenge Task 1 of 1
# All of the methods are complete for the Recipe and RecipeList resources except for delete. It does the deletion but just sends back "Deleted!" which isn't very useful.

# Complete the method so that it sends back an empty response, the 204 status code, and a Location header with a URL for the RecipeList resource.
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