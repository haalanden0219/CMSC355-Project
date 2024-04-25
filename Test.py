from Add import add
from Search import search
from Item import Item
from Location import Location
from Delete import delete
from Check_Inventory import check_inventory 
from update import update_item


def main():
    print("Testing the Add Item function:\n")
    print("Testing the Location function:\n")
    locations = []
    for row in range(1, 5):
        for shelf in range(1, 5):
            for bin in range(1, 5):
                locations.append(Location(f"Row {row}", f"Shelf {shelf}", f"Bin {bin}"))
    add("Box", "3301a", "35", "12", locations[30])
    add("Tape Rolls", "2931c", "5", "2", locations[63])
    print("Testing the Search function:\n")
    search(locations, "Box", "3301a")
    search(locations, "book", "3301a")

    print("Testing the Delete Item function:\n")
    # Delete item function call
    delete(locations, 5,1,2, "2931c","Tape Rolls")
    print("Testing the Check Location function:\n")
    # Check Location function call
    check_inventory(locations, 2,1,5)

    print("Testing Update Item function:\n")
    # Test modifying an item that is there
    # Test modifying an item that is not there
    

if __name__ == "__main__":
    main()
