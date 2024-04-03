class Location:
    def __init__(self, row, shelf, bin):
        self.row = row
        self.shelf = shelf
        self.bin = bin
        self.items = []
    def print_out(self):
        print("Row: " + str(self.row) + "\nShelf: " + str(self.shelf) + "\nBin: " + str(self.bin))

