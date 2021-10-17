from flask import  request, render_template, redirect, make_response, session, url_for , flash
from flask_bootstrap import Bootstrap
from app.forms import LoginForm
import unittest
from app import create_app

app = create_app()

todos = ["Comprar ropa", "Entregar paquetes", "Hacer cafe", "Limpiar casa"]



@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html", error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    
    #response.set_cookie('user_ip', user_ip) #Reemplazamos la cookie por una variable de sesion
    session['user_ip'] =  user_ip
    return response

@app.route('/hello', methods=['GET'])
def hello():
    #user_ip = request.cookies.get('user_ip') #Obtenemos la cookie, pero aca la reemplazamos por variable de sesion
    user_ip = session.get('user_ip')
    #login_form = LoginForm()
    username = session.get('username')
    context = {
        'user_ip':user_ip, 
        'todos':todos,
        #'login_form': login_form,
        'username' : username
    }

    # if login_form.validate_on_submit():
    #     username = login_form.username.data
    #     session['username'] = username

    #     flash('registrado con exito {}'.format(username))

    #     return redirect(url_for('index'))

    return render_template('hello.html', **context)