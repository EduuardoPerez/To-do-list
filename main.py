from flask import Flask, request, make_response, redirect, render_template

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

  return render_template('hello.html', user_ip=user_ip)
