#============= PART 1 ===============
# Challenge Task 1 of 2
# Creating products one at a time is getting tedious. I want to be able to make multiple at a time.
# In forms.py, create a model formset factory for the Digital model. Include the same fields as the DigitalProductForm. Name the factory DigitalFormset.


from django import forms

from . import models


class DigitalProductForm(forms.ModelForm):
    class Meta:
        model = models.Digital
        fields = ['name', 'description', 'url']

DigitalFormset = forms.modelformset_factory(
    models.Digital,
    form = DigitalProductForm
)


# Challenge Task 2 of 2
# Great! That's definitely going to help. Can you go one step further, though?

# I want to be able to make five (5) products at a time. Can you set extra and max_num to both be 5?


from django import forms

from . import models


class DigitalProductForm(forms.ModelForm):
    class Meta:
        model = models.Digital
        fields = ['name', 'description', 'url']

DigitalFormset = forms.modelformset_factory(
    models.Digital,
    form = DigitalProductForm,
    extra = 5,
    max_num = 5
)

#============= PART 2 ===============
# Challenge Task 1 of 1
# Now that we have a solid formset factory, we need to use it in a view.

# I've already set up a view, bulk_create_product, but it doesn't do anything on POST requests.

# Update the view so that POST requests, if valid, populate and save the formset. After saving, it should return a redirect to the URL named "products:bulk_create".
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms


def product_form(request):
    form = forms.DigitalProductForm()
    if request.method == 'POST':
        form = forms.DigitalProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products:create'))
    return render(request, 'products/product_form.html', {'form': form})


def bulk_create_products(request):
    formset = forms.DigitalFormset()
    if request.method == 'POST':
        formset = forms.DigitalFormset(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('products:bulk_create'))
    return render(request, 'products/bulk_create.html', {'formset': formset})

#============= PART 3 ===============


# Challenge Task 1 of 2
# I want to be able to create a Review in the same form as where I create a Product. That means I need an inline form!

# Create an inline model formset factory, named ReviewFormset, for the Review model. You need to include all the same fields as the existing ReviewForm.

# Remember, the first argument to the factory is the parent model (Product) and the second is the model the factory is for (Review).

from django import forms

from . import models
from products.models import Product


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ('headline', 'rating', 'content', 'writer', 'publish_date')

ReviewFormset = forms.inlineformset_factory(
    models.Product,
    models.Review,
    fields = ('headline', 'rating', 'content', 'writer', 'publish_date')
)


# Challenge Task 2 of 2
# Great! By default, I get 3 extra forms. That's a lot for a single view since they're big forms. Can you change it so I only get 1 extra?

from django import forms

from . import models
from products.models import Product


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ('headline', 'rating', 'content', 'writer', 'publish_date')

ReviewFormset = forms.inlineformset_factory(
    models.Product,
    models.Review,
    fields = ('headline', 'rating', 'content', 'writer', 'publish_date'),
    extra = 1
)
