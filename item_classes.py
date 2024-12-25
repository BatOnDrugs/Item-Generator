class Weapon():
    def __init__(self, type, name, rarity, damage, attack_speed, dps, weight, dmg_type, is_magical = False):
        self.type = type
        self.rarity = rarity
        self.dmg = damage
        self.attack_speed = attack_speed
        self.dps = damage * attack_speed
        self.weight = weight
        self.dmg_type = dmg_type
        self.is_magical = is_magical
        self.special_power = ""

class Armour():
    def __init__(self, armour_piece, rarity, armour_class, defense, weight, is_magical = False):
        self.armour_piece = armour_piece
        self.rarity = rarity
        self.armour_class = armour_class
        self.defense = defense
        self.weight = weight
        self.is_magical = False
        self.special_power = ""



