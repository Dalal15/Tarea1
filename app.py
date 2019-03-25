from flask import Flask, render_template, request
import requests
import json

BASE_URL = 'http://swapi.co/api/'
PLANET_URL = BASE_URL + 'planets/'
SHIPS_URL = BASE_URL + 'starships/'
FILM_URL = BASE_URL + 'films/'
PEOPLE_URL = BASE_URL + 'people/'

def get_all(search):
    json_planet = requests.get(PLANET_URL).json()
    json_star = requests.get(SHIPS_URL).json()
    json_film = requests.get(FILM_URL).json()
    json_people = requests.get(PEOPLE_URL).json()

    data = dict()
    lista_planet = []
    lista_people = []
    lista_film = []
    lista_star = []

    #Buscar en planetas
    while json_planet['next']:

        for planet in json_planet['results']:
            for value in planet.values():
                if search in str(value):
                    print("encontrado")
                    lista_planet.append(planet)
                    data['planets'] = lista_planet
                    break


        json_planet = requests.get(json_planet['next']).json()

    for planet in json_planet['results']:
        for value in planet.values():
            if search in str(value):
                print("encontrado")
                lista_planet.append(planet)
                data['planets'] = lista_planet
                break

    #Buscar en personas
    while json_people['next']:

        for people in json_people['results']:

            for value in people.values():
                if search in str(value):
                    print("encontrado")
                    lista_people.append(people)
                    data['people'] = lista_people
                    break


        json_people = requests.get(json_people['next']).json()

    for people in json_people['results']:
        for value in people.values():
            if search in str(value):
                print("encontrado")
                lista_people.append(people)
                data['people'] = lista_people
                break

    #Buscar en ships
    while json_star['next']:

        for ship in json_star['results']:
            for value in ship.values():

                if search in str(value):

                    lista_star.append(ship)
                    data['ships'] = lista_star
                    break


        json_star = requests.get(json_star['next']).json()

    for ship in json_star['results']:
        for value in ship.values():
            if search in str(value):
                print("encontrado")
                lista_star.append(ship)
                data['ships'] = lista_star
                break

    #Buscar en peliculas
    while json_film['next']:

        for film in json_film['results']:
            for value in film.values():

                if search in str(value):

                    lista_film.append(film)
                    data['films'] = lista_film
                    break


        json_film = requests.get(json_film['next']).json()

    for film in json_film['results']:
        for value in film.values():
            if search in str(value):
                print("encontrado")
                lista_film.append(film)
                data['films'] = lista_film

    return data

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

@app.route('/search' , methods=['POST'])
def search():

    response = request.form['searching']

    data = get_all(response)

    context = {
        "response": response,
        "data": data,
    }
    return render_template('search.html',**context)

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
