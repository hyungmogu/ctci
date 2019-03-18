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


# ============= Part 2 =============