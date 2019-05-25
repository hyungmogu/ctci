# ============= Part 1 =============
# Challenge Task 1 of 3
# Use the {% block %} tag in the layout.html template to add a dynamic section to this template for a header.

# code_challenges/templates/code_challenges/layout.html
<html>
    <head>
        <title>Code Challenge</title>
    </head>
    <body>
        <div class="page-header">
            <!-- YOUR CODE HERE -->
            {% block content %}{% endblock %}
        </div>
    </body>
</html>

#code_challenges/templates/code_challenges/list.html


# Challenge Task 2 of 3
# Now, in the "list.html" template, extend "layout.html" (which is in the "code_challenges" directory).

# code_challenges/templates/code_challenges/layout.html
<html>
    <head>
        <title>Code Challenge</title>
    </head>
    <body>
        <div class="page-header">
            <!-- YOUR CODE HERE -->
            {% block content %}{% endblock %}
        </div>
    </body>
</html>

#code_challenges/templates/code_challenges/list.html

{% extends 'code_challenges/layout.html' %}

{% block content %}

{% endblock %}


# Challenge Task 3 of 3
# Finally, add a header that says Welcome to the code challenges!

{% extends 'code_challenges/layout.html' %}

{% block content %}
<h1>Welcome to the code challenges</h1>
{% endblock %}

# ============= Part 2 =============


# Challenge Task 1 of 3
# Add code that will display how many flavors of ice cream there are in the query set flavors using the length filter.

<html>
    <head>
        <title>Ice Cream</title>
    </head>
    <body>

        <div>We have {{ flavors|length }} flavors today.</div>

        <ul>

        </ul>

    </body>
</html>


# Challenge Task 2 of 3
# Use an alternate method to get the number of flavors. (Hint: It's a built-in method, not a filter.)

<html>
    <head>
        <title>Ice Cream</title>
    </head>
    <body>

        <div>We have {{ flavors.count }} flavors today.</div>

        <ul>

        </ul>

    </body>
</html>


# Challenge Task 3 of 3
# Finally, list all of the flavors of ice cream in the unordered list below. Use either a for tag to list all the flavors in <li> tags or the unordered_list filter.

<html>
    <head>
        <title>Ice Cream</title>
    </head>
    <body>

        <div>We have {{ flavors.count }} flavors today.</div>

        <ul>
          {% for flavor in flavors %}
          <li>{{ flavor }}</li>
          {% endfor %}
        </ul>

    </body>
</html>
