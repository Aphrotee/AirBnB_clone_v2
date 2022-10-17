#!/usr/bin/python3
"""
This a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route('/hbnb')
def hbnb():
    """city objects"""
    cities = storage.all(City)
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    html_template = '100-hbnb.html'
    return render_template(html_template,
                           cities=cities,
                           states=states,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def storage_teardown(exception):
    """calls the close function on states"""
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
