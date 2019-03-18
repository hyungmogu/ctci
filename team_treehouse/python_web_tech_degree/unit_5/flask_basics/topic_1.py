# ============= Part 1 =============
# Challenge Task 1 of 2
# Import Flask from the flask library.

from flask import Flask

# Challenge Task 2 of 2
# Create a new Flask instance as a variable named app. The name you pass to the Flask app should be __name__.

from flask import Flask

app = Flask(__name__)

# ============= Part 2 =============
# Challenge Task 1 of 1
# Add a view function named index. Give this view a route of "/". Make the view return your name. You do not need to use app.run().

from flask import Flask

app = Flask(__name__)

# Your code goes here
@app.route('/')
def index():
    return "Hyungmo Gu"


# ============= Part 3 =============
# Challenge Task 1 of 1
# Import request from Flask. Then update the index view to return "Hello {name}", replacing {name} with a name argument in the query string.

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    return 'Hello {}'.format(name)


# ============= Part 4 =============
# Challenge Task 1 of 3
# Add a new route to hello() that expects a name argument. The view will need to accept a name argument, too.

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello(name):
     return 'Hello Student'

# Challenge Task 2 of 3
# Update the response from hello() to say "Hello {name}", replacing {name} with the passed-in name.

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello(name):
     return 'Hello {}'.format(name)

# Challenge Task 3 of 3
# Now give hello() a default name argument of "Treehouse".

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello(name="Treehouse"):
     return 'Hello {}'.format(name)

# ============= Part 5 =============

# Challenge Task 1 of 5
# Add a view named multiply. Give multiply a route named /multiply. Make multiply() return the product of 5 * 5. Remember, views have to return strings.

