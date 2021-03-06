#!/usr/bin/python3
"""
start a Flask web application
"""
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')
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


@app.route("/number/<int:n>")
def number(n):
    """
    display n is a number only if n is an integer
    """
    return '{} is a number'.format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """
    display HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
