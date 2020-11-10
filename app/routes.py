from app import db, Message, mail

from flask import current_app as app, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash

from app.forms import AvengerInfoForm, LoginForm, BlogPostForm

from app.models import Avenger, Post

from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
def index():

    context = {
        "head": "Welcome to the Avengers Phone Book"
    }
    return render_template('index.html', **context)





@app.route('/users')
@login_required
def users():
    context = {
        'users': Avenger.query.all()
    }
    return render_template('users.html', **context)


@app.context_processor
def cart_stuff():
    if 'cart' not in session:
        session['cart'] = {
            'items': [],
            'cart_total': 0
        }

    return {'cart': session['cart']} 

