from __future__ import print_function

from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://rrwood:rrwood!@localhost/helloflask"
flask_SQA = SQLAlchemy(app)


from resources.people import People

api.add_resource(People, '/people', '/people/<id>')


if (__name__=='__main__'):
    print("Hello, world.")