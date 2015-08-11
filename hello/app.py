import logging

from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy


# Create our Flask app and REST API

app = Flask(__name__)
api = Api(app)


# Configure database access

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://rrwood:rrwood!@localhost/helloflask"
flask_SQA = SQLAlchemy(app)


# Route resources

from hello.resources.endpoints import PeopleEndpoint

api.add_resource(PeopleEndpoint, '/people', '/people/<id>')


if (__name__=='__main__'):
    logging.info("Hello, %s",__file__)
    