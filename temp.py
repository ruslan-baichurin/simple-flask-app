import requests
from dataclasses import dataclass


@dataclass
class Pokemon:
    name: str
    id: int
    color: str
    egg_groups: list
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


pokemon = []
for i in range(1, 11):
    pok = get_pokemon(i)
    pokemon.append(pok)
