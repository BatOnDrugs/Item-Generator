import random

def weapon_stats_generator(rarity, weapon_type): #returns a dictionary of weapon stats in this format: {"damage":float, "attack speed":float, "weapon range":float, "weight":float}
    stats_dict = {}
    base_stats = 0.0
    if not rarity:
        raise Exception("rarity required")
    if rarity == "common":
        base_stats = random.randint(10, 20)
    elif rarity == "uncommon":
        base_stats = random.randint(18, 28)
    elif rarity == "rare":
        base_stats = random.randint(28, 40)
    elif rarity == "very rare":
        base_stats = random.randint(35, 45)
    elif rarity == "ultra rare":
        base_stats = random.randint(45, 50)
    elif rarity == "legendary":
        base_stats = random.randint(50, 65)
    elif rarity == "mythical":
        base_stats = random.randint(70, 100)
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
        
    stats_dict["damage"] = round(base_stats * (random.random()+0.1*damage_modifier), 2)
    stats_dict["attack speed"] = round(base_stats * (random.random()/speed_modifier), 2)
    stats_dict["weapon range"] = round(base_stats * (random.random())*range_modifier, 2)
    stats_dict["weight"] = round(base_stats * (random.random()/2)*weight_modifier, 2)

   
    return stats_dict

    


