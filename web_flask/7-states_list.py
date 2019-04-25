#!/usr/bin/python3
"""
start a Flask web application
"""
from flask import Flask, render_template, request, g
from models import storage
app = Flask(__name__, template_folder='templates', static_folder='static')
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


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """
    display HTML page only if n is an integer
    """
    oe = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, odd_or_even=oe)


@app.route("/states_list", methods=['GET', 'POST'])
def states_list():
    state_list = storage.all("State").values()
    return render_template('7-states_list.html',
                           state_list=state_list)


@app.teardown_appcontext
def teardown_db(error):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
