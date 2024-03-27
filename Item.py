class Item:
    def __init__(self, name, id, quantity, weight):
        self.name = name
        self.id = id
        self.quantity = quantity
        self.weight = weight
    def myFunc(self):
        print("Item is " + self.name + ", with ID " + self.id + ", with quantity  " + self.quantity + ",  with weight " + self.weight + ".")

