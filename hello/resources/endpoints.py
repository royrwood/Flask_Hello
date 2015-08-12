import logging

import flask
from flask_restful import Resource

from hello.models.people import People


LOGGER = logging.getLogger(__name__)


class PeopleEndpoint(Resource):
    
    # Test with: curl -X GET -H "Accept: application/json" http://localhost:8888/people
    
    def get(self,**kwargs):
        LOGGER.info("Getting list of People")
        
        result = {}
        
        for i,p in enumerate(People.query.all()):
            LOGGER.debug("Found a People = %s",str(p))
            result[str(i)] = str(p)

        LOGGER.info("Returning list of People")
        
        return result
    
    
    # Test with: curl -X POST -H "Content-Type: application/json" -d '{ "test":"data","foo":"bar" }' http://localhost:8888/people
    
    def post(self,id=None,**kwargs):
        LOGGER.info("Received POST call with id=%s", id)
        
        try:
            json_data = flask.request.get_json()
            LOGGER.info("Parsed incoming JSON: %s", json_data)
        
        except:
            LOGGER.info("Could not parse incoming JSON data")
        
        
        return { "id": id }

    
if (__name__ == '__main__'):
    LOGGER.info("Hello, %s",__file__)
    