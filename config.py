import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/ella-api"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
