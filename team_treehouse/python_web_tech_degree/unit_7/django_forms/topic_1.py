# ============= Part 1 =============
# Challenge Task 1 of 4
# If we're going to make a form, we need to import the forms library. Add an import to the top of the forms.py file to import forms from django.

from django import forms


# Challenge Task 2 of 4
# Now create a new class named LeadShareForm that inherits from forms.Form. Just put pass as the body of the class for now.

from django import forms

class LeadShareForm(forms.Form):
    pass


# Challenge Task 3 of 4
# Great! Delete the pass and add an email field to the form. It should be of the type EmailField. It doesn't need any attributes.

from django import forms

class LeadShareForm(forms.Form):
    email = forms.EmailField()


# Challenge Task 4 of 4
# Let's add one more field to the form. Add a new field named link that is an URLField. Again, we don't need any attributes for now.

from django import forms

class LeadShareForm(forms.Form):
    email = forms.EmailField()
    link = forms.URLField()



# ============= Part 2 =============
# Challenge Task 1 of 3
# Now we need to instantiate and show a form to our users. Before we can do that, though, we have to import our forms. Add an import to views.py for the forms module in the same directory.


from django.shortcuts import render

from . import forms


def lead_form(request):
    return render(request, 'lead_form.html')


# Challenge Task 2 of 3
# Now we need to instantiate the form in our view. Inside of lead_form, create an instance of LeadShareForm. Assign it to the variable form.

from django.shortcuts import render

from . import forms

def lead_form(request):
    form = forms.LeadShareForm()
    return render(request, 'lead_form.html')


# Challenge Task 3 of 3
# One last step, we need to send the form out to the template. Add a context dictionary to our render() call and include form as the key "form".

from django.shortcuts import render

from . import forms

def lead_form(request):
    form = forms.LeadShareForm()
    return render(request, 'lead_form.html', {'form': form})

# ============= Part 3 =============
# Challenge Task 1 of 2
# OK, I need you to do a couple of things. In lead_form, check that the request's method is a POST. If it is, make a new LeadShareForm with the request.POST data and make sure that form is valid. And, if that's all good, return an HttpResponseRedirect. Use reverse to find the URL for "lead".

from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms


def send_lead(email, url):
    send_mail(
        'Lead from {}'.format(email),
        '{} submitted {}'.format(email, url),
        email,
        ['kenneth@teamtreehouse.com']
    )


def lead_form(request):
    form = forms.LeadShareForm()
    if request.method == 'POST':
        form = forms.LeadShareForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('lead'))
    return render(request, 'lead_form.html', {'form': form})


# Challenge Task 2 of 2
# Alright, so let's make this useful. If the POSTed data is valid (so the form is valid), use send_lead to send an email. You can get email and url from form.cleaned_data but, remember, we named the URL field "link". Leave everything else alone.

from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms


def send_lead(email, url):
    send_mail(
        'Lead from {}'.format(email),
        '{} submitted {}'.format(email, url),
        email,
        ['kenneth@teamtreehouse.com']
    )


def lead_form(request):
    form = forms.LeadShareForm()
    if request.method == 'POST':
        form = forms.LeadShareForm(request.POST)
        if form.is_valid():
            send_lead(form.cleaned_data, form.cleaned_data['link'])
            return HttpResponseRedirect(reverse('lead'))
    return render(request, 'lead_form.html', {'form': form})

# ============= Part 4 =============
# Challenge Task 1 of 2
# Like we did in the video, let's add a honeypot field to our LeadShareForm form. Add a new field named honeypot. It should be CharField and have it's widget set to forms.HiddenInput. You should also set required to False.

from django import forms


class LeadShareForm(forms.Form):
    email = forms.EmailField()
    link = forms.URLField()
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

# Challenge Task 2 of 2
# Great job! Now we need to add a clean_honeypot method to our class. It should only take self as an argument. You can get the value in honeypot from self.cleaned_data (which acts like a dict). You should raise forms.ValidationError if honeypot has a length. Otherwise, just return honeypot. Your error message can be anything you want.


from django import forms


class LeadShareForm(forms.Form):
    email = forms.EmailField()
    link = forms.URLField()
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_honeypot(self):
        honey_pot = self.cleaned_data['honeypot']
        if len(honey_pot):
            raise forms.ValidationError('Must be left empty.')

        return honey_pot

# ============= Part 5 =============

# Challenge Task 1 of 2
# I want to make sure that the email address isn't from any of my coworkers at Treehouse. We'll solve this with a custom validator.

# Add a new function named not_treehouse that takes a single argument. If the argument ends with "@teamtreehouse.com", raise a ValidationError. You can use whatever error message you want.

# Remember, too, that it's a good idea to standardize your input before testing it, so you might want to lower- or uppercase the value.


from django import forms


def not_treehouse(value):
    temp = value.split('@')

    if len(temp) != 2 or temp[1].lower() == 'teamtreehouse.com':
        raise forms.ValidationError('The target path must be from teamtreehouse')

    return True

class LeadShareForm(forms.Form):
    email = forms.EmailField()
    link = forms.URLField()
    honeypot = forms.CharField(widget=forms.HiddenInput, required=False)

    def clean_honeypot(self):
        honey = self.cleaned_data['honeypot']
        if len(honey):
            raise forms.ValidationError('Bad robot!')
        return honey


# Challenge Task 2 of 2
# Alright, now that we have the validator, we need to use it!

# Add the not_treehouse validator to LeadShareForm's email field. Remember, validators is an iterable.


from django import forms


def not_treehouse(value):
    temp = value.split('@')

    if len(temp) != 2 or temp[1].lower() == 'teamtreehouse.com':
        raise forms.ValidationError('The target path must be from teamtreehouse')

    return True

class LeadShareForm(forms.Form):
    email = forms.EmailField(validators=[not_treehouse])
    link = forms.URLField()
    honeypot = forms.CharField(widget=forms.HiddenInput, required=False)

    def clean_honeypot(self):
        honey = self.cleaned_data['honeypot']
        if len(honey):
            raise forms.ValidationError('Bad robot!')
        return honey

# ============= Part 6 =============

# Challenge Task 1 of 1
# You can see I've added a new field to the LeadShareForm, email2. This field is your typical "please verify your email" field but we're not doing the verification yet.

# Add a clean method to the form and check that email and email2 have the same value. If not, raise a ValidationError. As usual, the error message can be anything you'd like.from django import forms


def not_treehouse(value):
    if value.lower().endswith('@teamtreehouse.com'):
        raise forms.ValidationError('Just come talk to me')


class LeadShareForm(forms.Form):
    email = forms.EmailField(validators=[not_treehouse])
    email2 = forms.EmailField(label='Email again', validators=[not_treehouse])
    link = forms.URLField()
    honeypot = forms.CharField(widget=forms.HiddenInput, required=False)

    def clean_honeypot(self):
        honey = self.cleaned_data['honeypot']
        if len(honey):
            raise forms.ValidationError('Bad robot!')
        return honey


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        email2 = cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError('Both emails must match!')