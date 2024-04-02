from Location import Location
from Item import Item


# warehouse is input list of locations, name is the name of item we are looking for, key is the ID
def search(warehouse, name, key):
    items = []
    flag = 0
    for location in warehouse:
        for item in location.items:
            if item.id == key:
                if item.name == name:
                    items.append(location)
                    flag = 1

    print(f"Items with name '{name}' and ID '{key}' found:")
    for location in items:
        print("Location(s):")
        location.print_out()
        print()
    if flag != 1:
        print("No item found with that name and ID")
        return
    return items
