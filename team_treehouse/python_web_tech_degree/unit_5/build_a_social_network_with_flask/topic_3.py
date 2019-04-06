# ============= Part 1 =============
# Challenge Task 1 of 2
# In the nav tag in layout.html, add three links:

# 1. A link to logout() with the text "Sign Out"
# 2. A link to 'login()' with the text "Sign In"
# 3. A link to 'register()' with the text "Sign Up"


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


@app.route('/')
def index():
    return render_template('index.html')



#HTML

<!doctype html>
<html>
<head>
<title>Lunch</title>
</head>
<body>

<nav>
<!-- Add menu here -->
  <a href="{{ url_for('logout') }}" title="Sign Out">Sign Out</a>
  <a href="{{ url_for('login') }}" title="Sign In">Sign In</a>
  <a href="{{ url_for('register') }}" title="Sign Up">Sign Up</a>
</nav>

<div class="messages">
{% with messages = get_flashed_messages() %}
{% for message in messages %}
<div>{{ message }}</div>
{% endfor %}
{% endwith %}
</div>

{% block content %}{% endblock %}
</body>
</html>

# Challenge Task 2 of 2
# Now use current_user.is_authenticated() to make the logout() link only show to authenticated users and the login() and register() links show to unauthenticated users.

<!doctype html>
<html>
<head>
<title>Lunch</title>
</head>
<body>

<nav>
<!-- Add menu here -->
  {% if current_user.is_authenticated() %}
    <a href="{{ url_for('logout') }}" title="Sign Out">Sign Out</a>
 	{% else %}
    <a href="{{ url_for('login') }}" title="Sign In">Sign In</a>
    <a href="{{ url_for('register') }}" title="Sign Up">Sign Up</a>
 	{% endif %}
</nav>

<div class="messages">
{% with messages = get_flashed_messages() %}
{% for message in messages %}
<div>{{ message }}</div>
{% endfor %}
{% endwith %}
</div>

{% block content %}{% endblock %}
</body>
</html>

# ============= Part 2 =============

# Challenge Task 1 of 3
# Create a new Model class with the name LunchOrder. Give it a TextField attribute named order.
import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase(':memory:')

class LunchOrder(Model):
    order = TextField()

class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = CharField(default='')

    class Meta:
        database = DATABASE

    @classmethod
    def new(cls, email, password):
        cls.create(
            email=email,
            password=generate_password_hash(password)
        )


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()


# Challenge Task 2 of 3
# Now add a DateField (not DateTimeField) to the LunchOrder model. Name it date and do not give it a default value.

import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase(':memory:')

class LunchOrder(Model):
    order = TextField()
    date = DateField()

class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = CharField(default='')

    class Meta:
        database = DATABASE

    @classmethod
    def new(cls, email, password):
        cls.create(
            email=email,
            password=generate_password_hash(password)
        )


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()


# Challenge Task 3 of 3
# Great! Now, add a ForeignKeyField to your LunchOrder model. Name it user. user should be related to the User model and the related_name should be "orders".

import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase(':memory:')

class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = CharField(default='')

    class Meta:
        database = DATABASE

    @classmethod
    def new(cls, email, password):
        cls.create(
            email=email,
            password=generate_password_hash(password)
        )

class LunchOrder(Model):
    order = TextField()
    date = DateField()
    user = ForeignKeyField(
    	rel_model=User,
        related_name='orders'
    )

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()

# ============= Part 3 =============

# Challenge Task 1 of 3
# In forms.py, add a new form class named LunchOrderForm. It should have two fields, order and date. The order field should be a TextAreaField and date should be a DateField. Both should have DataRequired as a validator.

## forms.py
from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email, Length


class LunchOrderForm(Form):
    order = TextAreaField(validators=[DataRequired()])
    date = DateField(validators=[DataRequired()])

class SignUpInForm(Form):
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired(), Length(min=8)])

## models.py

import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase(':memory:')


class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = CharField(default='')

    class Meta:
        database = DATABASE

    @classmethod
    def new(cls, email, password):
        cls.create(
            email=email,
            password=generate_password_hash(password)
        )


class LunchOrder(Model):
    order = TextField()
    date = DateField()
    user = ForeignKeyField(User, related_name="orders")

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()


## lunch.py

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


@app.route('/')
def index():
    return render_template('index.html')


# Challenge Task 2 of 3
# Next, create a new view in lunch.py named order_lunch. Give it a route of /order and make sure it accepts both GET and POST methods. Make it return the rendered version of the lunch.html template.

## lunch.py
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

@app.route('/order', methods=('GET', 'POST'))
def order_lunch():
    return render_template('lunch.html')

@app.route('/secret')
@login_required
def secret():
    return "I should only be visible to logged-in users"

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
def index():
    return render_template('index.html')


## forms.py
from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email, Length


class LunchOrderForm(Form):
    order = TextAreaField(validators=[DataRequired()])
    date = DateField(validators=[DataRequired()])

class SignUpInForm(Form):
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired(), Length(min=8)])


## models.py

import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase(':memory:')


class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = CharField(default='')

    class Meta:
        database = DATABASE

    @classmethod
    def new(cls, email, password):
        cls.create(
            email=email,
            password=generate_password_hash(password)
        )


class LunchOrder(Model):
    order = TextField()
    date = DateField()
    user = ForeignKeyField(User, related_name="orders")

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()

# Challenge Task 3 of 3
# Finally, you need to instantiate, process, and send LunchOrderForm to the template. If the form is valid after submission, create a new LunchOrder object with the data and set the user to the current user.

## lunch.py
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

@app.route('/order', methods=('GET', 'POST'))
def order_lunch():
    form = forms.LunchOrderForm()
    if form.validate_on_submit():
        models.LunchOrder.create(
            order=form.order.data.strip(),
            date=form.date.data,
            user=g.user._get_current_object()
        )
    return render_template('lunch.html', form=form)

@app.route('/secret')
@login_required
def secret():
    return "I should only be visible to logged-in users"

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
def index():
    return render_template('index.html')


## forms.py

from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email, Length


class LunchOrderForm(Form):
    order = TextAreaField(validators=[DataRequired()])
    date = DateField(validators=[DataRequired()])

class SignUpInForm(Form):
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired(), Length(min=8)])


## models.py

import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase(':memory:')


class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = CharField(default='')

    class Meta:
        database = DATABASE

    @classmethod
    def new(cls, email, password):
        cls.create(
            email=email,
            password=generate_password_hash(password)
        )


class LunchOrder(Model):
    order = TextField()
    date = DateField()
    user = ForeignKeyField(User, related_name="orders")

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()

# ============= Part 4 =============

# Challenge Task 1 of 1
# Add a new view at /today that shows the current user's lunch order for today. It should render the "today.html" template. Don't worry about editing the template yet. Since this is about the current user, login should be required.

## lunch.py
from flask import Flask, g, render_template, flash, redirect, url_for
from flask.ext.bcrypt import check_password_hash
from flask.ext.login import LoginManager, login_user, current_user, login_required, logout_user

import forms
import models
import datetime

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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order', methods=('GET', 'POST'))
def order_lunch():
    form = forms.LunchOrderForm()
    if form.validate_on_submit():
        models.LunchOrder.create(
            user=g.user._get_current_object(),
            date=form.date.data,
            order=form.order.data.strip()
        )
    return render_template('lunch.html', form=form)


@app.route('/today')
@login_required
def today():
    order = models.LunchOrder.select().where(
        models.LunchOrder.date == datetime.date.today(),
        models.LunchOrder.user == g.user._get_current_object()
    ).get()
    return render_template('today.html', order=order)

## template/today.html

{% extends "layout.html" %}

{% block content %}
<h1>Your lunch for today</h1>

<p>
	<h2>{{ order.user }}</h2>
	<h3>{{ order.date.strftime('%Y-%m-%d') }}</h3>
  <h3>{{ order.order }}</h3>
</p>
{% endblock %}

# ============= Part 5 =============

# Challenge Task 1 of 2
# Update templates/today.html to show today's order's date and the order attribute from the order variable. Use strftime on the date with the format %Y-%m-%d.

## lunch.py

import datetime

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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order', methods=('GET', 'POST'))
def order_lunch():
    form = forms.LunchOrderForm()
    if form.validate_on_submit():
        models.LunchOrder.create(
            user=g.user._get_current_object(),
            date=form.date.data,
            order=form.order.data.strip()
        )
    return render_template('lunch.html', form=form)


@app.route('/today')
@login_required
def today():
    order = models.LunchOrder.select().where(
        models.LunchOrder.date == datetime.date.today() &
        models.LunchOrder.user == g.user._get_current_object()
    ).get()
    return render_template('today.html', order=order)


@app.route('/cancel_order/<int:order_id>')
@login_required
def cancel_order(order_id):
    try:
        order = models.LunchOrder.select().where(
            id=order_id,
            user=g.user._get_current_object()
        ).get()
    except models.DoesNotExist:
        pass
    else:
        order.delete_instance()
    return redirect(url_for('index'))



## templates/today.html

{% extends "layout.html" %}

{% block content %}
<h1>Your lunch for today</h1>

<h2>{{ order.date.strftime('%Y-%m-%d') }}</h2>
<p>{{ order.order }}</p>
<!-- button to the route for cancel_order with order_id=order.id -->
<a href="{{ url_for('cancel_order', order_id=order.id) }}">Cancel</a>
{% endblock %}

# Challenge Task 2 of 2
# Now add a <a> with an href attribute that points to the url for the cancel_order view. The view takes one argument, order_id, which should be the id attribute of the order.

## templates/layout.html

{% extends "layout.html" %}

{% block content %}
<h1>Your lunch for today</h1>

<h2>{{ order.date.strftime('%Y-%m-%d') }}</h2>
<p>{{ order.order }}</p>
<!-- button to the route for cancel_order with order_id=order.id -->
<a href="{{ url_for('cancel_order', order_id=order.id) }}">Cancel</a>
{% endblock %}

## lunch.py


import datetime

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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order', methods=('GET', 'POST'))
def order_lunch():
    form = forms.LunchOrderForm()
    if form.validate_on_submit():
        models.LunchOrder.create(
            user=g.user._get_current_object(),
            date=form.date.data,
            order=form.order.data.strip()
        )
    return render_template('lunch.html', form=form)


@app.route('/today')
@login_required
def today():
    order = models.LunchOrder.select().where(
        models.LunchOrder.date == datetime.date.today() &
        models.LunchOrder.user == g.user._get_current_object()
    ).get()
    return render_template('today.html', order=order)


@app.route('/cancel_order/<int:order_id>')
@login_required
def cancel_order(order_id):
    try:
        order = models.LunchOrder.select().where(
            id=order_id,
            user=g.user._get_current_object()
        ).get()
    except models.DoesNotExist:
        pass
    else:
        order.delete_instance()
    return redirect(url_for('index'))


