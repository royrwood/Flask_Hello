# Flask_Hello

This is just a simple Flask application.

It demonstrates how to structure a Flask-REST app in a reasonable way, and how to use SQLAlchemy in the app.

The general structure is:

<pre>
.
├── hello
│   ├── app.py
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   └── people.py
│   └── resources
│       ├── endpoints.py
│       └── __init__.py
└── run.py
</pre>
