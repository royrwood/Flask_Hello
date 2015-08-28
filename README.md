# Flask_Hello

This is just a simple Flask application.

It demonstrates how to structure a Flask-REST app in a reasonable way, and how to use SQLAlchemy in the app.

The general structure is:

<pre>
.
├── run.py
│
├── hello
│   ├── __init__.py
│   ├── app.py
│   ├── models
│   │   ├── __init__.py
│   │   └── people.py
│   └── resources
│       ├── __init__.py
│       └── endpoints.py
</pre>
