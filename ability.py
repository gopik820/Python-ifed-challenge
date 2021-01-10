import requests
def ability(name):
    url = "http://pokeapi.co/api/v2/pokemon/"+name+"/"
    data = requests.get(url).json()
    abilitly=[]
    for i in data["abilities"]:
        abilitly.append(i['ability']['name'])
    return abilitly
    