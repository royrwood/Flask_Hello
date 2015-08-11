from __future__ import print_function
import sys

print("sys.path = {}".format(sys.path))

from hello.app import app


if __name__ == '__main__':
    print("Checking for WINGDB_ACTIVE")
    
    from os import environ
    
    if 'WINGDB_ACTIVE' in environ:
        print("Disabling Flask debugging")
        app.debug = False
    else:
        print("Flask debugging left enabled")
    
    app.run(host='0.0.0.0', port=8888, use_reloader=True)
