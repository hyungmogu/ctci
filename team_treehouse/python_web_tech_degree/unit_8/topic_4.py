# ============= Part 1 =============
# Challenge Task 1 of 1
# We've decided that we'd rather have review ratings be a scale of 1-10 instead of 1-5. That means, though, that we want to update all of our existing records so they accurately reflect the new scale.

# Write a function named double_ratings that uses .update() and an F object to double the current rating value for all of the existing Review objects.


from django.db.models import F

from . import models


def double_ratings():
    reviews = models.Review.objects.all().update(rating=F('rating')*2)

# ============= Part 2 =============
# Challenge Task 1 of 1
# Now that we have such a large range of reviews, we need to be more selective about the ones that we show. Can you update the product_detail view so that it only shows Reviews for the selected product if the Review has a rating of 8 or more or was created in the last 4 weeks? Oh, and don't change the ordering, we still want newest first.

import datetime

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from . import models


def good_reviews(request):
    reviews = models.Review.objects.filter(rating__gte=3)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def recent_reviews(request):
    six_months_ago = datetime.datetime.today() - datetime.timedelta(days=180)
    reviews = models.Review.objects.exclude(created_at__lt=six_months_ago)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def product_detail(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    four_weeks_ago = datetime.datetime.today() - datetime.timedelta(weeks=4)
    reviews = product.review_set.filter(Q(rating__gte=8)|Q(created_at__gte=four_weeks_ago)).order_by('-created_at')
    return render(request, 'products/product_detail.html', {'product': product, 'reviews': reviews})
# ============= Part 3 =============
# Challenge Task 1 of 1
# I think it's time to have a list view for all of our Products. I've created the URL and template for you and the beginnings of the view.

# I want the product_list view to list an average rating for each Product. Can you use annotate() and the Avg class (already imported) to add an annotation named avg_rating to the queryset? You'll use "review" instead of "review_set", by the way.
import datetime

from django.db.models import Q, Avg
from django.shortcuts import render, get_object_or_404

from . import models


def good_reviews(request):
    reviews = models.Review.objects.filter(rating__gte=3)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def recent_reviews(request):
    six_months_ago = datetime.datetime.today() - datetime.timedelta(days=180)
    reviews = models.Review.objects.exclude(created_at__lt=six_months_ago)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def product_detail(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    four_weeks_ago = datetime.datetime.today() - datetime.timedelta(weeks=4)
    reviews = product.review_set.filter(Q(rating__gte=8)|Q(created_at__gte=four_weeks_ago)).order_by('-created_at').all()
    return render(request, 'products/product_detail.html', {'product': product, 'reviews': reviews})


def product_list(request):
    products = models.Product.objects.all().annotate(
        avg_rating= Avg('review__rating')
    )
    return render(request, 'products/product_list.html', {'products': products})

# ============= Part 4 =============

# Challenge Task 1 of 1
# We're getting a lot of reviews! That's great! I'm worried, though, that our overall catalog isn't very well-rated.

# Update the current_average function to return the aggregate average rating for all Reviews. You should give it the key name of "average".

from django.db.models import Avg

from . import models


def current_average():
    reviews_avg = models.Review.objects.all().aggregate(
        average=Avg('rating')
    )

    return reviews_avg


# ============= Part 5 =============

# Challenge Task 1 of 2
# We can't stop the query in product_detail for the Reviews that belong to a Product, but we can move it up so it's done at the same time as fetching the product.

# First, though, change the product = get_object_or_404(...) to be a try and except combo that raises an Http404 exception if the Product doesn't exist.

import datetime

from django.db.models import Q, Avg
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from . import models


def good_reviews(request):
    reviews = models.Review.objects.filter(rating__gte=3)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def recent_reviews(request):
    six_months_ago = datetime.datetime.today() - datetime.timedelta(days=180)
    reviews = models.Review.objects.exclude(created_at__lt=six_months_ago)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def product_detail(request, pk):
    try:
        product = get_object_or_404(models.Product, pk=pk)
    except models.Product.DoesNotExist:
        raise Http404

    four_weeks_ago = datetime.datetime.today() - datetime.timedelta(weeks=4)
    reviews = product.review_set.filter(Q(rating__gte=8)|Q(created_at__gte=four_weeks_ago)).order_by('-created_at').all()

    return render(request, 'products/product_detail.html', {'product': product, 'reviews': reviews})


def product_list(request):
    products = models.Product.objects.annotate(avg_rating=Avg('review__rating')).all()
    return render(request, 'products/product_list.html', {'products': products})


# Challenge Task 2 of 2
# Great! Now, can you add the prefetch_related to the Product query? Make sure you fetch the "review_set" attribute.

import datetime

from django.db.models import Q, Avg
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from . import models


def good_reviews(request):
    reviews = models.Review.objects.filter(rating__gte=3)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def recent_reviews(request):
    six_months_ago = datetime.datetime.today() - datetime.timedelta(days=180)
    reviews = models.Review.objects.exclude(created_at__lt=six_months_ago)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def product_detail(request, pk):
    try:
        product = models.Product.objects.prefetch_related('review_set').get(pk=pk)
    except models.Product.DoesNotExist:
        raise Http404

    four_weeks_ago = datetime.datetime.today() - datetime.timedelta(weeks=4)
    reviews = product.review_set.filter(Q(rating__gte=8)|Q(created_at__gte=four_weeks_ago)).order_by('-created_at').all()

    return render(request, 'products/product_detail.html', {'product': product, 'reviews': reviews})


def product_list(request):
    products = models.Product.objects.annotate(avg_rating=Avg('review__rating')).all()
    return render(request, 'products/product_list.html', {'products': products})


# ============= Part 6 =============

# Challenge Task 1 of 1
# The view for an individual Review always has to talk about the Product that it relates to. This means we have to do at least two queries, one for the Review and one for the Product.

# Can you use select_related on the review_detail view to get the Product at the same time and reduce our queries to 1?

import datetime

from django.db.models import Q, Avg
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from . import models


def good_reviews(request):
    reviews = models.Review.objects.filter(rating__gte=3)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def recent_reviews(request):
    six_months_ago = datetime.datetime.today() - datetime.timedelta(days=180)
    reviews = models.Review.objects.exclude(created_at__lt=six_months_ago)
    return render(request, 'products/reviews.html', {'reviews': reviews})


def product_detail(request, pk):
    try:
        product = models.Product.objects.prefetch_related('review_set').get(pk=pk)
    except models.Product.DoesNotExist:
        raise Http404()
    four_weeks_ago = datetime.datetime.today() - datetime.timedelta(weeks=4)
    reviews = product.review_set.filter(Q(rating__gte=8)|Q(created_at__gte=four_weeks_ago)).order_by('-created_at').all()
    return render(request, 'products/product_detail.html', {'product': product, 'reviews': reviews})


def product_list(request):
    products = models.Product.objects.annotate(avg_rating=Avg('review__rating')).all()
    return render(request, 'products/product_list.html', {'products': products})


def review_detail(request, product_pk, pk):
    try:
        review = models.Review.objects.select_related('product').get(product_id=product_pk, pk=pk)
    except models.Review.DoesNotExist:
        raise Http404()
    else:
        return render(request, 'products/review_detail.html', {'review': review})