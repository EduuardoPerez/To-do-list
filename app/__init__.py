from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config
from .auth import auth

def create_app():
  app = Flask(__name__)
  bootstrap = Bootstrap(app)

  # Key for generate a security session in flask
  app.config.from_object(Config)

  # Registering the auth Blueprint
  app.register_blueprint(auth)

  return app
