from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest


app = Flask(__name__)
bootstrap = Bootstrap(app)

# Key for generate a security session in flask
app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['Comprar cafe', 'Solicitud de compra', 'Entregar video al productor']

class LoginForm(FlaskForm ):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Send')


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
@app.route('/hello', methods=['GET', 'POST'])
def hello():
  user_ip = session.get('user_ip') # The user's IP is obtained from the cookie
  login_form = LoginForm()
  username = session.get('username')

  context = {
    'user_ip': user_ip,
    'todos': todos,
    'login_form': login_form,
    'username': username
  }

  if login_form.validate_on_submit():
    username = login_form.username.data
    session['username'] = username

    flash('Username registered successfully')

    return redirect(url_for('index'))

  # The context varible is expanded for pass every key:value as single variables
  return render_template('hello.html', **context)
