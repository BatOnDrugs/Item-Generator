from item_classes import*
from name_generators import*
from special_power_generator import *
from stats_generator import *
import random

with open("weapon_types.md", "r") as content:
    weapon_types = content.read().split("\n")

item_types = ["weapon"]
rarities = ["common", "uncommon", "rare", "very rare", "ultra rare", "legendary", "mythical"]
# note to self, what i need for weapon class: weapon_type, name, rarity, weapon_stats_dict, effect, is_magical
def item_generator():
    item_type = random.choice(item_types)
    rarity = "".join(random.choices(rarities, weights = (60, 40, 30, 20, 10, 5, 1), k=1))
    if item_type == "weapon":
        weapon_type = random.choice(weapon_types)
        weapon_name = weapon_name_generator(weapon_type)
        weapon_stats = weapon_stats_generator(rarity, weapon_type)
        magical = is_magical(rarity)
        if magical == True:
            effect = weapon_power_picker()
            weapon = Weapon(weapon_type, weapon_name, rarity, weapon_stats, effect, magical)
        else:
            weapon = Weapon(weapon_type, weapon_name, rarity, weapon_stats)
        return weapon

        
    else:
        print("".join(rarity))

def is_magical(rarity):
    options = [True, False]
    if rarity == "common":
        return False
    elif rarity == "uncommon":
        return False
    elif rarity == "rare":
        return (random.choices(options, weights =(15, 85), k=1))[0]
    elif rarity == "very rare":
        return (random.choices(options, weights =(25, 75), k=1))[0]
    elif rarity == "ultra rare":
        return (random.choices(options, weights =(40, 60), k=1))[0]
    elif rarity == "legendary":
        return random.choice(options)
    elif rarity == "mythical":
        return True

item_one = item_generator()
print(f"""you found a {item_one.name}, it's a {item_one.rarity} item.
It deals {item_one.dmg} damage, and it's speed is {item_one.attack_speed}, in total thats {item_one.dps} damage per second!
It has a range of {item_one.range} and weighs {item_one.weight} of whatever units makes sense!
It {item_one.effect}!""")


        

