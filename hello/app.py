import logging

from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://rrwood:rrwood!@localhost/helloflask"
flask_SQA = SQLAlchemy(app)

# print("--> app.py: import resources.endpoints before")
# from resources.endpoints import PeopleEndpoint
# print("--> app.py: import resources.endpoints after")

# api.add_resource(PeopleEndpoint, '/people', '/people/<id>')


if (__name__=='__main__'):
    logging.info("Hello, %s",__file__)
    