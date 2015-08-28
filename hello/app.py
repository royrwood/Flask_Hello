import logging

from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy


LOGGER = logging.getLogger(__name__)


# Create our Flask app and REST API
#  Note that we need to create 'app' before we import our endpoints since they import the data models,
#  and the data models import and refer to app.  This circular reference works as long as we define
#  app before importing the endpoints and models!

LOGGER.info("Creating Flask app and api")

app = Flask(__name__)
api = Api(app)


# Configure database access

LOGGER.info("Configuring database connectivity")

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://rrwood:rrwood!@localhost/helloflask"
flask_SQA = SQLAlchemy(app)


# Route resources

LOGGER.info("Configuring REST endpoints and routes")

# Since 'app' is created above, it is safe to import the endpoint code.  This endpoint code in-turn
# imports 'app' from this file in a case of circular includes; however, since we have defined 'app'
# before we start the circular include, we are okay...

from hello.resources.endpoints import PeopleEndpoint

api.add_resource(PeopleEndpoint, '/people', '/people/<id>')


if (__name__=='__main__'):
    LOGGER.info("Hello, %s",__file__)
    