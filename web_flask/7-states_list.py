#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

"""method para unir flask app con la palntilla de html (7-states_list.html)"""


@app.route("/states_list", strict_slashes=False)
def statelist():
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def removesql(exit):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
