import logging

from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy


LOGGER = logging.getLogger(__name__)


# Create our Flask app and REST API

LOGGER.info("Creating Flask app and api")

app = Flask(__name__)
api = Api(app)


# Configure database access

LOGGER.info("Configuring database connectivity")

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://rrwood:rrwood!@localhost/helloflask"
flask_SQA = SQLAlchemy(app)


# Route resources

LOGGER.info("Configuring REST endpoints and routes")

from hello.resources.endpoints import PeopleEndpoint

api.add_resource(PeopleEndpoint, '/people', '/people/<id>')


if (__name__=='__main__'):
    logging.info("Hello, %s",__file__)
    