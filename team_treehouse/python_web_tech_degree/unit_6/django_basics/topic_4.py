# ============= Part 1 =============

# Challenge Task 1 of 1
# Use a {% for %} loop to print the headline attribute for each item in the articles queryset.

{% for item in articles %}
	{{item.headline}}
{% endfor %}

# ============= Part 2 =============

# Challenge Task 1 of 2
# We want to use our base.html template. Please add an {% extends %} tag to the article_list.html template.

{% extends "base.html" %}

{% for article in articles %}
{{ article.headline }}
{% endfor %}

# Challenge Task 2 of 2
# Now put the existing contents of article_list.html, the {% for %} loop, into the block "content".

{% extends "base.html" %}

{% block content %}
{% for article in articles %}
{{ article.headline }}
{% endfor %}
{% endblock %}

# ============= Part 3 =============

# Challenge Task 1 of 2
# We want to use some static files in our project and we want to use the {% static %} tag. To do that, we have to load this special tag. Use the {% load %} tag to load static from the staticfiles library.
{% extends 'base.html' %}
{% load static from staticfiles %}


{% block static %}
<link rel="stylesheet" href="">
{% endblock %}

{% block content %}
{% for article in articles %}
{{ article.headline }}
{% endfor %}
{% endblock %}

# Challenge Task 2 of 2
# Now that we have the tag available, we can use it in our <link> tag. Use {% static %} to reference the "css/styles.css" file in the href attribute of the <link> tag.

{% extends 'base.html' %}
{% load static from staticfiles %}


{% block static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
{% endblock %}

{% block content %}
{% for article in articles %}
{{ article.headline }}
{% endfor %}
{% endblock %}

# ============= Part 4 =============

# Challenge Task 1 of 3
# Add a new model, Writer, and give it a name attribute that's a CharField with a max_length of 255.

from django.db import models


class Writer (models.Model):
    name = models.CharField(max_length=255)


class Article(models.Model):
    headline = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.headline



# Challenge Task 2 of 3
# We want people to be able to email our writers, so each one needs an email address, too. Add an email attribute to the model. It should be an EmailField and doesn't need any arguments.

from django.db import models


class Writer (models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()


class Article(models.Model):
    headline = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.headline

# Challenge Task 3 of 3
# Finally, we want our writers to have a biography that we can show. Add a TextField to the model with a name of bio.

from django.db import models


class Writer (models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    bio= models.TextField()


class Article(models.Model):
    headline = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.headline


# ============= Part 5 =============

# Challenge Task 1 of 2
# We need to add a view to see the details on a specific Writer. To start, we should import the Writer model.


from django.shortcuts import render

from .models import (Article,Writer)


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})


# Challenge Task 2 of 2
# Now we need to create the view. I've already made the URL and template for you.

# Create a view named writer_detail that takes a pk argument. It should .get() the Writer with the requested pk and render() the "articles/writer_detail.html" template. Provide the Writer in the context as "writer".

from django.shortcuts import render

from .models import (Article,Writer)


def writer_detail(request, pk):
    writer = Writer.objects.get(pk=pk)
    return render(request, "articles/writer_detail.html", {'writer': writer})

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})