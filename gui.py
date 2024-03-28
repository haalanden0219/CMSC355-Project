import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from Item import Item
from Location import Location

drop_down_menu_options = []

def bin_search_button_clicked():
    print("Will implement search function later")
    #bin_identifier = bin_search_textbox.get()
    #bin_success = f"{bin_identifier} is succesfully saved"
    #messagebox.showinfo("Success" , bin_success )

def add_item_button_clicked():
    item_name = item_name_entry.get()
    item_id = item_id_entry.get()
    item_quantity = item_quantity_entry.get()
    item_weight = item_weight_entry.get()
    new_item = Item(item_name, item_id, item_quantity, item_weight)
    new_item.print_out()
    new_location.items.append(new_item)
    print(new_location.items)
    item_add_success = f"{item_name} is succesfully saved"
    messagebox.showinfo("Success" , item_add_success )

global new_location 
new_location = Location("1", "1", "1")
new_location.print_out()

root = tk.Tk()
root.title("Warehouse Inventory system")
root.geometry("500x500")

bin_search_button = tk.Button(root, text="Search Bin", command=bin_search_button_clicked)
add_item_button = tk.Button(root, text="Add Item to Bin", command=add_item_button_clicked)

bin_search_textbox = tk.Entry(root)
item_name_entry = tk.Entry(root)
item_id_entry = tk.Entry(root)
item_quantity_entry = tk.Entry(root)
item_weight_entry = tk.Entry(root)
item_name_label = tk.Label(root, text="Item Name:")
item_id_label = tk.Label(root, text="Item ID:")
item_quantity_label = tk.Label(root, text="Item Quantity:")
item_weight_label = tk.Label(root, text="Item Weight:")
bin_search_button.pack(side=tk.TOP, padx=5, pady=5, anchor=tk.CENTER)
bin_search_textbox.pack(side=tk.TOP, padx=5, pady=5, anchor=tk.CENTER)

add_item_button.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.CENTER)

item_name_label.pack(side=tk.LEFT, padx=5, pady=5)
item_name_entry.pack(side=tk.LEFT, padx=5, pady=5)
item_id_label.pack(side=tk.LEFT, padx=5, pady=5)
item_id_entry.pack(side=tk.LEFT, padx=5, pady=5)
item_quantity_label.pack(side=tk.LEFT, padx=5, pady=5)
item_quantity_entry.pack(side=tk.LEFT, padx=5, pady=5)
item_weight_label.pack(side=tk.LEFT, padx=5, pady=5)
item_weight_entry.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
