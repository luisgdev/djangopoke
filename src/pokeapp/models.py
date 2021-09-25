from django.db import models

# Create your models here.
from typing import List
from django.db import models

# Create your models here.


class Pokemon(models.Model):
    """
    A Pokemon is a mystical creature that belongs to a fictional world, 
    designed and managed by the Japanese companies Nintendo, Game Freak 
    and Creatures.
    """
    poke_id = models.IntegerField()
    name = models.CharField(max_length=128)
    height = models.IntegerField()
    weight = models.IntegerField()
    evo_chain = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name


class Stat(models.Model):
    """
    Stats determine certain aspects of battles. Each Pokémon has a value for 
    each stat which grows as they gain levels and can be altered momentarily 
    by effects in battles.
    """
    name = models.CharField(max_length=64)
    base_stat = models.IntegerField()
    effort = models.IntegerField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Evolution(models.Model):
    """
    Evolution chains are essentially family trees. They start with the lowest 
    stage within a family and detail evolution conditions for each as well as 
    Pokémon they can evolve into up through the hierarchy.
    """
    evo_id = models.IntegerField()
    name = models.CharField(max_length=128)
    evo_type = models.CharField(max_length=64)
    evo_chain = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name
