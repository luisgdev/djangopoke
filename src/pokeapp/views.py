from django.http import JsonResponse
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from .models import Pokemon, Stat, Evolution

# Create your views here.
def pokesearch(request, name):
    pokemon: Pokemon = Pokemon.objects.get(name=name)
    stats = []
    for item in Stat.objects.filter(pokemon=pokemon):
        stats.append(model_to_dict(item))
    evolutions = []
    for item in Evolution.objects.filter(evo_id=pokemon.evo_chain):
        evolutions.append(model_to_dict(item))
    response: dict = model_to_dict(pokemon)
    response["stats"] = stats
    response["evolutions"] = evolutions
    return JsonResponse(response)
