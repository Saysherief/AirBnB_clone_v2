#!/usr/bin/python3
""" Flask web Application """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Function that routes '/':display 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Function that routes '/hbnb':display 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Function that routes '/c/<text>':display 'C' followed by the value of
    the text variable (replace underscore _ symbols with a space )"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """ Function that routes '/python/<text>':display 'Python' followed by the
    value of the text variable (replace underscore _ symbols with a space )"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """ Function that routes '/number/<n>':display '<n> is number'"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
