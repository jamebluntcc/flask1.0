# coding:utf-8
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from settings import Config

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(Config['develop'])
