import random

with open("weapon_names.md", "r") as content:
    weapon_names_list = content.read().split("\n")

with open("armour_names.md", "r") as content:
    armour_names_list = content.read().split("\n")

def weapon_name_generator(weapon_type):
    weapon_name = random.choice(weapon_names_list)
    return f"{weapon_type} of {weapon_name}"

def armour_name_generator(armour_piece):
    armour_name = random.choice(armour_names_list)
    return f"{armour_piece} of {armour_name}"

print(armour_name_generator("Greaves"))

