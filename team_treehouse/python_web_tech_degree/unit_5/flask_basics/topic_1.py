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

from flask import Flask

app = Flask(__name__)

@app.route('/multiply')
def multiply():
    return '{}'.format(5 * 5)


# Challenge Task 2 of 5
# Add a new route to multiply() that has two arguments. Add the same two arguments to the multiply() view. They should have defaults of 5.


from flask import Flask

app = Flask(__name__)

@app.route('/multiply')
@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1=5, num2=5):
    return '{}'.format(5 * 5)


# Challenge Task 3 of 5
# Mark both route arguments as ints.

from flask import Flask

app = Flask(__name__)

@app.route('/multiply')
@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1=5, num2=5):
    return '{}'.format(5 * 5)


# Challenge Task 4 of 5
# Add routes to allow floats or a combination of floats and ints.

from flask import Flask

app = Flask(__name__)

@app.route('/multiply')
@app.route('/multiply/<int:num1>/<int:num2>')
@app.route('/multiply/<int:num1>/<float:num2>')
@app.route('/multiply/<float:num1>/<int:num2>')
@app.route('/multiply/<float:num1>/<float:num2>')
def multiply(num1=5, num2=5):
    return '{}'.format(5 * 5)


# Challenge Task 5 of 5
# Change the response to multiply the two arguments and return their product.

from flask import Flask

app = Flask(__name__)

@app.route('/multiply')
@app.route('/multiply/<int:num1>/<int:num2>')
@app.route('/multiply/<int:num1>/<float:num2>')
@app.route('/multiply/<float:num1>/<int:num2>')
@app.route('/multiply/<float:num1>/<float:num2>')
def multiply(num1=5, num2=5):
    return '{}'.format(num1 * num2)

