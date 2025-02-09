#!/usr/bin/python3
'''module: 5-number_template
demonstrating basic flask functionality @author: @medjarraya ''' 
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello, HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<wisdom>', strict_slashes=False)
def c_text(wisdom):
    wisdom = wisdom.replace("_", " ")
    return 'C {}'.format(wisdom)


@app.route('/python/', strict_slashes=False)
def python_default():
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_test(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
