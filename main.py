"""
Main file of flask example application.
"""

import sqlite3

import flask

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = flask.Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route("/")
def index():
    """Display index page"""
    return flask.render_template("/index.html")


@app.route("/login/")
def login():
        return flask.render_template("/login.html")


@app.errorhandler(404)
def not_found(error):
        """Display friendly error message"""
        print(error)
        return flask.render_template("error_404.html", msg=error)


if __name__ == '__main__':
    connect_db()
    app.run(debug=True, port=8080)

