#!/usr/bin/python3
"""
start a Flask web application
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """
    display Hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    display HBNB
    """
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """
    display C followed by the value of text variable
    """
    return 'C {}'.format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python(text="is cool"):
    """
    display Python followed by the value of text variable with default is cool
    """
    return 'Python {}'.format(text.replace("_", " "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
