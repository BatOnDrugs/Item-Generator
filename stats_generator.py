import random

def weapon_stats_generator(rarity, weapon_type): #returns a dictionary of weapon stats in this format: {"damage":float, "attack speed":float, "weapon range":float, "weight":float}
    stats_dict = {}
    base_dmg = 0.0
    base_speed = 1
    base_range = 1
    base_weight = 1
    if rarity == "common":
        base_dmg = random.randint(10, 20)
    elif rarity == "uncommon":
        base_dmg = random.randint(18, 28)
    elif rarity == "rare":
        base_dmg = random.randint(28, 40)
    elif rarity == "very rare":
        base_dmg = random.randint(35, 45)
    elif rarity == "ultra rare":
        base_dmg = random.randint(45, 50)
    elif rarity == "legendary":
        base_dmg = random.randint(50, 65)
    elif rarity == "mythical":
        base_dmg = random.randint(70, 100)
    else:
        raise Exception("unknown rarity")

    if weapon_type == "Sword": # mid range stats
        damage_modifier = 1        
        speed_modifier = 1
        range_modifier = 1
        weight_modifier = 1        
    elif weapon_type == "Axe": # heavy with higher damage
        damage_modifier = 1.3       
        speed_modifier = 2
        range_modifier = 1
        weight_modifier = 1.2 
    elif weapon_type == "Spear": #mid damage with high range but lower speed
        damage_modifier = 1
        speed_modifier = 1.3
        range_modifier = 1.5
        weight_modifier = 1
    elif weapon_type == "Hammer": # heavy with high damage and very low speed
        damage_modifier = 1.5
        speed_modifier = 3
        range_modifier = 1
        weight_modifier = 1.3
    elif weapon_type == "Dagger": # light and fast with low damage and range
        damage_modifier = 0.8
        speed_modifier = .6
        range_modifier = 0.5
        weight_modifier = 0.5
       
    stats_dict["damage"] = round(base_dmg * (random.random()+0.1*damage_modifier), 1)
    stats_dict["attack speed"] = round(base_speed / speed_modifier, 1)
    stats_dict["weapon range"] = round(base_range * range_modifier, 1)
    stats_dict["weight"] = round(base_weight * weight_modifier, 1)

   
    return stats_dict

def armour_stats_generator(rarity, armour_piece, armour_class):
    stats_dict = {}
    base_def = 0.0
    if rarity == "common":
        base_def = random.randint(10, 20)
    elif rarity == "uncommon":
        base_def = random.randint(18, 28)
    elif rarity == "rare":
        base_def = random.randint(28, 40)
    elif rarity == "very rare":
        base_def = random.randint(35, 45)
    elif rarity == "ultra rare":
        base_def = random.randint(45, 50)
    elif rarity == "legendary":
        base_def = random.randint(50, 65)
    elif rarity == "mythical":
        base_def = random.randint(70, 100)
    else:
        raise Exception("unknown rarity")
    if armour_class == "Cloth":
        stats_dict["defense"] = 0
        stats_dict["weight"] = 0
        return stats_dict
    elif armour_class == "Light":
        base_def *= 0.8
    elif armour_class == "Heavy":
        base_def *= 1.3

    if armour_piece == "Helmet":
        stats_dict["defense"] = round(base_def * 0.9, 1)
        stats_dict["weight"] = round(2 * base_def * 0.1, 1)
    elif armour_piece == "Chestpiece":
        stats_dict["defense"] = round(base_def, 1)
        stats_dict["weight"] = round(5 * base_def * 0.1, 1)
    elif armour_piece == "Greaves":
        stats_dict["defense"] = round(base_def * 0.7, 1)
        stats_dict["weight"] = round(1 * base_def * 0.1, 1)
    elif armour_piece == "Pants":
        stats_dict["defense"] = round(base_def, 1)
        stats_dict["weight"] = round(3 * base_def * 0.1, 1)
    elif armour_piece == "Boots":
        stats_dict["defense"] = round(base_def * 0.7 , 1)
        stats_dict["weight"] = round(1 * base_def * 0.1, 1)
    return stats_dict

    


