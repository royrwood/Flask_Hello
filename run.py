#!/usr/bin/env python


# Configure logging

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] {%(name)s:%(lineno)d} %(levelname)s - %(message)s", datefmt="%Y/%m/%d %H:%M:%S")

LOGGER = logging.getLogger(__name__)


# Pull in the actual Flask app

LOGGER.info("Importing hello.app")

from hello.app import app


if __name__ == '__main__':
    LOGGER.info("Checking for WINGDB_ACTIVE")
    
    from os import environ
    
#    if 'WINGDB_ACTIVE' in environ:
#        LOGGER.info("Disabling Flask debugging")
#        app.debug = False
#    else:
#        LOGGER.info("Flask debugging left enabled")
    
    
    # Run the Flask app
    
    LOGGER.info("Running main app")
    
    # app.run(host='0.0.0.0', port=8888, use_reloader=True)
    app.run(host='0.0.0.0', port=8888, use_reloader=False)
