from Location import Location
from Item import Item


def delete(locations, row, shelf, bin, item_id, item_name):
    for location in locations:
        if location.row == row and location.shelf == shelf and location.bin == bin:
            for item in location.items:
                if item.id == item_id and item.name == item_name:
                    location.items.remove(item)
                    print(f"Item '{item_name}' with ID '{item_id}' successfully deleted from location:")
                    location.print_out()
                    return
            print(f"No item with name '{item_name}' and ID '{item_id}' found in location:")
            location.print_out()
            return
    print(f"No location found matching row '{row}', shelf '{shelf}', and bin '{bin}'.")
