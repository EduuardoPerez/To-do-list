from flask import Flask, request, make_response, redirect

app = Flask(__name__)


@app.route('/')
def index():
  user_ip = request.remote_addr

  response = make_response(redirect('/hello'))
  response.set_cookie('user_ip', user_ip) # se guarda en una cookie la IP del usuario

  return response


@app.route('/hello')
def hello():
  user_ip = request.cookies.get('user_ip') # Se obtiene de las cookies la IP del usuario

  return f'Hello World Flask! Your IP is {user_ip}'