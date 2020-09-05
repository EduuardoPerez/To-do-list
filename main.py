from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['Comprar cafe', 'Solicitud de compra', 'Entregar video al productor']

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
