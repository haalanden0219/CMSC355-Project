from Location import Location
from Item import Item


# warehouse is input list of locations, name is the name of item we are looking for, key is the ID
def search(warehouse, name, key):
    items = []
    for location in warehouse:
        for item in location.items:
            if item.id == key:
                if item.name == name:
                    items.append(location)

    return items
