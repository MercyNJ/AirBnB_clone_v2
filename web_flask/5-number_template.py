#!/usr/bin/python3
"""A Script that starts a Flask web application """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """print given message"""
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Prints hbnb"""
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Displays C then value of text var"""
    text = text.replace('_', ' ')
    return ('C {}'.format(text))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_txt(text='is cool'):
    """
    Displays python then value of var text.
    Default value is is cool.
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_num(n):
    """Display n is a num if its an int"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_num_template(n):
    """Displays a HTML pg with H1 tag with num n"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
