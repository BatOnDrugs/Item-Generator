from inventory import Inventory
from item_classes import Weapon, Armour

class Guy():
    def __init__(self, health, strength, name):
        self.name = name
        self.health = health
        self.strength = strength
        self.inventory = Inventory(self.strength)

    def prepare_for_battle(self, num_items):
        self.inventory.add_n_items_to_inventory(num_items)
        print(f"Added {num_items} items to inventory!")
        self.inventory.sort_storage()
        self.inventory.equip_all_possible_items()
        print(self.inventory.check_equipped_items())
        self.modify_health()
        print(f"Current Health is {self.health}")
        print(f"Current strength is {self.strength}")
        
        

    def modify_health(self):
        for item in self.inventory._used_slots:
            if isinstance(self.inventory.slots[item], Weapon):
                self.strength += int(self.inventory.slots[item].dmg)
            elif isinstance(self.inventory.slots[item], Armour):
                self.health += int(self.inventory.slots[item].defense)

    def attack(self, other):
        print(f"{self.name} hit {other.name} for {self.strength} damage!")
        return other.get_hit(self)
    
    def get_hit(self, other):
        print(f"{self.name} got hit by {other.name} for {other.strength} damage!")
        self.health -= other.strength / 2
        print(f"{self.name} has {self.health} health left!")
        
        

guy1 = Guy(100, 10, "Jacob")
guy2 = Guy(100, 10, "Edward") 
guy1.prepare_for_battle(20)
guy2.prepare_for_battle(20)
guy1.attack(guy2)