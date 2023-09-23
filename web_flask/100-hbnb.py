#!/usr/bin/python3
"""
Starts a Flask web appl. Listens on 0.0.0.0  on port 5000.
Routes:*  /hbnb: Display the HTML page for hbnb home page.
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.place import Place
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays the HTML page for hbnb home page."""
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    states = storage.all(State)
    return render_template("100-hbnb.html",
                           amenities=amenities,
                           places=places,
                           states=states)


@app.teardown_appcontext
def teardown(excpt=None):
    """Closes the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    storage.reload()
    app.run(host='0.0.0.0', port=5000, debug=True)
