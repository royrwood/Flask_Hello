# Configure logging

import logging

rootLogger = logging.getLogger()
rootLogger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s','%Y/%m/%d %H:%M:%S')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
rootLogger.addHandler(handler)

logging.info("This is a test")


# Add routes to Flask app/api

from hello.app import app, api
from hello.resources.endpoints import PeopleEndpoint

api.add_resource(PeopleEndpoint, '/people', '/people/<id>')



if __name__ == '__main__':
    logging.info("Checking for WINGDB_ACTIVE")
    
    from os import environ
    
    if 'WINGDB_ACTIVE' in environ:
        logging.info("Disabling Flask debugging")
        app.debug = False
    else:
        logging.info("Flask debugging left enabled")
    
    
    # Run the Flask app
    
    # app.run(host='0.0.0.0', port=8888, use_reloader=True)
    app.run(host='0.0.0.0', port=8888, use_reloader=False)
