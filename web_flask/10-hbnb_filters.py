#!/usr/bin/python3
"""
This a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters')
def hbnb_filters():
    """city objects"""
    cities = storage.all(City)
    states = storage.all(State)
    amenities = storage.all(Amenity)
    html_template = '10-hbnb_filters.html'
    return render_template(html_template,
                           cities=cities,
                           states=states,
                           amenities=amenities)


@app.teardown_appcontext
def storage_teardown(exception):
    """calls the close function on states"""
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
