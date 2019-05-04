# ============= Part 1 =============
# Challenge Task 1 of 3
# Create a model named Article that has a headline attribute. Article.headline should be a CharField with a max_length of 255.

#articles/models.py
from django.db import models


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=255)


# Challenge Task 2 of 3
# Now add another field to the Article model named publish_date. It should be a DateTimeField and have no arguments.

#articles/models.py
from django.db import models

class Article(models.Model):
    publish_date = models.DateTimeField()
    headline = models.CharField(max_length=255)


# Challenge Task 3 of 3
# Finally, add a third field, content. This field should be a TextField() and shouldn't have any arguments.

#articles/models.py
from django.db import models

class Article(models.Model):
    publish_date = models.DateTimeField()
    headline = models.CharField(max_length=255)
    content = models.TextField()


# ============= Part 2 =============
# Challenge Task 1 of 1
# Add a __str__ method to the model that returns the model's headline attribute.

from django.db import models

# Create your models here
class Article(models.Model):
    headline = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.headline


# ============= Part 3 =============
# Challenge Task 1 of 2
# First, we need to import our Article model from models.py. Remember to use .models to reference the models module in the current app.

#articles/views.py
from django.http import HttpResponse

from .models import Article
# Write your views here


# Challenge Task 2 of 2
# Now, create a view named article_list that selects all Article instances and returns an HttpResponse like "There are 5 articles." Be sure to use the len() of the Article queryset to get the number of articles.

from django.http import HttpResponse

from .models import Article
# Write your views here

def article_list(request):
    articles = Article.objects.all()
    output = "There are {0} articles".format(len(articles))
    return HttpResponse(output)


# ============= Part 4 =============
# Challenge Task 1 of 2
# Before we can register our model, we need to import it. Import Article from models.py in the same directory.

# admin.py
from django.contrib import admin

from .models import Article


# Challenge Task 2 of 2
# Now, use admin.site.register() to register the Article model with the admin site.

# admin.py
from django.contrib import admin

from .models import Article

admin.site.register(Article)