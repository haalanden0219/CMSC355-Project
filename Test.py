from Add import add
from Search import search
from Item import Item
from Location import Location


def main():
    locations = []
    for row in range(1, 5):
        for shelf in range(1, 5):
            for bin in range(1, 5):
                locations.append(Location(f"Row {row}", f"Shelf {shelf}", f"Bin {bin}"))
    add("Box", "3301a", "35", "12", locations[30])
    add("Tape Rolls", "2931c", "5", "2", locations[63])
    search(locations, "Box", "3301a")
    search(locations, "book", "3301a")
#  print("Testing the Add Item function:\n")
#  print("Testing the Location function:\n")

if __name__ == "__main__":
    main()
