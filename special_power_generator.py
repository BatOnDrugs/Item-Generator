import random

with open("weapon_effects.md", "r") as content:
    weapon_effects_list = content.read().split("\n")

with open("armour_effects.md", "r") as content:
    armour_effects_list = content.read().split("\n")

def weapon_power_picker():
    return random.choice(weapon_effects_list)



def armour_power_picker():
    return random.choice(armour_effects_list)



