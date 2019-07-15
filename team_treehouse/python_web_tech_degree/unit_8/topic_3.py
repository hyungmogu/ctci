# ============= Part 1 =============

# Challenge Task 1 of 1
# We're starting to get a lot of advertisement spam in our reviews. We're going to implement a better solution later, but for now, write a function named can_spam that selects all of the Reviews where the comment field contains the string "http" and then delete them.

from . import models

def can_spam():
    reviews = models.Review.objects.filter(comment__icontains='http')
    reviews.delete()


# ============= Part 2 =============

# Challenge Task 1 of 1
# Oh no!

# We accidentally deleted a few product reviews and need to get them back. And, wouldn't you know it? It happened between backups. We have a couple of logs, though, so we know the rating just not the comments. It's not ideal but it'll have to do.

# In a function named fix_25, can you use the bulk_create method to make three Reviews for the Product with an id of 1? They should have ratings of 2, 3, and 5. Thanks!

from . import models

def fix_25():
    item = models.Product.objects.get(id=1)
    models.Review.objects.bulk_create([
        models.Review(product=item,rating=2),
        models.Review(product=item,rating=3),
        models.Review(product=item,rating=5)
    ])



# ============= Part 3 =============

# Challenge Task 1 of 1
# We have a view for showing a product, product_detail, but it currently shows the Reviews in the order they were created. I'd rather show them newest-first, though. Can you use order_by to sort them by created_at in descending order?

import datetime

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
    reviews = product.review_set.all().order_by('-created_at')
    return render(request, 'products/product_detail.html', {'product': product, 'reviews': reviews})