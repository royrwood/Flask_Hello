import logging

import flask
from flask_restful import Resource

from hello.models.people import People


class PeopleEndpoint(Resource):
    
    # Test with: curl -X GET -H "Accept: application/json" http://localhost:8888/people
    
    def get(self,**kwargs):
        logging.info("Getting list of People")
        
        result = {}
        
        for i,p in enumerate(People.query.all()):
            logging.info("Found a People = %s",str(p))
            result[str(i)] = str(p)

        logging.info("Returning list of People")
        
        return result
    
    
    # Test with: curl -X POST -H "Content-Type: application/json" -d '{ "test":"data","foo":"bar" }' http://localhost:8888/people
    
    def post(self,id=None,**kwargs):
        logging.info("Received POST call with id=%s", id)
        
        try:
            json_data = flask.request.get_json()
            logging.info("Parsed incoming JSON: %s", json_data)
        
        except:
            logging.info("Could not parse incoming JSON data")
        
        
        return { "id": id }

    
if (__name__ == '__main__'):
    logging.info("Hello, %s",__file__)
    