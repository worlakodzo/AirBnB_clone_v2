#!/usr/bin/python3
"""
This module starts a simple Flask web application.

The web application listens on 0.0.0.0, port 5000 and has the following route:
    /: display "Hello HBNB!"

"""
# pip install flake8
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL.

    Returns:
        str: A welcome message "Hello HBNB!".
    """

    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
