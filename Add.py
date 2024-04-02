from Location import Location
from Item import Item
def add(new_item_name, new_item_id, new_item_quantity, new_item_weight, desired_location):
    new_item = Item(new_item_name, new_item_id, new_item_quantity, new_item_weight)
    desired_location.items.append(new_item)
    print("Item Added!")