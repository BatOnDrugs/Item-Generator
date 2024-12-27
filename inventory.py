
from item_generator import item_generator
from item_classes import *



class Inventory():
    def __init__(self):
        self.carrying_capacity = 100
        self.current_load = 0
        self.storage = []
        self.slots = {}
    
    def add_to_inventory(self, item):
        if (self.current_load + item.weight) <= self.carrying_capacity:
            self.item = item
            self.storage.append(self.item)
            return True
        else:
            return False
        
            

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
        
        if slot_to_equip not in self.slots:
            self.slots[slot_to_equip] = item
            self.storage.remove(item)
        else:
            self.storage.append(self.slots[slot_to_equip])
            self.slots.pop(slot_to_equip)
    
    def equip_all_possible_items(self):
        for item in self.storage:
            print(item.name)
            inventory.equip_item()
    
    def check_stored_items(self):
        stored_items = "Items in bag:\n"
        for item in self.storage:
            if isinstance(item, Weapon):
                stored_items = f"{stored_items}{item.name}\nSpecial Power: {item.effect}\n------------\n"
            elif isinstance(item, Armour):
                stored_items = f"{stored_items}{item.armour_class} {item.name}\nSpecial Power: {item.effect}\n------------\n"
        return stored_items
    
    def check_equipped_items(self):
        equipped_items = []
        keys = [*self.slots]
        
        for item in keys:
                if self.slots[item]:
                    if isinstance(self.slots[item], Armour):
                        if self.slots[item].is_magical:
                            equipped_items.append(f"{item} slot:\n{self.slots[item].armour_class} {self.slots[item].name}\nSpecial Power: {self.slots[item].effect}")
                        else:
                            equipped_items.append(f"{item} slot:\n{self.slots[item].armour_class} {self.slots[item].name}")
                    elif isinstance(self.slots[item], Weapon):
                        if self.slots[item].is_magical:
                            equipped_items.append(f"{item} slot:\n{self.slots[item].name}\nSpecial Power: {self.slots[item].effect}")
                        else:
                            equipped_items.append(f"{item} slot:\n{self.slots[item].name}")
        if equipped_items:
            equipped_items_return = ")))Currently Equipped(((\n"
            for item in equipped_items:
                equipped_items_return = f"{equipped_items_return}{item}\n----------------------\n"
            return equipped_items_return
        else:
            return "No items equipped"
    
    #def drop_item(self, item):


def add_n_items_to_inventory(inventory, n):
    for i in range(n):
        item = item_generator()
        if inventory.add_to_inventory(item):
            continue
        else:
            print("Can't carry any more items")
            break
    




inventory = Inventory()
add_n_items_to_inventory(inventory, 5)
inventory.equip_all_possible_items()
print(inventory.check_stored_items())
print(inventory.check_equipped_items())

            
