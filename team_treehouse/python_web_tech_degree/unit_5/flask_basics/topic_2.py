# ============= Part 1 =============
# Challenge Task 1 of 3
# Add an import for render_template. It comes directly from the flask library.

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hello/<name>')
def hello(name="Treehouse"):
    return 'Hello {}'.format(name)


# Challenge Task 2 of 3
# Use render_template() to render the "hello.html" template in hello().

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hello/<name>')
def hello(name="Treehouse"):
    return render_template('hello.html')


# Challenge Task 3 of 3
# Pass the name argument to the template. Print the name variable in the <h1> in the template.


from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hello/<name>')
def hello(name="Treehouse"):
    return render_template('hello.html', name=name)

<!doctype html>
<html>
<head><title>Hello!</title></head>
<body>
<h1>{{name}}</h1>
</body>
</html>
# ============= Part 2 =============
# Challenge Task 1 of 6
# Add two blocks to the "layout.html" template. Add a block named title around the content of the <title> tag. Add a block named content inside the <body> tag.

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

layout.html

<!doctype html>
<html>
<head><title>{% block title %}Smells Like Bakin'{% endblock %}</title></head>
<body>
	{% block content %}{% endblock %}
</body>
</html>


# Challenge Task 2 of 6
# Change "index.html" so it extends "layout.html".

{% extends "layout.html" %}


# Challenge Task 3 of 6
# Wrap everything in the <body> tag in "index.html" in the {% block content %} block.

{% extends "layout.html" %}

{% block content %}
<h1>Smells Like Bakin'!</h1>
<p>Welcome to my bakery web site!</p>
{% endblock %}


# Challenge Task 4 of 6
# Put the contents of the <title> tag in "index.html" into the title block.

{% extends "layout.html" %}

{% block title %}Homepage{% endblock %}

{% block content %}
<h1>Smells Like Bakin'!</h1>
<p>Welcome to my bakery web site!</p>
{% endblock %}

# Challenge Task 5 of 6
# Put the contents of the <title> tag in "index.html" into the title block.

{% extends "layout.html" %}

{% block title %}Homepage{% endblock %}

{% block content %}
<h1>Smells Like Bakin'!</h1>
<p>Welcome to my bakery web site!</p>
{% endblock %}


# Challenge Task 6 of 6
# Finally, change the "index.html" <title> tag to be: {{ super() }} Homepage. Make sure there's a space before "Homepage".

{% extends "layout.html" %}

{% block title %}{{ super() }} | Homepage{% endblock %}

{% block content %}
<h1>Smells Like Bakin'!</h1>
<p>Welcome to my bakery web site!</p>
{% endblock %}
