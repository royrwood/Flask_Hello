#!/usr/bin/env python


# Configure logging

import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s", datefmt="%Y/%m/%d %H:%M:%S")


# Pull in the actual Flask app

logging.info("Importing hello.app")

from hello.app import app, api


if __name__ == '__main__':
    logging.info("Checking for WINGDB_ACTIVE")
    
    from os import environ
    
    if 'WINGDB_ACTIVE' in environ:
        logging.info("Disabling Flask debugging")
        app.debug = False
    else:
        logging.info("Flask debugging left enabled")
    
    
    # Run the Flask app
    
    logging.info("Running main app")
    
    # app.run(host='0.0.0.0', port=8888, use_reloader=True)
    app.run(host='0.0.0.0', port=8888, use_reloader=False)
