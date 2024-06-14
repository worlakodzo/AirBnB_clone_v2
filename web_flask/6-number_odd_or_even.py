#!/usr/bin/python3
"""
This module starts a simple Flask web application.

The web application listens on 0.0.0.0, port 5000 and has the following route:
    /: display "Hello HBNB!"

"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb_route():
    """
    Route handler for the root URL.

    Returns:
        str: A welcome message "Hello HBNB!".
    """

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    Route handler for the root URL.

    Returns:
        str: A welcome message "Hello HBNB!".
    """

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text="is cool"):
    """
    Route handler for the root URL.

    Returns:
        str: A welcome message "C".
    """
    text = text.replace("_", " ")
    return f'C {text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """
    Route handler for the root URL.

    Returns:
        str: A welcome message "Python ".
    """

    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Route handler for the root URL.

    Returns:
        a number.
    """

    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """
    Route handler for the root URL.

    Returns:
        Render a number".
    """

    return render_template('5-number.html', num_text=n)


@app.route('/airbnb-dynamic/number_odd_or_even/<int:n>', strict_slashes=False)
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route handler for the root URL.

    Returns:
        Render a number".
    """

    odd_or_even = "even" if n % 2 == 0 else "odd"
    num_text = f"{n} is {odd_or_even}"
    
    return render_template('6-number_odd_or_even.html', num_text=num_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
