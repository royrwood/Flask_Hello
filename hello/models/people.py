from __future__ import print_function

print("--> people.py")

import datetime

# import sys
# print("sys.path = {}".format(sys.path))

print("--> people.py: import hello.app before")
from hello.app import flask_SQA
print("--> people.py: import hello.app before")


class People(flask_SQA.Model):
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
    
##    new_people = People("Peter", "Harrison")
##    flask_SQA.session.add(new_people)
##    flask_SQA.session.commit()
    
    for i,p in enumerate(People.query.all()):
        print("{}: {}".format(i, p))