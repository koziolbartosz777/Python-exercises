import requests

base_url = "https://pokeapi.co/api/v2/"

pokemon_name = "pikachu"

def get_pokemon_info(pokemon_name):
    full_url = f"{base_url}/pokemon/{pokemon_name}"
    response = requests.get(full_url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
        # print("Data retreived")
    else:
        print("Error in retrieving data")
    

pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Heigth: {pokemon_info["height"]}")
