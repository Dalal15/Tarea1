from flask import Flask, render_template
import requests

BASE_URL = 'http://swapi.co/api/'
PLANET_URL = BASE_URL + 'planets/'
SHIPS_URL = BASE_URL + 'starships/'
FILM_URL = BASE_URL + 'films/'
PEOPLE_URL = BASE_URL + 'people/'

def get_planets():

    json_response = requests.get(PLANET_URL).json()
    data = dict()

    while json_response['next']:

        for planet in json_response['results']:
            data[planet['url']] = planet['name']

        json_response = requests.get(json_response['next']).json()

    for planet in json_response['results']:
        data[planet['url']] = planet['name']

    return data

def get_films():
    '''
    Get json film info
    :return: json response
    '''
    json_response = requests.get(FILM_URL).json()
    return json_response

def get_people():
    '''
    Get json film info
    :return: json response
    '''
    json_response = requests.get(PEOPLE_URL).json()


    data = dict()

    while json_response['next']:

        for person in json_response['results']:
            data[person['url']] = person['name']

        json_response = requests.get(json_response['next']).json()

    for person in json_response['results']:
        data[person['url']] = person['name']



    return data

def get_starship():

    json_response = requests.get(SHIPS_URL).json()

    data = dict()

    while json_response['next']:

        for ship in json_response['results']:
            data[ship['url']] = ship['name']

        json_response = requests.get(json_response['next']).json()

    for ship in json_response['results']:
        data[ship['url']] = ship['name']

    return data

def get_films_data():

    json_response = requests.get(FILM_URL).json()

    data = dict()

    while json_response['next']:

        for film in json_response['results']:
            data[film['url']] = film['title']

        json_response = requests.get(json_response['next']).json()

    for film in json_response['results']:
        data[film['url']] = film['title']

    return data


def get_url(url):

    json_response = requests.get(url).json()
    return json_response

def route_id(url):
    return url[::-1].split('/')[1][::-1]



app = Flask(__name__)


@app.route('/')
def index():
    context = {
        "films": get_films()['results'],
    }
    return render_template("index.html", **context)

@app.route('/film/<path:path>')
def film(path):
    films = get_films_data()

    for film in films.keys():
        if path == route_id(film):
            response = get_url(film)

    context = {
        "response": response,
        "people": get_people(),
        "ships": get_starship(),
        "planets": get_planets(),
    }
    return render_template('film.html',**context)

@app.route('/starship/<path:path>')
def starship(path):
    ships = get_starship()

    for ship in ships.keys():
        if path == route_id(ship):
            response = get_url(ship)

    context = {
        "response": response,
        "people": get_people(),
        "ships": get_starship(),
        "planets": get_planets(),
        "films": get_films_data(),
    }
    return render_template('starship.html',**context)

@app.route('/people/<path:path>')
def people(path):
    people = get_people()

    for char in people.keys():

        if path == route_id(char):
            response = get_url(char)

    context = {
        "response": response,
        "people": get_people(),
        "ships": get_starship(),
        "planets": get_planets(),
        "films": get_films_data(),
    }
    return render_template('character.html',**context)

@app.route('/planet/<path:path>')
def planet(path):
    planets = get_planets()

    for plan in planets.keys():

        if path == route_id(plan):
            response = get_url(plan)

    context = {
        "response": response,
        "people": get_people(),
        "ships": get_starship(),
        "planets": get_planets(),
        "films": get_films_data(),
    }
    return render_template('planet.html',**context)

if __name__ == '__main__':

    app.run()
