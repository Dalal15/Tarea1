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
