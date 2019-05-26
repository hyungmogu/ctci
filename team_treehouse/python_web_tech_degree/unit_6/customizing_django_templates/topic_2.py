# ============= Part 1 =============
# Challenge Task 1 of 2
# Output the value in the variable timestamp into your template.
{{ timestamp }}

# Challenge Task 2 of 2
# Using the date filter, render timestamp with the format "m/d/y, H:i". (That's 2-digit month, day, and year, hour in 24-hour format, and number of minutes.)
{{ timestamp | date:"m/d/y, H:i" }}

# ============= Part 2 =============

# Challenge Task 1 of 5
# Let's create a custom template tag. Start by importing template from django.
from django import template


# Challenge Task 2 of 5
# Import the Step class from the models.py file in the courses directory.
from django import template
from courses.models import Step


# Challenge Task 3 of 5
# Now assign template.Library() to the variable register.
from django import template
from courses.models import Step


register = template.Library()


# Challenge Task 4 of 5
# Next, create a function named steps_list that returns all of the Step objects.
from django import template
from courses.models import Step


register = template.Library()

def steps_list():
    steps = Step.objects.all()
    return steps


# Challenge Task 5 of 5
# Finally, use the @register decorator to register the function as an inclusion tag. Use the 'courses/step_list.html' template.

from django import template
from courses.models import Step


register = template.Library()

@register.inclusion_tag('courses/step_list.html')
def steps_list():
    steps = Step.objects.all()
    return steps

# ============= Part 3 =============