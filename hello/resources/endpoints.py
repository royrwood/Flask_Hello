import logging

from flask_restful import Resource

logging.info("hello.models.people before")
from hello.models.people import People
logging.info("import hello.models.people after")


class PeopleEndpoint(Resource):
    def get(self,**kwargs):
        logging.info("Getting list of People")
        
        result = {}
        
        for i,p in enumerate(People.query.all()):
            logging.info("Found a People = %s",str(p))
            result[str(i)] = str(p)

        logging.info("Returning list of People")
        
        return result
    
    def post(self,id,**kwargs):
        logging.info("Received POST call with id={}", id)
        
        return "People.post(); id = %s".format(id)

    
if (__name__ == '__main__'):
    logging.info("Hello, %s",__file__)
    