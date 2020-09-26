from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
import unittest

from app import create_app
from app.forms import LoginForm
from app.firestore_service import get_users, get_todos

app = create_app()

todos = ['Comprar cafe', 'Solicitud de compra', 'Entregar video al productor']


@app.cli.command()
def test():
  # The tests are going to be all the tests that find unittest in the test folder in the root directory of the project
  test = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner().run(test)


@app.errorhandler(404)
def not_found(error):
  return render_template('404.html', error=error )


@app.errorhandler(500)
def internal_server_error(error):
  return render_template('500.html', error=error )


# Route for test how to handle a 500 error
# The enviroment varible FLASK_DEBUG has to be set in 0 for have disable the DEBUG
@app.route('/error_500')
def test_server_error():
	return 1/0


@app.route('/')
def index():
  user_ip = request.remote_addr

  response = make_response(redirect('/hello'))
  #response.set_cookie('user_ip', user_ip) # The user's IP is saved in the cookie
  session['user_ip'] = user_ip

  return response


# By default the flask routes allow the GET method, but when we want allow a POST method we have to declarte both in the list
# It isn't necesary when the route is just going to accept the GET method
@app.route('/hello', methods=['GET'])
def hello():
  user_ip = session.get('user_ip') # The user's IP is obtained from the cookie
  username = session.get('username')

  context = {
    'user_ip': user_ip,
    'todos': get_todos(user_id=username),
    'username': username
  }

  users = get_users()

  for user in users:
    print(user.id)
    print(user.to_dict()['password'])

  # The context varible is expanded for pass every key:value as single variables
  return render_template('hello.html', **context)
