import requests 
import json
from bs4 import BeautifulSoup

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
poke_data = response.json()
print(f"{(poke_data["name"])}")
print("Abilities are  : ")
print(poke_data["abilities"][0]["ability"]["name"])
print(poke_data["abilities"][1]["ability"]["name"])
print(f" {(poke_data["weight"])} lbs")

def fetch_pokemon_data():
    b_response= requests.get("https://pokeapi.co/api/v2/pokemon/bulbasaur")
    poke_data_b = b_response.json()
    print(f"{(poke_data_b["name"])}")
    print("It's two main abilities are  : ")
    print(poke_data_b["abilities"][0]["ability"]["name"])
    print(poke_data_b["abilities"][1]["ability"]["name"])
    print(f"{(poke_data_b["weight"])} lbs")
  
    c_response = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
    poke_data_c = c_response.json()
    print(f"Name :  {(poke_data_c["name"])}")
    print("It's two main abilities are  : ")
    print(poke_data_c["abilities"][0]["ability"]["name"])
    print(poke_data_c["abilities"][1]["ability"]["name"])
    print(f"Weight : {(poke_data_c["weight"])} lbs")
    
    p_response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    poke_data_p = p_response.json()
    print(f"Name :  {(poke_data_p["name"])}")
    print("It's two main abilities are  : ")
    print(poke_data_p["abilities"][0]["ability"]["name"])
    print(poke_data_p["abilities"][1]["ability"]["name"])
    print(f"Weight: {(poke_data["weight"])} lbs")

fetch_pokemon_data()



def calculate_average_weight():
    p_response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu") 
    poke_data_p = p_response.json()
    b_response = requests.get("https://pokeapi.co/api/v2/pokemon/bulbasaur")
    poke_data_b = b_response.json()
    c_response = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
    poke_data_c = c_response.json()

    pikachu = (poke_data_p["weight"])
    bulbasaur = (poke_data_b["weight"])
    charmander = (poke_data_c["weight"])

    average = (pikachu+bulbasaur+charmander)/3
    print(f"Average weight:   {average}")

calculate_average_weight()










