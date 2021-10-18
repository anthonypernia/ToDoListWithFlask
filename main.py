from flask import  request, render_template, redirect, make_response, session, url_for , flash
from flask_bootstrap import Bootstrap
from app.forms import LoginForm
import unittest
from app import create_app
from app.firestore_service import get_users, get_todos

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
    user_ip = session.get('user_ip')
    username = session.get('username')
    context = {
        'user_ip':user_ip, 
        'todos':get_todos(user_id=username),
        'username' : username
    }

    users = get_users()
    for user in users:
        print(user.id)
        print(user.to_dict()['password'])
    
    

    return render_template('hello.html', **context)