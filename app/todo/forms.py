# -*- coding: utf-8 -*-
"""todo forms."""
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms.validators import DataRequired, Length

from .models import Todo


class TodoForm(FlaskForm):
    """Todo form."""
    todoname = StringField('Todo',
                           validators=[DataRequired(), Length(min=3, max=20)])
    content = TextAreaField('Content',
                            validators=[DataRequired()])
