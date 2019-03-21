from flask import Flask, render_template
from starwars import (get_films,
                      get_planet,

                      get_ship,)
app = Flask(__name__)


@app.route('/')
def index():
    context = {
        "films": get_films()['results'],
        "planet_name": get_planet(1)['name'],
        "ship_length": get_ship(3)['length'],
        "ship_name": get_ship(3)['name']
    }
    return render_template("index.html", **context)

if __name__ == '__main__':
    app.run()
