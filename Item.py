class Item:
    def __init__(self, name, id, quantity, weight):
        self.name = name
        self.id = id
        self.quantity = quantity
        self.weight = weight
    def print_out(self):
        print("Item Name: " + self.name + "\nID: " + self.id + "\nQuantity: " + self.quantity + "\nWeight: " + self.weight)

