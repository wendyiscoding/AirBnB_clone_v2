#!/usr/bin/python3
"""
start a Flask web application
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def display_hello():
    """
    display Hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def display_hbnb():
    """
    display HBNB
    """
    return "HBNB"


@app.route("/c/<text>")
def display_c(text):
    """
    display C followed by the value of text variable
    """
    return 'C {}'.format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def display_python(text="is cool"):
    """
    display Python followed by the value of text variable with default is cool
    """
    return 'Python {}'.format(text.replace("_", " "))


@app.route("/number/<int:n>")
def display_number(n):
    """
    display n is a number only if n is an integer
    """
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
