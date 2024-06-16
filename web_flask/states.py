#!/usr/bin/python3
"""
This module starts a simple Flask web application.

The web application listens on 0.0.0.0, port 5000 and has the following route:
    /: display "Hello HBNB!"

"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/v1/states", strict_slashes=False)
def states():
    data = [
        {
            "__class__": "State",
            "created_at": "2019-05-10T00:39:27.032802",
            "id": "7512f664-4951-4231-8de9-b18d940cc912",
            "name": "California",
            "updated_at": "2019-05-10T00:39:27.032965",
        },
        {
            "__class__": "State",
            "created_at": "2019-05-10T00:39:36.021219",
            "id": "b25625c8-8a7a-4c1f-8afc-257bf9f76bc8",
            "name": "Arizona",
            "updated_at": "2019-05-10T00:39:36.021281",
        },
    ]

    return jsonify(data)


@app.route("/", strict_slashes=False)
def index():
    """
    Route handler for the root URL.

    Returns:
        str: A welcome message "Hello HBNB!".
    """

    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
