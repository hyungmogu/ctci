# ============= Part 1 =============
# Challenge Task 1 of 3
# We need to be able to view a single article. In articles/views.py, create a view named article_detail that takes a pk. The view should return the "articles/article_detail.html" template. Assign the Article to the article key in the context dictionary.

from django.shortcuts import render

from .models import Article, Writer


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})

def writer_detail(request, pk):
    writer = Writer.objects.get(pk=pk)
    return render(request, 'articles/writer_detail.html', {'writer': writer})


# Challenge Task 2 of 3
# Our view needs an URL. Add a new url to article/urls.py. The pattern should be "article/" and then the pk argument, which should be one or more digits.


#articles/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url (r'article/(?P<pk>\d+)/$',views.article_detail),
    url(r'writer/(?P<pk>\d+)/$', views.writer_detail),
    url(r'', views.article_list)
]

# Challenge Task 3 of 3
# Finally, we want to make sure we handle bad pks when looking up our Articles. Use get_object_or_404 to look up the Article. You'll need to import it from django.shortcuts.

from django.shortcuts import render, get_object_or_404

from .models import Article, Writer


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})

def writer_detail(request, pk):
    writer = Writer.objects.get(pk=pk)
    return render(request, 'articles/writer_detail.html', {'writer': writer})

# ============= Part 2 =============

# Challenge Task 1 of 1
# We need to be able to associate a Writer with an Article. Add a ForeignKey field to the Article model to link it to the Writer model. Give the attribute the name writer. IMPORTANT Since our Article model comes first, you'll need to quote the Writer model in the foreign key. So use "Writer" instead of Writer.

from django.db import models


class Article(models.Model):
    headline = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField()
    writer = models.ForeignKey("Writer")
    
    def __str__(self):
        return self.headline


class Writer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()

# ============= Part 3 =============
# Challenge Task 1 of 2
# I've added URL names for you but I need you to add the HTML markup for the links. Use the {% url %} tag to create the href attribute for the <a> tag. The URL name is articles_detail and you need to provide the pk from the Article as the pk argument.


{% extends 'base.html' %}
{% load static from staticfiles %}

{% block static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
{% endblock %}

{% block content %}
  {% for article in articles %}
  	<a href="{% url 'articles_detail' pk=article.pk %}">{{ article.headline }}</a>
  {% endfor %}
{% endblock %}

# Challenge Task 2 of 2
# It's probably better if we use namespaces. I've put all of the articles URLs into the "articles" namespace. Change your {% url %} tag to use "articles:detail" for the URL name.

{% extends 'base.html' %}
{% load static from staticfiles %}

{% block static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
{% endblock %}

{% block content %}
  {% for article in articles %}
  	<a href="{% url 'articles:detail' pk=article.pk %}">{{ article.headline }}</a>
  {% endfor %}
{% endblock %}



