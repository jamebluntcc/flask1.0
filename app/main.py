# coding:utf-8
"""main application"""
from flask import Flask
from settings import Config
from extensions import db
from .import todo


def create_app(config='develop'):
    app = Flask(__name__)
    app.config.from_object(Config[config])
    db.init_app(app)
    app.register_blueprint(todo.views.blueprint)
    return app

