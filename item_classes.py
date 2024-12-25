class Weapon():
    def __init__(self, weapon_type, name, rarity, weapon_stats_dict, dmg_type, is_magical = False):
        self.weapon_type = type
        self.rarity = rarity
        self.dmg = weapon_stats_dict["damage"]
        self.attack_speed = weapon_stats_dict["attack speed"]
        self.dps = self.dmg * self.attack_speed
        self.range = weapon_stats_dict["weapon range"]
        self.weight = weapon_stats_dict["weight"]
        self.dmg_type = dmg_type
        self.is_magical = is_magical
        self.special_power = ""

class Armour():
    def __init__(self, armour_piece, rarity, armour_class, armour_stats_dict, is_magical = False):
        self.armour_piece = armour_piece
        self.rarity = rarity
        self.armour_class = armour_class
        self.defense = armour_stats_dict["defense"]
        self.weight = armour_stats_dict["weight"]
        self.is_magical = False
        self.special_power = ""



