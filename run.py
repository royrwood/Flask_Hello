from hello.app import app


if __name__ == '__main__':
    from os import environ
    
    if 'WINGDB_ACTIVE' in environ:
        app.debug = False
    
    app.run(host='0.0.0.0', port=8888, use_reloader=True)