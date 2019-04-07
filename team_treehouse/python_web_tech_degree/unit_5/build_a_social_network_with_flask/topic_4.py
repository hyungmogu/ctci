# ============= Part 1 =============

# Challenge Task 1 of 3
# Add a new model named Relationship. It should have a ForeignKeyField, related to User. The field should be named from_user with a related_name of "relationships".

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


class Relationship(Model):
    from_user = ForeignKeyField(User, related_name="relationships")


class LunchOrder(Model):
    order = TextField()
    date = DateField()
    user = ForeignKeyField(User, related_name="orders")


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, LunchOrder], safe=True)
    DATABASE.close()


# Challenge Task 2 of 3
# Now add a second ForeignKeyField to Relationship. This one, named to_user, should also point to User and have a related_name of "related_to".

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


class Relationship(Model):
    from_user = ForeignKeyField(User, related_name="relationships")
    to_user = ForeignKeyField(User, related_name="related_to")


class LunchOrder(Model):
    order = TextField()
    date = DateField()
    user = ForeignKeyField(User, related_name="orders")


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, LunchOrder], safe=True)
    DATABASE.close()

# Challenge Task 3 of 3
# Finally, add a third field, created_at, that's a DateTimeField with a default of datetime.datetime.now.

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


class Relationship(Model):
    from_user = ForeignKeyField(User, related_name="relationships")
    to_user = ForeignKeyField(User, related_name="related_to")
    created_at = DateTimeField(default=datetime.datetime.now)


class LunchOrder(Model):
    order = TextField()
    date = DateField()
    user = ForeignKeyField(User, related_name="orders")


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, LunchOrder], safe=True)
    DATABASE.close()

# ============= Part 2 =============

# Challenge Task 1 of 2
# Add a view named follow with a route of "/follow/<int:user_id>". It should be login_required. In the view, create a new Relationship with the current user as the from_user and the user with the provided ID as the to_user. Return a redirect to index.

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


@app.route('/follow/<int:user_id>')
@login_required
def follow(user_id):
    models.Relationship.create(
    	from_user=g.user._get_current_object(),
    	to_user=user_id
    )

    return redirect(url_for('index'))

# Challenge Task 2 of 2
# Now create a view for unfollowing a user. It should be at "/unfollow/<int:user_id>", should require a login, and should also redirect to the index view. The view should find and delete the existing Relationship instance.

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


@app.route('/follow/<int:user_id>')
@login_required
def follow(user_id):
    models.Relationship.create(
    	from_user=g.user._get_current_object(),
    	to_user=user_id
    )

    return redirect(url_for('index'))

@app.route('/unfollow/<int:user_id>')
@login_required
def unollow(user_id):
    models.Relationship.get(
    	from_user=g.user._get_current_object(),
    	to_user=user_id
    ).delete_instance()

    return redirect(url_for('index'))



# ============= Part 3 =============

# Challenge Task 1 of 1
# Update templates/profile.html so that it shows the total number of lunches ordered, followers, and people followed by a user.

{% extends "layout.html" %}
{% from "macro.html" import hide_email %}

{% block content %}

<h1>{{ hide_email(user) }}</h1>

<dl>
    <dt>Lunches:</dt>
    <dd>{{ user.orders.count() }} </dd>
    <dt>Followers:</dt>
    <dd>{{ user.followers.count() }}</dd>
    <dt>Following:</dt>
    <dd>{{ user.following.count() }}</dd>
</dl>

{% endblock %}

# ============= Part 4 =============

# Challenge Task 1 of 3
# Import abort from flask in lunch.py.

import datetime

from flask import Flask, g, abort, render_template, flash, redirect, url_for
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


@app.route('/follow/<int:user_id>')
@login_required
def follow(user_id):
    try:
        user = models.User.get(
            models.User.id == user_id
        )
        models.Relationship.create(
            from_user=g.user._get_current_object(),
            to_user=user
        )
    except (models.DoesNotExist, models.IntegrityError):
        pass
    return redirect(url_for('index'))


@app.route('/unfollow/<int:user_id>')
@login_required
def unfollow(user_id):
    try:
        user = models.User.get(
            models.User.id == user_id
        )
        models.Relationship.get(
            models.Relationship.from_user==g.user._get_current_object(),
            models.Relationship.to_user==user
        ).delete_instance()
    except (models.DoesNotExist, models.IntegrityError):
        pass
    return redirect(url_for('index'))


@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = models.User.select().where(
        models.User.id == user_id
    ).get()
    return render_template('profile.html', user=user)

# Challenge Task 2 of 3
# Add a new function named not_found that returns the string "404". Remember, error handlers need to accept a single argument, the error. Decorate this function with @app.errorhandler(404). Add , 404 after your response, too.

import datetime

from flask import Flask, g, abort, render_template, flash, redirect, url_for
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


@app.route('/follow/<int:user_id>')
@login_required
def follow(user_id):
    try:
        user = models.User.get(
            models.User.id == user_id
        )
        models.Relationship.create(
            from_user=g.user._get_current_object(),
            to_user=user
        )
    except (models.DoesNotExist, models.IntegrityError):
        pass
    return redirect(url_for('index'))


@app.route('/unfollow/<int:user_id>')
@login_required
def unfollow(user_id):
    try:
        user = models.User.get(
            models.User.id == user_id
        )
        models.Relationship.get(
            models.Relationship.from_user==g.user._get_current_object(),
            models.Relationship.to_user==user
        ).delete_instance()
    except (models.DoesNotExist, models.IntegrityError):
        pass
    return redirect(url_for('index'))


@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = models.User.select().where(
        models.User.id == user_id
    ).get()
    return render_template('profile.html', user=user)


@app.errorhandler(404)
def not_found(error):
    return "404", 404

# Challenge Task 3 of 3
# Now make not_found render the "404.html" template. Add an <h1> to the template with the 404 error code in it. Add a message to the template, if you want.

import datetime

from flask import Flask, g, abort, render_template, flash, redirect, url_for
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


@app.route('/follow/<int:user_id>')
@login_required
def follow(user_id):
    try:
        user = models.User.get(
            models.User.id == user_id
        )
        models.Relationship.create(
            from_user=g.user._get_current_object(),
            to_user=user
        )
    except (models.DoesNotExist, models.IntegrityError):
        pass
    return redirect(url_for('index'))


@app.route('/unfollow/<int:user_id>')
@login_required
def unfollow(user_id):
    try:
        user = models.User.get(
            models.User.id == user_id
        )
        models.Relationship.get(
            models.Relationship.from_user==g.user._get_current_object(),
            models.Relationship.to_user==user
        ).delete_instance()
    except (models.DoesNotExist, models.IntegrityError):
        pass
    return redirect(url_for('index'))


@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = models.User.select().where(
        models.User.id == user_id
    ).get()
    return render_template('profile.html', user=user)


@app.errorhandler(404)
def not_found(error):
    return "404", 404

# Challenge Task 3 of 3
# Now make not_found render the "404.html" template. Add an <h1> to the template with the 404 error code in it. Add a message to the template, if you want.


import datetime

from flask import Flask, g, abort, render_template, flash, redirect, url_for
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


@app.route('/follow/<int:user_id>')
@login_required
def follow(user_id):
    try:
        user = models.User.get(
            models.User.id == user_id
        )
        models.Relationship.create(
            from_user=g.user._get_current_object(),
            to_user=user
        )
    except (models.DoesNotExist, models.IntegrityError):
        pass
    return redirect(url_for('index'))


@app.route('/unfollow/<int:user_id>')
@login_required
def unfollow(user_id):
    try:
        user = models.User.get(
            models.User.id == user_id
        )
        models.Relationship.get(
            models.Relationship.from_user==g.user._get_current_object(),
            models.Relationship.to_user==user
        ).delete_instance()
    except (models.DoesNotExist, models.IntegrityError):
        pass
    return redirect(url_for('index'))


@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = models.User.select().where(
        models.User.id == user_id
    ).get()
    return render_template('profile.html', user=user)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

#404.html

{% extends "layout.html" %}

{% block content %}
<h1>404</h1>
{% endblock %}