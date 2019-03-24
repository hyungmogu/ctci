# ============= Part 1 =============
# Challenge Task 1 of 3
# Add an import for the make_response function from Flask.

from flask import Flask, make_response

app = Flask(__name__)


@app.route('/save')
def save():
    pass

# Challenge Task 2 of 3
# In the save() function, remove the pass statement. Now add a variable named response and set it's value to make_response(). You'll need to return the response variable.

from flask import Flask, make_response

app = Flask(__name__)


@app.route('/save')
def save():
    response = make_response()
    return response

# Challenge Task 3 of 3
# Now set a cookie on the response object using the response.set_cookie method. The key should be treehouse but the value can be anything you want.

from flask import Flask, make_response

app = Flask(__name__)


@app.route('/save')
def save():
    response = make_response()
    response.set_cookie("treehouse","hello world")
    return response

# ============= Part 2 =============

# Challenge Task 1 of 2
# Import the json library.

import json

# Challenge Task 2 of 2
# Create a function named to_json that takes a single argument. Convert the argument to string with the json library and return it.

import json

def to_json(arg):
    return json.dumps(arg)

# ============= Part 3 =============

# Challenge Task 1 of 1
# Create a function named from_json that takes a single argument. Parse the argument with the json library and return it.

import json

def from_json(args):
    return json.loads(args)

# ============= Part 4 =============

# Challenge Task 1 of 1
# Your template has been given a list named options. Loop through each item in options and create an <li> inside the <ul>. Print out the name key of each item.

from flask import Flask, render_template

from options import OPTIONS

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('options.html', options=OPTIONS)

# options.html

<ul>
	{% for item in options %}
  	<li>{{ item.name }}</li>
  {% endfor %}
</ul>


# ============= Part 5 =============

# Challenge Task 1 of 2
# Loop through each of the teachers in teachers and create an <li> for them in the provided <ul>. Inside the <li>, create an <h2> that holds the teacher's 'name' key.

#flask_app.py

from flask import Flask, render_template

from teachers import TEACHERS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("teachers.html", teachers=TEACHERS)

# templates/teachers.html

<ul class="teachers">
	{% for item in teachers %}
  	<li><h2>{{ item.name }}</h2></li>
  {% endfor %}
</ul>

# Challenge Task 2 of 2
# Now add a new <ul> inside of the <li> with a class of "courses". Inside this <ul> loop through the teacher's 'courses' key, creating an <li> for each course and printing the course.

<ul class="teachers">
	{% for item in teachers %}
  	<li>
      <h2>{{ item.name }}</h2>
      <ul class="courses">
        	{% for course in item.courses %}
          	<li>{{ course }}</li>
        	{% endfor %}
      </ul>
  </li>
  {% endfor %}
</ul>




# ============= Part 6 =============

# Challenge Task 1 of 3
# Import flash from Flask.

from flask import Flask, redirect, url_for, render_template, flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/fishy')
def fishy():
    return redirect(url_for('index'))

# Challenge Task 2 of 3
# Add a secret_key attribute to the app object.

from flask import Flask, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = "#$*)(*ASD)(SDG)(DIF)(I)(ASID)(ASd"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/fishy')
def fishy():
    return redirect(url_for('index'))


# Challenge Task 3 of 3
# flash() a message in the fishy() view before the return. The message can have any content you want.