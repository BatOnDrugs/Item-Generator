class Weapon():
    def __init__(self, weapon_type, name, rarity, weapon_stats_dict, effect = None, is_magical = False):
        self.name = name
        self.weapon_type = weapon_type
        self.rarity = rarity
        self.dmg = weapon_stats_dict["damage"]
        self.attack_speed = weapon_stats_dict["attack speed"]
        self.dps = round((self.dmg * self.attack_speed), 2)
        self.range = weapon_stats_dict["weapon range"]
        self.weight = weapon_stats_dict["weight"]
        self.effect = effect
        self.is_magical = is_magical
        self.special_power = ""
        self.value = self._get_value()

    def _get_value(self):
        if self.is_magical == True:
            multiplier = 2
        else:
            multiplier = 1
        self.value = int((100 + (self.dps*2)) * multiplier)
        return self.value
        

class Armour():
    def __init__(self, armour_piece, name, rarity, armour_class, armour_stats_dict, effect = None, is_magical = False):
        self.name = name
        self.armour_piece = armour_piece
        self.rarity = rarity
        self.armour_class = armour_class
        self.defense = armour_stats_dict["defense"]
        self.weight = armour_stats_dict["weight"]
        self.effect = effect
        self.is_magical = False
        self.value = self._get_value()

    def _get_value(self):
        if self.is_magical == True:
            multiplier = 2
        else:
            multiplier = 1
        self.value = int((100 + (self.defense*2)) * multiplier)
        return self.value
        



