# coding=utf-8


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/flask_todo_dev.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY = 'dev'


class ProductConfig(BaseConfig):
    DEBUG = False
    SECRET_KEY = "djaeifheaofjaeofjeaafn"


Config = {
    'develop': BaseConfig,
    'product': ProductConfig,
    'test': BaseConfig
}