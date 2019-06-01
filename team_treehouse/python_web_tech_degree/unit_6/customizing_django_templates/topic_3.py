# ============= Part 1 =============
# Challenge Task 1 of 4
# Output the contents of the num_elf variable in the template.

{{num_elf}}

# Challenge Task 2 of 4
# After printing num_elf, include the word "elf". So for example, if num_elf were set to 1, the page should say "1 elf".

{{num_elf}} elf

# Challenge Task 3 of 4
# Now change the template so that if num_elf is 1, the word "elf" is singular, but if num_elf is more than 1, the word "elf" is plural ("elves"). Here are the pluralize docs if you need them.

{{num_elf}} el{{num_elf|pluralize:"f,ves"}}

# Challenge Task 4 of 4
# Add a conditional that prints, "Wow, that's a lot of elves!" if there are more than 5 elves.

{{num_elf}} el{{num_elf|pluralize:"f,ves"}}

{% if num_elf > 5 %}
 Wow, that's a lot of elves!
{% endif %}


# ============= Part 2 =============
# Challenge Task 1 of 2
# Create a function called "reverse_text" that takes a string as an argument, and returns a string with those words reversed. So reverse_text("balloon") should return "noollab".

from django import template

register = template.Library()

def reverse_text(text):
    return text[::-1]

# Challenge Task 2 of 2
# Now that your function works, register it as a filter. Be sure to give your filter a name when you register it!

from django import template

register = template.Library()

@register.filter('reverse_text')
def reverse_text(text):
    return text[::-1]



# ============= Part 3 =============
# Challenge Task 1 of 4
# In this final code challenge, you'll create a tag that will return the proper conjugation of the verb "to be" depending on whether the subject is plural or singular. Example: "There is 1 elf" versus "There are 5 elves".

# Start by creating a conjugate_is function for your template tag. It should take a number as an argument. If (and only if) that number equals 1, the function should return the string 'is'.

# code_challenges/templatetags/fairy_extras.py
from django import template

register = template.Library()


def conjugate_is(number):
    if number == 1:
        return 'is'

# Challenge Task 2 of 4
# Update the conjugate_is function to return the string 'are' if the number is anything other than 1.

# code_challenges/templatetags/fairy_extras.py
from django import template

register = template.Library()


def conjugate_is(number):
    if number == 1:
        return 'is'
    else:
        return 'are'


# Challenge Task 3 of 4
# Now, register your functions as a simple tag!

# code_challenges/templatetags/fairy_extras.py
from django import template

register = template.Library()

@register.simple_tag()
def conjugate_is(number):
    if number == 1:
        return 'is'
    else:
        return 'are'

# Challenge Task 4 of 4
# Replace the word "is" in the sentence in the template with your custom template tag. Don't forget to pass in the num_elf argument!

# code_challenges/templatetags/fairy_extras.py
from django import template

register = template.Library()

@register.simple_tag()
def conjugate_is(number):
    if number == 1:
        return 'is'
    else:
        return 'are'

# code_challenges/templates/code_challenges/list.html
{% load fairy_extras %}

There {% conjugate_is num_elf %} {{num_elf}} el{{ num_elf|pluralize:"f,ves" }}.
