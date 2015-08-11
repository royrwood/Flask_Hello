import logging
import datetime

from hello.app import flask_SQA


# Interesting-- looks like SQA supports automatic setting of the timestamp....
# date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class People(flask_SQA.Model):
    __tablename__ = "people"
    
    id = flask_SQA.Column(flask_SQA.Integer, primary_key=True)
    firstname = flask_SQA.Column(flask_SQA.String)
    lastname = flask_SQA.Column(flask_SQA.String)
    tstamp = flask_SQA.Column(flask_SQA.TIMESTAMP)

    def __init__(self, firstname, lastname, tstamp = datetime.datetime.utcnow()):
        self.firstname = firstname
        self.lastname = lastname
        self.tstamp = tstamp

    def __repr__(self):
        return "<People: id={}, firstname={}, lastname={}, tstamp={}>".format(self.id, self.firstname, self.lastname, self.tstamp)
    
    
if (__name__ == '__main__'):
    logging.info("Hello, %s",__file__)
    
##    for i,p in enumerate(People.query.all()):
##        print("{}: {}".format(i, p))
        