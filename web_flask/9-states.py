#!/usr/bin/python3
"""
This a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states')
def states_list():
    """states objects"""
    states = storage.all(State)
    html_template = '9-states.html'
    return render_template(html_template, states=states)

@app.route('/states/<id>')
def states_list():
    """state object"""
    cities = storage.all(City)
    states = storage.all(State)
    html_template = '9-states.html'
    return render_template(html_template, states=states)


@app.teardown_appcontext
def storage_teardown(exception):
    """calls the close function on states"""
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
