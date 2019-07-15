# ============= Part 1 =============
# Challenge Task 1 of 1
# We're getting a lot of reviews in the system. That's great but we need to be able to show users just the products with decent ratings. Fill out good_reviews so it returns a QuerySet of Review objects where the rating is 3 or higher. You'll use the gte field lookup for "greater than or equal to". Make sure to provide the Reviews to the template as "reviews" in the context dictionary.

from django.shortcuts import render

from . import models

def good_reviews(request):
    reviews = models.Review.objects.filter(rating__gte=3)
    return render(request, 'products/reviews.html', {'reviews': reviews})

# ============= Part 2 =============
# Challenge Task 1 of 2
# Users love our "good reviews" feature but they want to be able to see only recent features, too. Let's add that!

# First, import the datetime library at the top of products/views.py.

from django.shortcuts import render
import datetime
from . import models


def good_reviews(request):
    reviews = models.Review.objects.filter(rating__gte=3)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def recent_reviews(request):
    return render(request, 'products/reviews.html', {'reviews': None})


# Challenge Task 2 of 2
# Alright, now we can compare dates.

# In the recent_reviews view, use datetime.datetime.today() and a datetime.timedelta to get a new datetime of 180 days ago. Then use that datetime to .exclude() of the Review records with a created_at that is less than it.

from django.shortcuts import render
import datetime
from . import models


def good_reviews(request):
    reviews = models.Review.objects.filter(rating__gte=3)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def recent_reviews(request):
    temp_time = datetime.datetime.today() - datetime.timedelta(days=180)
    reviews = models.Review.objects.exclude(created_at__lt=temp_time)
    return render(request, 'products/reviews.html', {'reviews': reviews})
