from Location import Location
from Item import Item


def check_inventory(locations, row, shelf, bin):
    found_location = None
    for location in locations:
        if location.row == row and location.shelf == shelf and location.bin == bin:
            found_location = location
            break

    if found_location:
        print(f"Inventory at location {row}, {shelf}, {bin}:")
        print("Items at this location:")
        for item in found_location.items:
            item.print_out()
            print()
    else:
        print(f"No items found at location {row}, {shelf}, {bin}.")
