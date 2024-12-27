import random
import json

with open("data/item_data.json", "r") as item_data:
    data = json.load(item_data)

weapon_names_list = data["weapon_names"]
armour_names_list = data["armour_names"]

def weapon_name_generator(weapon_type):
    weapon_name = random.choice(weapon_names_list)
    return f"{weapon_type} of {weapon_name}"

def armour_name_generator(armour_piece):
    armour_name = random.choice(armour_names_list)
    return f"{armour_piece} of {armour_name}"



