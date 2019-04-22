#!/usr/bin/python3
"""
start a Flask web application
"""
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')
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


@app.route("/number_template/<int:n>")
def display_number_template(n):
    """
    display HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def display_number_odd_or_even(n):
    """
    display HTML page only if n is an integer
    """
    oe = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, odd_or_even=oe)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
