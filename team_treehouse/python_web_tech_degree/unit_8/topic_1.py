# ============= Part 1 =============
# Challenge Task 1 of 3
# We're building a pretty good list of products but we need to start collecting reviews. Can you create a Review model for me? To start with, give it a single field, rating, that is an IntegerField.

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField(default='')
    price = models.DecimalField()

    def __str__(self):
        return self.name

class Review(models.Model):
    rating = models.IntegerField()


# Challenge Task 2 of 3
# Great! Now we need to add a link between the Review model and the Product model. Add a new field to Review, named product, that is a ForeignKey to the Product model.


from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField(default='')
    price = models.DecimalField()

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product)
    rating = models.IntegerField()


# Challenge Task 3 of 3
# Alright, almost done! Our model only needs two more fields.
# Add a created_at field that is a DateTimeField with auto_now_add set to True.
# Then, add a comment field that is a TextField. It should have an empty string for its default.

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField(default='')
    price = models.DecimalField()

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(default='')
