from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError, CommandParser
from pokeapp.models import Pokemon, Stat, Evolution
import requests

POKE_API: str = "https://pokeapi.co/api/v2/"


def clean_db() -> None:
    Pokemon.objects.all().delete()
    print("Database rows deleted!")

def fetch_pokemon(name: str, chain_id: int) -> Pokemon:
    try:
        endpoint: str = f"pokemon/{name}/"
        response: dict = requests.get(POKE_API+endpoint).json()
        pokemon: Pokemon = Pokemon(
            poke_id=response["id"],
            name=response["name"],
            height=response["height"],
            weight=response["weight"],
            evo_chain=chain_id
        )
        pokemon.save()
        print(f"Pokemon {pokemon.name} saved.")
        for item in response["stats"]:
            stat: Stat = Stat(
                name=item["stat"]["name"],
                base_stat=item["base_stat"],
                effort=item["effort"],
                pokemon=pokemon
            )
            stat.save()
            print(f"Stat {stat.name} saved.")
    except:
        raise CommandError("Error fetching Pokemon")
    return pokemon


def fetch_evolution(id_: int) -> None:
    try:
        endpoint: str = f"evolution-chain/{id_}/"
        response: dict = requests.get(POKE_API+endpoint).json()
        chain_id: int = response["id"]
        print(f"Chain_id: {chain_id}")
        chain: dict = response["chain"]
        while chain:
            name: str = chain["species"]["name"]
            evo_details = chain["evolution_details"]
            type_: str = "Evolution" if evo_details else "Preevolution"
            pokemon: Pokemon = fetch_pokemon(name, chain_id)
            evolution: Evolution = Evolution(
                evo_id=response["id"],
                name=name,
                evo_type=type_,
                evo_chain=chain_id
            )
            evolution.save()
            print(f"Evolution: {evolution.name} saved.")
            chain = chain["evolves_to"][0] if chain["evolves_to"] else {}
    except:
        raise CommandError("Error fetching Evolution")

class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('chain_id', type=int)
    
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        clean_db()
        try:
            fetch_evolution(options['chain_id'])
            self.stdout.write(self.style.SUCCESS("Data stored succesfuly!"))
        except:
            raise CommandError("Error fetching data from Poke API.")
