from item_classes import*
from name_generators import*
from special_power_generator import *
from stats_generator import *
import random

with open("text_files/weapon_types.md", "r") as content:
    weapon_types = content.read().split("\n")
with open("text_files/armour_pieces.md", "r") as content:
    armour_types = content.read().split("\n")

item_types = ["weapon", "armour"]
rarities = ["common", "uncommon", "rare", "very rare", "ultra rare", "legendary", "mythical"]
armour_classes = ["Cloth", "Light", "Medium", "Heavy"]

def item_generator():
    item_type = random.choice(item_types)
    rarity = "".join(random.choices(rarities, weights = (60, 40, 30, 20, 10, 5, 1), k=1))
    # what i need for weapon class: weapon_type, name, rarity, weapon_stats_dict, effect, is_magical
    if item_type == "weapon":
        weapon_type = random.choice(weapon_types)
        weapon_stats = weapon_stats_generator(rarity, weapon_type)
        magical = is_magical(rarity)
        if magical == True:
            weapon_name = weapon_name_generator(weapon_type)
            effect = weapon_power_picker()
            weapon = Weapon(weapon_type, weapon_name, rarity, weapon_stats, effect, magical)
        else:
            weapon_name = weapon_type
            weapon = Weapon(weapon_type, weapon_name, rarity, weapon_stats)
        return weapon

    # what i need for armour class:   armour_piece, name, rarity, armour_class, armour_stats_dict, effect, is_magical 
    elif item_type == "armour":
        armour_piece = random.choice(armour_types)
        armour_class = random.choice(armour_classes)    
        armour_stats = armour_stats_generator(rarity, armour_piece, armour_class)
        magical = is_magical(rarity)
        if magical == True:
            armour_name = armour_name_generator(armour_piece) 
            effect = armour_power_picker()
            armour = Armour(armour_piece, armour_name, rarity, armour_class, armour_stats, effect, magical)
        else:
            armour_name = armour_piece
            armour = Armour(armour_piece, armour_name, rarity, armour_class, armour_stats)
        return armour

        

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
if isinstance(item_one, Weapon):
    if item_one.weapon_type == "Axe":
        prefix = "An"
    else:
        prefix = "A"
    print(f"""you found...
{prefix} {item_one.name}!
{item_one.rarity}
It deals {item_one.dmg} damage, and it's speed is {item_one.attack_speed}, in total thats {item_one.dps} damage per second!
It has a range of {item_one.range} and weighs {item_one.weight} of whatever units makes sense!
Special power: {item_one.effect}
Value: {item_one.value} gold
It has been added to your inventory!""")
    
elif isinstance(item_one, Armour):
    if item_one.armour_piece == "Helmet" or item_one.armour_piece == "Chestpiece":
        prefix_one = "A "
        prefix_two = "It has"
    else:
        prefix_one = ""
        prefix_two = "They have"
    
    print(f"""You found...
{prefix_one}{item_one.armour_class} {item_one.name}!
{item_one.rarity}
{prefix_two} {item_one.defense} defense and a weight of {item_one.weight} of whatever unit makes sense!
Special power: {item_one.effect}
Value: {item_one.value} gold
{prefix_two} been added to your inventory!""")
    

        

