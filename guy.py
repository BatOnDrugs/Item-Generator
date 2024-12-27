from inventory import Inventory
from item_classes import Weapon, Armour

class Guy():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        self.inventory = Inventory(self.strength)

    def prepare_for_battle(self, num_items):
        self.inventory.add_n_items_to_inventory(num_items)
        print(f"Added {num_items} items to inventory!")
        self.inventory.sort_storage()
        print(self.inventory.check_stored_items())
        self.inventory.equip_all_possible_items()
        print(self.inventory.check_equipped_items())
        self.modify_health()
        
        

    def modify_health(self):
        for item in self.inventory._used_slots:
            if isinstance(self.inventory.slots[item], Weapon):
                self.strength += self.inventory.slots[item].dmg
            elif isinstance(self.inventory.slots[item], Armour):
                self.health += self.inventory.slots[item].defense
        
        

guy1 = Guy(100, 100)
print(guy1.prepare_for_battle(5))