
from item_generator import item_generator
from item_classes import *
from algs import bubble_sort_items


class Inventory():
    def __init__(self):
        self.carrying_capacity = 100
        self.current_load = 0
        self.storage = []
        self.slots = {}
        self._used_slots = []
    def add_to_inventory(self, item):
        if (self.current_load + item.weight) <= self.carrying_capacity:
            self.item = item
            self.storage.append(self.item)
            return True
        else:
            return False
        
            

    def equip_all_possible_items(self):
        items_to_equip = self.storage[:]
        for item in items_to_equip:
            self.equip_item(item)

    def equip_item(self, item):
        if not self.storage:
            return "No items in inventory"

        slot_to_equip = ""
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

        if slot_to_equip and slot_to_equip not in self.slots:
            # Equip the item if the slot is empty
            self.slots[slot_to_equip] = item
            self.storage.remove(item)
    
    def check_stored_items(self):
        stored_items = "Items in bag:\n"
        for item in self.storage:
            if isinstance(item, Weapon):
                stored_items = f"{stored_items}{item.name}\nSpecial Power: {item.effect}\nDamage: {item.dmg}\nSpecial Power: {item.effect}\n------------\n"
            elif isinstance(item, Armour):
                stored_items = f"{stored_items}{item.armour_class} {item.name}\nDefense: {item.defense}\nSpecial Power: {item.effect}\n------------\n"
        return stored_items
        
    def check_equipped_items(self):
        equipped_items = []
        self._used_slots = [*self.slots]
        
        for item in self._used_slots:
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
    
    def check_empty_slots(self):
        possible_slots = ("Head", "Chest", "Hands", "Legs", "Feet", "Weapon")
        empty_slots = list(possible_slots)
        if self._used_slots != []:
            for item in self._used_slots:
                empty_slots.remove(item)       
        return f"Empty Slots: {empty_slots}"
    
    def sort_storage(self, sort_by = "Unspecified"):   
        # make a list of armour pieces and a list of Weapons
        armour_in_storage = []
        weapons_in_storage = []
        for i in range(len(self.storage)):
            if isinstance(self.storage[i], Armour):
                armour_in_storage.append(self.storage[i])
            elif isinstance(self.storage[i], Weapon):
                weapons_in_storage.append(self.storage[i])
        
        
        if sort_by == "Unspecified":
            sort_by = "main stat" #will sort by defense for armour and damage for weapons

        armour_in_storage = bubble_sort_items(armour_in_storage, "Armour", sort_by)
        weapons_in_storage = bubble_sort_items(weapons_in_storage, "Weapons", sort_by)

        self.storage = armour_in_storage + weapons_in_storage
        return self.storage
        




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

print(inventory.check_stored_items())
inventory.sort_storage()
print(inventory.check_stored_items())



            
