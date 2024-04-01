
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, bin_number):
        self.items[item_name] = bin_number

    def search_item(self, item_name):
        if item_name in self.items:
            return f"Item '{item_name}' is located in bin {self.items[item_name]}"
        else:
            return f"Item '{item_name}' not found in the warehouse."


# Test cases
def test_add_item():
    warehouse = Warehouse()
    warehouse.add_item("Chair", "A1")
    assert warehouse.items["Chair"] == "A1"
    print("Add item test passed.")


def test_search_item():
    warehouse = Warehouse()
    warehouse.add_item("Chair", "A1")
    warehouse.add_item("Table", "B2")
    assert warehouse.search_item("Chair") == "Item 'Chair' is located in bin A1"
    assert warehouse.search_item("Table") == "Item 'Table' is located in bin B2"
    assert warehouse.search_item("Lamp") == "Item 'Lamp' not found in the warehouse."
    print("Search item test passed.")


if __name__ == "__main__":
    test_add_item()
    test_search_item()
