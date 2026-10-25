import random
import requests

API_URL = "https://pokeapi.co/api/v2/pokemon/"
POKEMON_LIST = [
    "pikachu",
    "bulbasaur",
    "charmander",
    "squirtle",
    "eevee",
]


def get_pokemon(name):
    """Get a Pokémon's details from PokeAPI."""
    try:
        response = requests.get(f"{API_URL}{name.lower().strip()}", timeout=10)

        
        if response.status_code == 404:
            print(f'"{name}" was not found in PokeAPI.')
            return None

        response.raise_for_status()
        data = response.json()

        return {
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
        }

    except requests.exceptions.RequestException as error:
        print("Network error. Please check your internet connection and try again.")
        print(f"Details: {error}")
        return None
    except (KeyError, ValueError):
        print("The API returned data that could not be processed.")
        return None


def play_game():
    print("=== WHO'S THAT POKÉMON? ===")
    print("Guess the Pokémon using its height and weight!")
    print("You have 3 attempts. Good luck!\n")

    
    pokemon_name = random.choice(POKEMON_LIST)
    pokemon = get_pokemon(pokemon_name)

    if pokemon is None:
        print("The game could not start. Please run it again later.")
        return

    print(f"Height: {pokemon['height']} decimeters")
    print(f"Weight: {pokemon['weight']} hectograms")
    print()

    attempts = 3

    while attempts > 0:
        guess = input(f"Attempt {4 - attempts}/3 — Pokémon name: ").strip().lower()

        if not guess:
            print("Please enter a Pokémon name.")
            continue

        
        guessed_pokemon = get_pokemon(guess)
        if guessed_pokemon is None:
            print("Please enter a valid Pokémon name. This does not use an attempt.\n")
            continue

        if guessed_pokemon["name"] == pokemon["name"]:
            print("Correct! You guessed the Pokémon!")
            return

        attempts -= 1
        if attempts > 0:
            print(f"Not quite! You have {attempts} attempt(s) left.\n")

    print(f"Game over! The correct Pokémon was {pokemon['name'].capitalize()}.")


if __name__ == "__main__":
    play_game()


