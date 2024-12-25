import random

with open("weapon_names.md", "r") as content:
    weapon_names_list = content.read().split("\n")

def weapon_name_generator(weapon_type):
    weapon_name = random.choice(weapon_names_list)
    return f"{weapon_type} of {weapon_name}"

print(weapon_name_generator("Sword"))