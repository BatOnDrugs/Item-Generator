import random
import json
with open("data/item_data.json", "r") as item_data:
    data = json.load(item_data)

weapon_effects_list = data["weapon_effects"]
armour_effects_list = data["armour_effects"]

def weapon_power_picker():
    return random.choice(weapon_effects_list)



def armour_power_picker():
    return random.choice(armour_effects_list)



