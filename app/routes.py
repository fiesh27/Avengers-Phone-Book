from app import app, db

from flask import render_template, request, redirect, url_for

from app.forms import AvengerInfoForm

from app.models import Avenger




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
        name = form.name.data
        avenger_name = form.avenger_name.data
        phone_num = form.phone_num.data
        password = form.password.data
        new_user = Avenger(name, avenger_name, phone_num, password )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('register.html', **context)