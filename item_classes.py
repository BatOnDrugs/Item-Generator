class Weapon():
    def __init__(self, name, rarity, damage, attack_speed, dps, weight, dmg_type, is_magical = False):
        self.rarity = rarity
        self.dmg = damage
        self.attack_speed = attack_speed
        self.dps = damage * attack_speed
        self.weight = weight
        self.dmg_type = dmg_type
        self.is_magical = is_magical

class Armour():
    def __init__(self, rarity, armour_class, defense, weight, is_magical = False):
        self.rarity = rarity
        self.armour_class = armour_class
        self.defense = defense
        self.weight = weight
        self.is_magical = False

