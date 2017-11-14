# -*- coding: utf-8 -*-
"""todo views."""
from flask import render_template, Blueprint
from flask_login import login_required

blueprint = Blueprint('todo', __name__, url_prefix='/todo', static_folder='../static')


@blueprint.route('/')
@login_required
def todo():
    return render_template('todo/todos.html')