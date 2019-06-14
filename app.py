from flask import Flask, render_template, request
import requests
import json

BASE_URL = 'http://swapi.co/api/'
PLANET_URL = BASE_URL + 'planets/'
SHIPS_URL = BASE_URL + 'starships/'
FILM_URL = BASE_URL + 'films/'
PEOPLE_URL = BASE_URL + 'people/'
BASE_URL_GQL = 'https://swapi-graphql-integracion-t3.herokuapp.com'

QUERY_FILMS = '''query {
allFilms {
  edges {
    node {
      id
      title
      episodeID
      director
      producers
      releaseDate
    }
  }
}
}'''


def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.

    request = requests.post(BASE_URL_GQL, json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))



app = Flask(__name__)


@app.route('/')
def index():
    result = run_query(QUERY_FILMS)['data']['allFilms']['edges']
    print(type(result))
    context = {
        "films": result,
    }
    return render_template("index.html", **context)

@app.route('/film/<path:path>')
def film(path):
    print(path)
    query = '''query {
film(id: "%s") {
id
episodeID
title
releaseDate
director
producers
openingCrawl
characterConnection {
characters {
name
id
}
}
planetConnection{
    planets{
      id
      name
    }
  }
  starshipConnection{
    starships{
      id
      name

    }
  }
}
}'''
    query = query % (path)
    result = run_query(query)
    context = {
        "response": result['data']['film'],
    }
    return render_template('film.html',**context)

@app.route('/starship/<path:path>')
def starship(path):
    query = '''query {
starship(id: "%s") {
  id
  model
  name
  costInCredits
  cargoCapacity
  manufacturers
  length
  maxAtmospheringSpeed
  crew
  passengers
  consumables
  MGLT
  hyperdriveRating
  starshipClass
  filmConnection {
    films
    {
      title
      id
    }
  }
  pilotConnection {
    pilots{
      name
      id
    }
  }
}
}'''
    query = query % (path)
    result = run_query(query)

    context = {
        "response": result['data']['starship'],

    }
    return render_template('starship.html',**context)

@app.route('/people/<path:path>')
def people(path):
    query = '''query {
person(id: "%s") {
  id
  name
  mass
  birthYear
  height
  eyeColor
  skinColor
  hairColor
  homeworld {
    id
    name
  }
  filmConnection {
    films{
      id
      title
    }
  }
  starshipConnection{
    starships{
      id
      name
    }
  }


}
}'''
    query = query % (path)
    result = run_query(query)

    context = {
        "response": result['data']['person']
    }
    return render_template('character.html',**context)


@app.route('/planet/<path:path>')
def planet(path):
    query = '''query {
planet(id: "%s") {
  id
  name
  orbitalPeriod
  rotationPeriod
  diameter
  climates
  surfaceWater
  terrains
  gravity
  population
  filmConnection{
    films{
      title
      id
    }
  }
  residentConnection{
    residents{
      id
      name
    }
  }
}
}'''
    query = query % (path)
    result = run_query(query)

    context = {
        "response": result['data']['planet'],

    }
    return render_template('planet.html',**context)

if __name__ == '__main__':

    app.run()
