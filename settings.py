# coding=utf-8

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'akfdlcidhdswijkehcdkd'


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.db')
    DEBUG = True


class ProductConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql://{username}:{passwd}@{host}/{database}".format(
        username=os.environ.get('USERNAME'),
        passwd=os.environ.get('PASSWORD'),
        host=os.environ.get('HOSTNAME', 'localhost'),
        database=os.environ.get('DATABASE')
    )


Config = {
    'develop': DevConfig,
    'product': ProductConfig,
    'test': DevConfig
}