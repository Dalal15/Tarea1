def route_id(url):
    return url[::-1].split('/')[1][::-1]

print(route_id("https://swapi.co/api/starships/15/"))
