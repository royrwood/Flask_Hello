# Flask_Hello

This is just a simple Flask application.

It demonstrates how to structure a Flask-REST app in a reasonable way, and how to use SQLAlchemy in the app.

The general structure is:

<pre>
.
├── hello
│   ├── app.py
│   ├── app.pyc
│   ├── create_db.sql
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── models
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── people.py
│   │   └── people.pyc
│   └── resources
│       ├── endpoints.py
│       ├── endpoints.pyc
│       ├── __init__.py
│       └── __init__.pyc
└── run.py
</pre>
