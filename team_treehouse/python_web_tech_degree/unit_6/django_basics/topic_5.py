# ============= Part 1 =============
# Challenge Task 1 of 2
# We need to test that our Writer model's creation works like we want it to. First, though, we need to import the model from our models.py file. Add that import, please.

#articles/test.py
from django.test import TestCase
from .models import Writer


class WriterModelTestCase(TestCase):
    '''Tests for the Writer model'''


#articles/models.py
from django.db import models


class Article(models.Model):
    headline = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField()
    writer = models.ForeignKey('Writer')

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

# Challenge Task 2 of 2
# Now add a test that creates an instance of the Writer model and, using self.assertIn, make sure the email attribute is in the output of the mailto() method.


#articles/test.py
from django.test import TestCase
from .models import Writer


class WriterModelTestCase(TestCase):
    def test_mailto(self):
        writer = Writer.objects.create(
            name = "Hyungmo Gu",
            email = "helloworld@test.com",
            bio = "Test"
        )
        self.assertIn(writer.email, writer.mailto())



#articles/models.py
from django.db import models


class Article(models.Model):
    headline = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField()
    writer = models.ForeignKey('Writer')

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

# ============= Part 2 =============
# Challenge Task 1 of 1
# We want to be sure that our article_list view returns all of our articles. Add a test to the ArticleListViewTestCase that uses assertIn to make sure that self.article is in the "articles" context dict key when you use self.client.get() to get the list view. The route name is "articles:list".

import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Article, Writer

class ArticleListViewTestCase(TestCase):
    '''Tests for the Article list view'''

    def setUp(self):
        self.writer = Writer.objects.create(
            name='Kenneth Love',
            email='kenneth@teamtreehouse.com',
            bio='Your friendly, local Python teacher'
        )
        self.article = Article.objects.create(
          writer=self.writer,
          headline='Article 0',
          content='Something about 0',
          publish_date=datetime.datetime.today()
        )
        for x in range(1, 3):
            Article.objects.create(
                writer=self.writer,
                headline='Article {}'.format(x),
                content='Something about {}'.format(x),
                publish_date=datetime.datetime.today()
            )
    def test_view_test(self):
        resp = self.client.get(reverse('articles:list'))
        self.assertIn(self.article, resp.context['articles'])

# ============= Part 3 =============
# Challenge Task 1 of 2
# I've created two test stubs for you. Finish the test_detail_template test by using assertTemplateUsed to check that the correct template is used when you get() the articles:detail URL. Remember to pass the pk of self.article when you use reverse!

import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Article, Writer

class ArticleDetailViewTestCase(TestCase):
    '''Tests for the Article detail view'''

    def setUp(self):
        self.writer = Writer.objects.create(
            name='Kenneth Love',
            email='kenneth@teamtreehouse.com',
            bio='Your friendly, local Python teacher'
        )
        self.article = Article.objects.create(
          writer=self.writer,
          headline='Article 0',
          content='Something about 0',
          publish_date=datetime.datetime.today()
        )

    def test_detail_template(self):
        '''Make sure the `articles/article_detail.html` template is used'''
        resp = self.client.get(reverse('articles:detail', kwargs = {'pk': self.article.pk}))
        self.assertTemplateUsed(resp, 'articles/article_detail.html')
    def test_detail_template_writer(self):
        '''Make sure the article writer's name is in the rendered output'''


# Challenge Task 2 of 2
# For the second test, use assertContains() to make sure the response contains the name value of self.article.writer.

import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Article, Writer

class ArticleDetailViewTestCase(TestCase):
    '''Tests for the Article detail view'''

    def setUp(self):
        self.writer = Writer.objects.create(
            name='Kenneth Love',
            email='kenneth@teamtreehouse.com',
            bio='Your friendly, local Python teacher'
        )
        self.article = Article.objects.create(
          writer=self.writer,
          headline='Article 0',
          content='Something about 0',
          publish_date=datetime.datetime.today()
        )

    def test_detail_template(self):
        '''Make sure the `articles/article_detail.html` template is used'''
        resp = self.client.get(reverse('articles:detail', kwargs = {'pk': self.article.pk}))
        self.assertTemplateUsed(resp, 'articles/article_detail.html')
    def test_detail_template_writer(self):
        resp = self.client.get(reverse('articles:detail', kwargs = {'pk': self.article.pk}))
        self.assertContains(resp, self.article.writer.name)



# ============= Part 4 =============


#karaoke/songs/views.py
from django.shortcuts import render, get_object_or_404

from .models import Song, Performer

def song_list(request):
  songs = Song.objects.all()
  return render(request, 'songs/song_list.html', {'songs': songs})


def song_detail(request, pk):
  song = get_object_or_404(Song, pk=pk)
  return render(request, 'songs/song_detail.html', {'song': song})

def performer_detail(request, pk):
  performer = get_object_or_404(Performer, pk=pk)
  songs = performer.song_set.all()
  return render(request, 'songs/performer_detail.html', {'performer': performer, 'songs': songs})


#karaoke/songs/models.py
from django.db import models

# Write your models here
class Performer(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Song(models.Model):
  title= models.CharField(max_length=255)
  artist=models.CharField(max_length=255)
  length= models.IntegerField(default=0)
  performer= models.ForeignKey(Performer)

  def __str__(self):
    return "{0} - {1}".format(self.title, self.artist)


#karaoke/templates/songs/performer_detail.html
{% extends 'base.html' %}

{%block title%}{{ performer.name }}{% endblock %}

{% block content %}
  <h1>{{ performer.name }}</h1>

  {% for song in songs %}
    <div>{{ song.title }} - {{ song.artist }}</div>
  {% endfor %}
{% endblock %}

#karaoke/templates/songs/song_detail.html
{% extends 'base.html' %}

{%block title%}{{ song.title }}{% endblock %}

{% block content %}
  <h1>{{ song.title }}</h1>
  <div>{{ song.artist }}</div>
  <div>{{ song.length }}</div>
  <div>{{ song.performer.name }}</div>
{% endblock %}

#karaoke/templates/songs/song_list.html
{% extends 'base.html' %}

{% block content %}
  {% for song in songs %}
    <h1>{{ song.title }}</h1>
    <div>{{ song.artist }}</div>
    <div>{{ song.length }}</div>
    <div>{{ song.performer.name }}</div>
  {% endfor %}
{% endblock %}