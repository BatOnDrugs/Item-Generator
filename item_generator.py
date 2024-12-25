from item_classes import*
from name_generators import*
from special_power_generator import *
from stats_generator import *
import random

with open("weapon_types.md", "r") as content:
    weapon_types = content.read().split("\n")

item_types = ["weapon", "armour"]
rarities = ["common", "uncommon", "rare", "very rare", "ultra rare", "legendary", "mythical"]
# note to self, what i need for weapon class: weapon_type, name, rarity, weapon_stats_dict, dmg_type, is_magical
def item_generator():
    item_type = random.choice(item_types)
    rarity = random.choices(rarities, weights = (60, 40, 30, 20, 10, 5, 1), k=1)
    if item_type == "weapon":
        weapon_type = random.choice(weapon_types)
        weapon_name = weapon_name_generator(weapon_type)
        weapon_stats = weapon_stats_generator(rarity, weapon_type)

        
    else:
        print("".join(rarity))

def is_magical(rarity):
    options = [True, False]
    if rarity == "common":
        return False
    elif rarity == "uncommon":
        return False
    elif rarity == "rare":
        return (random.choices(options, weights =(5, 95), k=1))[0]
    elif rarity == "very rare":
        return (random.choices(options, weights =(5, 95), k=1))[0]
    elif rarity == "ultra rare":
        return (random.choices(options, weights =(25, 75), k=1))[0]
    elif rarity == "legendary":
        return random.choice(options)
    elif rarity == "mythical":
        return True


print(is_magical("legendary"))

        

