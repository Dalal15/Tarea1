from flask import Flask, render_template
import requests

BASE_URL = 'http://swapi.co/api/'
PLANET_URL = BASE_URL + 'planets/'
SHIPS_URL = BASE_URL + 'starships/'
FILM_URL = BASE_URL + 'films/'

def get_planet(planet_id):
    '''
    Get json planet info
    :param planet_id: string or integer number representing a planet
    :return: json response
    '''
    json_response = requests.get(PLANET_URL + str(planet_id)).json()
    return json_response

def get_films():
    '''
    Get json film info
    :return: json response
    '''
    json_response = requests.get(FILM_URL).json()
    return json_response

def get_ship(ship_id):
    '''
    Get json ship info
    :param ship_id: string or integer number representing a ship
    :return: json response
    '''
    json_response = requests.get(SHIPS_URL + str(ship_id)).json()
    return json_response


app = Flask(__name__)


@app.route('/')
def index():
    context = {
        "films": get_films()['results'],
    }
    return render_template("index.html", **context)

if __name__ == '__main__':
    port = int(os.environ.get('PORT'))
    app.run(host='0.0.0.0', port=port)
