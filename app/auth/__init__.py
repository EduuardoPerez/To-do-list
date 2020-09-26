from flask import Blueprint

# Every route that starts with auth it's going to be redirect to this Blueprint
auth = Blueprint('auth', __name__, url_prefix='/auth')

# After import the Blueprint import the views and configured the application with the function create_app
from . import views