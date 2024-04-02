from Location import Location
from Item import Item


# warehouse is input list of locations, name is the name of item we are looking for, key is the ID
def search(warehouse, name, key):
    items = []
    for key_item in warehouse.items:
        if key_item.id == key:
            if key_item.name == name:
                items.append(key_item)
    return items
