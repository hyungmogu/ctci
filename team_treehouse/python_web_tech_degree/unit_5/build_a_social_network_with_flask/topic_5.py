# model.py
from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('sample.db')

class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)

    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls, email, password):
        try:
            with DATABASE.transaction():
                cls.create(
                    email=email,
                    password=generate_password_hash(password)
                )
        except IntegrityError:
          raise ValueError("User Already Exists")

class Taco(Model):
    user = ForeignKeyField(User,related_name="customer")
    protein = CharField(max_length=100)
    cheese = CharField(max_length=100)
    shell = CharField(max_length=100)
    extras = TextField()

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Taco], safe=True)
    DATABASE.close()

# forms.py
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired, Email, Length, EqualTo)

class SignUpInForm(Form):
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
          Length(min=8),
          EqualTo('password2', message='Passwords must match')
        ]
    )
    password2 = PasswordField(
    	'Confirm Password',
        validators = [DataRequired()]
    )

class Taco(Form):
    protein = StringField(
      'Protein'
    )
    cheese = StringField(
      'Cheese'
    )
    shell = StringField(
      'Shell'
    )
    extras = StringField(
      'Extras'
    )
# tacocat.py
from flask import Flask, g, abort, render_template, flash, redirect, url_for, request
from flask.ext.bcrypt import check_password_hash
from flask.ext.login import LoginManager, login_user, current_user, login_required, logout_user

import forms
import models

DEBUG = True
HOST = "0.0.0.0"
PORT = 8000

app = Flask(__name__)
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = True

app.secret_key = 'Hello world. This part can be any random but very secret string'
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
        models.User.create_user(
            email=form.email.data,
            password=form.password.data
        )
        flash("Thanks for registering!")
    return redirect(url_for('index'))


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.SignUpInForm()
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = models.User.get(
            models.User.email == email
        )
        if check_password_hash(user.password, password):
            login_user(user)
            flash("You're now logged in!")
            return redirect(url_for('index'))
        else:
            flash("No user with that email/password combo")
    except models.DoesNotExist:
        flash("No user with that email/password combo")
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
def index():
    tacos=models.Taco.select()
    return render_template('index.html', tacos=tacos)

@app.route('/taco', methods=('GET', 'POST'))
def taco():
    form = forms.Taco()
    protein = request.form.get('protein')
    cheese = request.form.get('cheese')
    shell = request.form.get('shell')
    extras = request.form.get('extras')

    if form.validate_on_submit():
        models.Taco.create(
            user=g.user._get_current_object(),
            protein = protein,
            cheese = cheese,
            shell = shell,
            extras = extras,
        )

        return redirect(url_for('index'))
    return render_template('taco.html', form=form)


if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, host=HOST, port=PORT)
# templates/index.html

{% extends 'layout.html' %}

{% block content %}
<h2>Tacos</h2>
    {% if tacos.count() %}
        <table class="u-full-width">
          <thead>
            <tr>
              <th>Protein</th>
              <th>Cheese?</th>
              <th>Shell</th>
              <th>Extras</th>
            </tr>
          </thead>
          <tbody>
        {% for taco in tacos %}
            <tr>
              <!-- taco attributes here -->
              <td>{{ taco.protein }}</td>
              <td>{{ taco.cheese }}</td>
              <td>{{ taco.shell }}</td>
              <td>{{ taco.extras }}</td>
            </tr>
        {% endfor %}
          </tbody>
        </table>
    {% else %}
        <!-- message for missing tacos -->
        no tacos yet
    {% endif %}
{% endblock %}

# templates/layout.html

<!doctype html>
<html>
  <head>
    <title>Tacocat</title>
    <link rel="stylesheet" href="/static/css/normalize.css">
    <link rel="stylesheet" href="/static/css/skeleton.css">
    <link rel="stylesheet" href="/static/css/tacocat.css">
  </head>
  <body>
    {% with messages=get_flashed_messages() %}
    {% if messages %}
        <div class="messages">
          {% for message in messages %}
          <div class="message">
            {{ message }}
          </div>
          {% endfor %}
        </div>
    {% endif %}
    {% endwith %}

    <div class="container">
      <div class="row">
        <div class="u-full-width">
          <nav class="menu">
          <!-- menu goes here -->
            <a href="{{ url_for('login') }}">Log in</a>
            <a href="{{ url_for('logout') }}">Log out</a>
            <a href="{{ url_for('register') }}">Sign up</a>
            {% if current_user.is_authenticated() %}
              <a href="{{ url_for('taco') }}">Add a New Taco</a>
              <a href="{{ url_for('logout') }}">Log Out</a>
            {% endif %}
          </nav>
          {% block content %}{% endblock %}
        </div>
      </div>
      <footer>
        <p>An MVP web app made with Flask on <a href="http://teamtreehouse.com">Treehouse</a>.</p>
      </footer>
    </div>
  </body>
</html>


# templates/login.html

{% extends 'layout.html' %}
{% from 'macros.html' import render_field %}

{% block content %}
<form method='POST' action=''>
  {{ form.hidden_tag() }}
  <div class="row">
    <div class="six columns">
      {{ render_field(form.email) }}
    </div>
    <div class="six columns">
      {{ render_field(form.password) }}
    </div>
  </div>
  <div class="u-full-width">
    <input type="submit" class="button-primary" value="Login">
  </div>
</form>
{% endblock %}


# templates/macro.html

{% macro render_field(field) %}
{% if field.errors %}
<div class="u-full-width field-errors">
  <ul>
    {% for error in field.errors %}
    <li>{{ error }}</li>
    {% endfor %}
  </ul>
</div>
{% endif %}
{{ field.label }}
{{ field(class="u-full-width") }}
{% endmacro %}


# templates/register.html

{% extends 'layout.html' %}

{% from 'macros.html' import render_field %}

{% block content %}

<form method='POST' action=''>
  {{ form.hidden_tag() }}
  <div class="u-full-width">
    {{ render_field(form.email) }}
  </div>
  <div class="row">
    <div class="six columns">
      {{ render_field(form.password) }}
    </div>
    <div class="six columns">
      {{ render_field(form.password2) }}
    </div>
  </div>
  <div class="u-full-width">
    <input type="submit" class="button-primary" value="Register">
  </div>
</form>

{% endblock %}


# templates/taco.html

{% extends 'layout.html' %}

{% from 'macros.html' import render_field %}

{% block content %}

<form method='POST' action=''>
  {{ form.hidden_tag() }}
  <div class="row">
    <div class="six columns">
      {{ render_field(form.protein) }}
    </div>
    <div class="six columns">
      {{ render_field(form.shell) }}
    </div>
  </div>
  <div class="row">
    <div class="six columns">
      {{ render_field(form.cheese) }}
    </div>
    <div class="six columns">
      {{ render_field(form.extras) }}
    </div>
  </div>
  <div class="u-full-width">
    <input type="submit" class="button-primary" value="Create">
  </div>
</form>

{% endblock %}

