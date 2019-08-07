import requests

from dataclasses import dataclass
from datetime import datetime
from flask import render_template, request
from program import app


@app.route('/')
@app.route('/index')
def index():
    time_now = str(datetime.today())
    return render_template('index.html', time_now=time_now)


@app.route('/chuck')
def chuck():
    joke = get_chuck_joke()
    return render_template('chuck.html', joke=joke)


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    pokemon = []
    # if request.method == 'POST' and 'pokecolor' in request.form:
    #     color = request.form.get('pokecolor')
    #     pokemons = get_pokemons(color)
    for i in range(1, 11):
        pok = get_pokemon(i)
        pokemon.append(pok)

    return render_template('pokemon.html', pokemon=pokemon)


def get_chuck_joke():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    data = r.json()

    return data['value']


@dataclass
class Pokemon:
    name: str
    id: int
    color: str
    # egg_groups: list
    habitat: str
    shape: str
    flavor_text: str


def get_pokemon(i: int):
    r = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + str(i))
    pokemon_data = r.json()

    name = pokemon_data['name']
    color = pokemon_data['color']['name']
    # eggs = [e['name'] for e in pokemon_data['egg_groups']]
    habitat = pokemon_data['habitat']['name']
    shape = pokemon_data['shape']['name']
    flavor_text = [t['flavor_text'] for t in pokemon_data['flavor_text_entries'] if t['language']['name'] == 'en']

    p = Pokemon(name, i, color, habitat, shape, flavor_text[0])
    print(p)
    return p
