from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

todos = ['Comprar cafe', 'Solicitud de compra', 'Entregar video al productor']


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
  response.set_cookie('user_ip', user_ip) # The user's IP is saved in the cookie

  return response


@app.route('/hello')
def hello():
  user_ip = request.cookies.get('user_ip') # The user's IP is obtained from the cookie
  context = {
    'user_ip': user_ip,
    'todos': todos,
  }

  # The context varible is expanded for pass every key:value as single variables
  return render_template('hello.html', **context)
