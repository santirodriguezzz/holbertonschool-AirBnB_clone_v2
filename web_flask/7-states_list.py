#!/usr/bin/python3
"""Start web application
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def app_teardown(exit):
    """Clean
    """
    storage.close()


@app.route('/states_list')
def states_list():
    """Render template
    """
    return render_template('7-states_list.html',states=storage.all('state'))




if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
