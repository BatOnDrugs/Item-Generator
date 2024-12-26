
from item_generator import item_generator
from item_classes import *



class Inventory():
    def __init__(self):
        self.storage = []
        self.slots = {"Head":[], "Chest":[], "Hands":[], "Legs":[], "Feet":[], "Weapon":[]}
    
    def add_to_inventory(self, item):
        self.item = item
        self.storage.append(self.item)

    def equip_item(self):
        if self.storage == []:
            return "No items in inventory"
        slot_to_equip = ""
        item = self.storage[0]
        if isinstance(item, Weapon):
            slot_to_equip = "Weapon"
        elif isinstance(item, Armour):
            if item.armour_piece == "Helmet":
                slot_to_equip = "Head"
            elif item.armour_piece == "Chestpiece":
                slot_to_equip = "Chest"
            elif item.armour_piece == "Greaves":
                slot_to_equip = "Hands"
            elif item.armour_piece == "Pants":
                slot_to_equip = "Legs"
            elif item.armour_piece == "Boots":
                slot_to_equip = "Feet"
        
        if self.slots[slot_to_equip] == []:
            self.slots[slot_to_equip] = item
            self.storage.remove(item)
        else:
            self.storage.append(self.slots[slot_to_equip])
            self.slots[slot_to_equip] == ""
    
    def equipped_items(self):
        

inventory = Inventory()   
item = item_generator()
inventory.add_to_inventory(item)
inventory.equip_item()
print(inventory.slots)
            
