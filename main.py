"""
Main file of flask example application.
"""

import sqlite3

from flask import Flask

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    connect_db()
    app.run()
