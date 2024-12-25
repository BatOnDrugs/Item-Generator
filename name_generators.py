import random

with open("text_files/weapon_names.md", "r") as content:
    weapon_names_list = content.read().split("\n")

with open("text_files/armour_names.md", "r") as content:
    armour_names_list = content.read().split("\n")

def weapon_name_generator(weapon_type):
    weapon_name = random.choice(weapon_names_list)
    return f"{weapon_type} of {weapon_name}"

def armour_name_generator(armour_piece):
    armour_name = random.choice(armour_names_list)
    return f"{armour_piece} of {armour_name}"



