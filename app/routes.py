from app import app, db, Message, mail

from flask import render_template, request, redirect, url_for, flash
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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = AvengerInfoForm()
    context = {
        'form': form 
    }
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        avenger_name = form.avenger_name.data
        address = form.address.data
        email = form.email.data
        phone_num = form.phone_num.data
        password = form.password.data
        print(first_name)
        
        new_user = Avenger(first_name,last_name, avenger_name, address, email, phone_num, password)
        db.session.add(new_user)
        db.session.commit()

        flash("You have successfully registered!")
        return redirect(url_for('index'))

    return render_template('register.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    context = {
        'form': form
    }
    if request.method == 'POST' and form.validate():
        avenger_name = form.avenger_name.data
        password = form.password.data
        user = Avenger.query.filter_by(avenger_name=avenger_name).first()
        if user is None or not check_password_hash(user.password, password):
            flash('Incorrect Avenger Name/Password. Please try again', 'danger')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        flash('You have successfully logged in', 'success')
        
        return redirect(url_for('index'))

    return render_template('login.html', **context)
        
@app.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out', 'primary')
    return redirect(url_for('index'))


@app.route('/users')
@login_required
def users():
    context = {
        'users': Avenger.query.all()
    }
    return render_template('users.html', **context)

@app.route('/createposts', methods=['GET', 'POST'])
@login_required
def createposts():
    form = BlogPostForm()
    context = {
        'form': form
    }

    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        user_id = current_user.id

        new_post = Post(title, content, user_id)

        db.session.add(new_post)
        db.session.commit()

        flash('You have created a new post!', 'success')

        return redirect(url_for('createposts'))
    
    return render_template('createposts.html', **context)


@app.route('/posts/<int:post_id>')
@login_required
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST' and update_form.validate():
        title = update_form.title.data
        content = update_form.content.data
        user_id = current_user.id

        post.title = title
        post.content = content
        post.user_id = user_id

        db.session.commit()
        return redirect(url_for('post_update', post_id=post.id))

    return render_template('post_update.html', form=update_form, post=post)


@app.route('/posts/delete/<int:post_id>', methods=['POST'])
@login_required
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))