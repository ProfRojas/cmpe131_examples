import os

from flask_sqlalchemy import SQLAlchemy

# include Flask class from file flask
from flask import Flask

# for the location of the current file, what is its directory
basedir = os.path.abspath(os.path.dirname(__file__))

# create an instance of Flask class
# __name__ is a predefined setup variable
myapp_obj = Flask(__name__)
myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    # location of database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(myapp_obj)

from app import routes, models
