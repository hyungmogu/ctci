#============= PART 1 ===============

# Challenge Task 1 of 2
# We want to have multiple types of Articles so we need to make our existing 
# Article model abstract. Can you do that for me?

from django.db import models


class Article(models.Model):
    headline = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField()
    writer = models.ForeignKey('Writer')
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.headline


class Writer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()
    
    def __str__(self):
        return self.name
      
    def mailto(self):
        return '{} <{}>'.format(self.name, self.email)
    

#Challenge Task 2 of 2
#Great! Now make a new model, Review, that inherits from Article. It should have one new field, rating, which is an IntegerField with a default value of 5.

from django.db import models


class Article(models.Model):
    headline = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField()
    writer = models.ForeignKey('Writer')
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.headline


class Review(Article):
    rating = models.IntegerField(default=5)
    
    
class Writer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()
    
    def __str__(self):
        return self.name
      
    def mailto(self):
        return '{} <{}>'.format(self.name, self.email)

    
#============= PART 2 ===============
# Challenge Task 1 of 2
# Alright, let's start setting up our products models. I want a Product model to start with, so make that, please.
#
# Give your Product model a name field that should be a CharField with a max_length of 255.
#
# Also give it a description field that is a TextField.

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    
# Challenge Task 2 of 2
# Amazing! OK, now let's add models for our Digital products.
#
# Make a new model, Digital, that inherits from Product. Add a new field to it, url, that is an URLField.

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        abstract = True
        
class Digital(Product):
    url = models.URLField()
