import logging
import datetime

from hello.app import flask_SQA


LOGGER = logging.getLogger(__name__)


class People(flask_SQA.Model):
    __tablename__ = "people"
    
    id = flask_SQA.Column(flask_SQA.Integer, primary_key=True)
    firstname = flask_SQA.Column(flask_SQA.String)
    lastname = flask_SQA.Column(flask_SQA.String)
    # tstamp = flask_SQA.Column(flask_SQA.TIMESTAMP)
    tstamp = flask_SQA.Column(flask_SQA.DateTime, default=flask_SQA.func.current_timestamp(), onupdate=flask_SQA.func.current_timestamp())

    def __init__(self, firstname, lastname, tstamp = datetime.datetime.utcnow()):
        self.firstname = firstname
        self.lastname = lastname
        self.tstamp = tstamp

    def __repr__(self):
        return "<People: id={}, firstname={}, lastname={}, tstamp={}>".format(self.id, self.firstname, self.lastname, self.tstamp)
    
    
if (__name__ == '__main__'):
    LOGGER.info("Hello, %s",__file__)
    
##    for i,p in enumerate(People.query.all()):
##        print("{}: {}".format(i, p))
        