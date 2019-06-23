#============= PART 1 ===============

# Challenge Task 1 of 1
# We need to make a model form for our Digital product model. We have a couple of fields on Product, its parent, though, that we don't want in our form.

#Make a model form for Digital and name the form class DigitalProductForm. Only include the name, description, and url fields.


from django import forms

from . import models

class DigitalProductForm(forms.ModelForm):
    class Meta:
        model = models.Digital
        fields = [
            'name',
            'description',
            'url'
        ]
        
#============= PART 2 ===============

#Challenge Task 1 of 2
#We've made models and model forms, now we need a view to render the form.

#Write a new view named product_form that instantiates the DigitalProductForm and provides it to the products/product_form.html template as the key "form".
 

# products/views.py
from django.shortcuts import render

from . import forms


def product_form(request):
    form = forms.DigitalProductForm()
    
    return render(request, 'products/product_form.html', {'form': form})


# products/templates/products/product_form.html
<form action='' method='POST'>
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>

# Challenge Task 2 of 2
# Great! Now we need to use the form in our template. Add the CSRF token template tag and then print out our form as either paragraphs (as_p), list items (as_ul), or a table (as_table).

# products/views.py
from django.shortcuts import render

from . import forms


def product_form(request):
    form = forms.DigitalProductForm()
    
    return render(request, 'products/product_form.html', {'form': form})


# products/templates/products/product_form.html
<form action='' method='POST'>
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>


#============= PART 3 ===============

# Challenge Task 1 of 1
# OK, now we need to make the view handle saving a new Digital instance. I'm sure you can do this on your own, but if you need a guide, here are the basic steps:

# 1.Check request.method
# 2.Instantiate a new form with request.POST
# 3.Check if the new form is valid
# 4.form.save()
# 5.Return an HTTP redirect to "products:create"

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms

def product_form(request):
    form_class = forms.DigitalProductForm
    form = form_class()
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products:create'))
    return render(request, 'products/product_form.html', {'form': form})

