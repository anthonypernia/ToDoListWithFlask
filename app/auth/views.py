from . import auth
from app.forms import LoginForm
from flask import render_template, flash, url_for, redirect, session

@auth.route('/login', methods=['GET', 'POST'])
def login():
    context = {
        'login_form': LoginForm()
    }
    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('registrado con exito {}'.format(username))

        return redirect(url_for('index'))
    return render_template('login.html', **context)
