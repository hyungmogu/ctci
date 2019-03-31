# ============= Part 1 =============
# Challenge Task 1 of 3
# Import the g object from the flask library.

from flask import Flask, g

import models

app = Flask(__name__)


# Challenge Task 2 of 3
# Now add a function named before_request that sets g.db to the DATABASE variable in models and calls the .connect() method. The function should be decorated with the before_request decorator.

from flask import Flask, g

import models

app = Flask(__name__)


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

# Challenge Task 3 of 3
# Finally, create a function named after_request that takes a response object. The function should close the g.db connection and return the response. You should decorate the function with after_request.

from flask import Flask, g

import models

app = Flask(__name__)


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response


# ============= Part 2 =============
# Challenge Task 1 of 4
# Add a secret_key attribute to app with a random value.

from flask import Flask, g

import models

app = Flask(__name__)
app.secret_key = '()*#)(US)(DUA)S(DK()ASKBVKNKSANDKJWE32irjoifva'


# Challenge Task 2 of 4
# Import the LoginManager from Flask-Login.

from flask import Flask, g
from flask.ext.login import LoginManager

import models

app = Flask(__name__)
app.secret_key = '()*#)(US)(DUA)S(DK()ASKBVKNKSANDKJWE32irjoifva'


# Challenge Task 3 of 4
# Now create a LoginManager instance named login_manager. Then run the init_app method, passing app as the argument.

from flask import Flask, g
from flask.ext.login import LoginManager

import models

app = Flask(__name__)
app.secret_key = '()*#)(US)(DUA)S(DK()ASKBVKNKSANDKJWE32irjoifva'

login_manager = LoginManager()
login_manager.init_app(app)

# Challenge Task 4 of 4
# Finally, create a function named load_user that takes a user's id attribute as an argument. Inside the function, look up a models.User instance with the id and return it. Return None if the User doesn't exist. Decorate the function with @login_manager.user_loader.

from flask import Flask, g
from flask.ext.login import LoginManager

import models

app = Flask(__name__)
app.secret_key = '()*#)(US)(DUA)S(DK()ASKBVKNKSANDKJWE32irjoifva'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

# ============= Part 3 =============
# Challenge Task 1 of 4
# Import Form from Flask-WTF. Import StringField and PasswordField from wtforms. Lastly, import DataRequired, Email, and Length from wtforms.validators.

from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired, Email, Length)

# Challenge Task 2 of 4
# Create a new Form class named SignUpForm. Give it two fields, email and password. email should be a StringField and password should be a PasswordField.


from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired, Email, Length)



class SignUpForm(Form):
    email = StringField()
    password = PasswordField()

# Challenge Task 3 of 4
# Add DataRequired and Email to the validators for the email field.

from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired, Email, Length)



class SignUpForm(Form):
    email = StringField(
        'Email',
    	validators = [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField()

# Challenge Task 4 of 4
# Finally, add DataRequired and Length to the validators for password. Set the min for Length to 8.

from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired, Email, Length)



class SignUpForm(Form):
    email = StringField(
        'Email',
    	validators = [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField(
    	'Password',
        validators = [
        	DataRequired(),
            Length(min=8)
        ]
    )

# ============= Part 4 =============

# Challenge Task 1 of 1
# Create a macro named hide_email. It should take a User as an argument. Print out the email attribute of the User in the following format: t***@example.com for the email test@example.com. This will require splitting the email string and using a for loop.

{% macro hide_email(user) %}
	{% for char in user.email.split('@') %}
		{% if loop.index == 1 %}
			{{(user.email.split('@'))[0][0]}}{{ '*' * ((user.email.split('@'))[0][1:]|length) }}@{{ (user.email.split('@'))[1] }}
		{% else %}
			{{ char }}
        {% endif %}
	{% endfor %}
{% endmacro %}

# ============= Part 5 =============

# Challenge Task 1 of 3
# Add a new view to lunch.py. The function name should be register and the route should be "/register". It should accept both GET and POST methods. For now, have it return the string "register".


from flask import Flask, g
from flask.ext.login import LoginManager

import forms
import models

app = Flask(__name__)
app.secret_key = 'this is our super secret key. do not share it with anyone!'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.select().where(
            models.User.id == int(userid)
        ).get()
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route("/register", methods=('GET','POST'))
def register():
    return 'register'


# Challenge Task 2 of 3
# Your register() view needs to create an instance of the SignUpForm from forms. It should also render and return the register.html template. You'll need to import render_template. In the template's context, name the SignUpForm instance as form.



from flask import Flask, g, render_template
from flask.ext.login import LoginManager

import forms
import models

app = Flask(__name__)
app.secret_key = 'this is our super secret key. do not share it with anyone!'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.select().where(
            models.User.id == int(userid)
        ).get()
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/register', methods=('GET','POST'))
def register():
    form = forms.SignUpForm()
    return render_template('register.html', form=form)


# Challenge Task 3 of 3
# Finally, update the register() view so that the form is validated on submission. If it's valid, use the models.User.new() method to create a new User from the form data and flash the message "Thanks for registering!". You'll need to import flash().

from flask import Flask, g, render_template, flash
from flask.ext.login import LoginManager

import forms
import models

app = Flask(__name__)
app.secret_key = 'this is our super secret key. do not share it with anyone!'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.select().where(
            models.User.id == int(userid)
        ).get()
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/register', methods=('GET','POST'))
def register():
    form = forms.SignUpForm()
    if form.validate_on_submit():
        models.User.new(form.email.data, form.password.data)
        flash ('Thanks for registering!')
    return render_template('register.html', form=form)


# ============= Part 7 =============

# Challenge Task 1 of 2
# Currently, "/secret" isn't protected from anonymous users. Mark it so it requires users to be logged in. You'll need to import login_required.

from flask import Flask, g, render_template, flash
from flask.ext.bcrypt import check_password_hash
from flask.ext.login import LoginManager, login_user, current_user, login_required

import forms
import models

app = Flask(__name__)
app.secret_key = 'this is our super secret key. do not share it with anyone!'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.select().where(
            models.User.id == int(userid)
        ).get()
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.SignUpInForm()
    if form.validate_on_submit():
        models.User.new(
            email=form.email.data,
            password=form.password.data
        )
        flash("Thanks for registering!")
    return render_template('register.html', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.SignUpInForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(
                models.User.email == form.email.data
            )
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("You're now logged in!")
            else:
                flash("No user with that email/password combo")
        except models.DoesNotExist:
              flash("No user with that email/password combo")
    return render_template('register.html', form=form)

@app.route('/secret')
@login_required
def secret():
    return "I should only be visible to logged-in users"

# Challenge Task 2 of 2
# Now add a view named logout() with "/logout" as its route. This view should log the user out and then redirect to "/login". You'll need to import logout_user, redirect, and probably url_for.

from flask import Flask, g, render_template, flash, redirect, url_for
from flask.ext.bcrypt import check_password_hash
from flask.ext.login import LoginManager, login_user, current_user, login_required, logout_user

import forms
import models

app = Flask(__name__)
app.secret_key = 'this is our super secret key. do not share it with anyone!'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.select().where(
            models.User.id == int(userid)
        ).get()
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.SignUpInForm()
    if form.validate_on_submit():
        models.User.new(
            email=form.email.data,
            password=form.password.data
        )
        flash("Thanks for registering!")
    return render_template('register.html', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.SignUpInForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(
                models.User.email == form.email.data
            )
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("You're now logged in!")
            else:
                flash("No user with that email/password combo")
        except models.DoesNotExist:
              flash("No user with that email/password combo")
    return render_template('register.html', form=form)

@app.route('/secret')
@login_required
def secret():
    return "I should only be visible to logged-in users"

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
