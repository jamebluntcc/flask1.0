from flask import Blueprint

blueprint = Blueprint('todo', __name__)

from . import views