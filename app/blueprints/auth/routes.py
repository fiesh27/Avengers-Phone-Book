from app import db
from . import bp as auth
from flask import request, redirect, render_template, url_for, flash
from app.forms import AvengerInfoForm, LoginForm
from app.models import Avenger
from werkzeug.security import check_password_hash
from flask_login import login_required, login_user, logout_user





@auth.route('/register', methods=['GET', 'POST'])
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


@auth.route('/login', methods=['GET', 'POST'])
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
        flash('You have successfully logged in', 'danger')
        
        return redirect(url_for('index'))

    return render_template('login.html', **context)
        
@auth.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out', 'danger')
    return redirect(url_for('index'))