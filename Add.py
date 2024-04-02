from Location import Location
from Item import Item

# get all item inputs
item_name, item_id, item_quantity, item_weight = input("Enter item name, id, quantity, and weight all separated by spaces: ").split()

# create item
new_item = Item(item_name, item_id, item_quantity, item_weight)

# get location inputs
location_row, location_shelf, location_bin = input("Enter location row, shelf, and bin all separated by spaces: ").split()

# create location
new_location = Location(location_row, location_shelf, location_bin)

# display new Item and Location data
new_item.print_out()
new_location.print_out()