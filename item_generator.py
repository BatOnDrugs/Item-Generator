from item_classes import*
from name_generators import*
from special_power_generator import *
import random

with open("weapon_types.md", "r") as content:
    weapon_types = content.read().split("\n")

item_types = ["weapon", "armour"]
rarities = ["common", "uncommon", "rare", "very rare", "ultra rare", "legendary", "mythical"]

def item_generator():
    item_type = random.choice(item_types)
    rarity = random.choices(rarities, weights = (60, 40, 30, 20, 10, 5, 1), k=1)
    if item_type == "weapon":
        weapon = 
    else:
        print("".join(rarity))
item_generator()

        

