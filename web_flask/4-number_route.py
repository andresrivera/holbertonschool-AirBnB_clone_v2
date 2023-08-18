#!/usr/bin/python3
"""Import Modules"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Main Route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Route C"""
    text_with_spaces = text.replace('_', ' ')
    return f"C {text_with_spaces}"


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Route Python"""
    # text_with_spaces = text.replace('_', ' ')
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """number route, return if only is an integer"""
    return f"{n} is a number"

"""Entry Point"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
