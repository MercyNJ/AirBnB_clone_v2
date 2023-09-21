#!/usr/bin/python3
"""A Script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """print given message"""
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Prints hbnb"""
    return ('HBNB')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=None)
