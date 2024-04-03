import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from Item import Item
from Location import Location
from Search_gui import search

drop_down_menu_options = []
counter = 0


def bin_search_button_clicked():
    search_item_name = bin_search_name_entry.get()
    search_item_id = bin_search_id_entry.get()
    searched_items_list = search(warehouse_object, search_item_name, search_item_id)
    for items_to_print in searched_items_list:
        print(items_to_print.print_out())


def add_item_button_clicked():
    global counter
    counter += 1
    item_name = item_name_entry.get()
    item_id = item_id_entry.get()
    item_quantity = item_quantity_entry.get()
    item_weight = item_weight_entry.get()

    new_item = Item(item_name, item_id, item_quantity, item_weight)
    new_item.print_out()

    warehouse_object[counter].items.append(new_item)
    print(warehouse_object[counter].items)
    item_add_success = f"{item_name} is succesfully saved"
    messagebox.showinfo("Success", item_add_success)


global warehouse_object
warehouse_object = [Location(1, 1, 1), Location(1, 1, 2)]

root = tk.Tk()
root.title("Warehouse Inventory system")
root.geometry("500x500")

bin_search_button = tk.Button(root, text="Search Bin", command=bin_search_button_clicked)
add_item_button = tk.Button(root, text="Add Item to Bin", command=add_item_button_clicked)

bin_search_name_entry = tk.Entry(root)
bin_search_id_entry = tk.Entry(root)

item_name_entry = tk.Entry(root)
item_id_entry = tk.Entry(root)
item_quantity_entry = tk.Entry(root)
item_weight_entry = tk.Entry(root)

bin_search_name_label = tk.Label(root, text="Item Name:")
bin_search_id_label = tk.Label(root, text="Item ID:")

item_name_label = tk.Label(root, text="Item Name:")
item_id_label = tk.Label(root, text="Item ID:")
item_quantity_label = tk.Label(root, text="Item Quantity:")
item_weight_label = tk.Label(root, text="Item Weight:")

bin_search_button.pack(side=tk.TOP, padx=5, pady=5, anchor=tk.CENTER)
add_item_button.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.CENTER)

bin_search_name_label.pack(side=tk.TOP, padx=5, pady=5, anchor=tk.CENTER)
bin_search_name_entry.pack(side=tk.TOP, padx=5, pady=5, anchor=tk.CENTER)
bin_search_id_label.pack(side=tk.TOP, padx=5, pady=5, anchor=tk.CENTER)
bin_search_id_entry.pack(side=tk.TOP, padx=5, pady=5, anchor=tk.CENTER)

item_name_label.pack(side=tk.LEFT, padx=5, pady=5)
item_name_entry.pack(side=tk.LEFT, padx=5, pady=5)
item_id_label.pack(side=tk.LEFT, padx=5, pady=5)
item_id_entry.pack(side=tk.LEFT, padx=5, pady=5)
item_quantity_label.pack(side=tk.LEFT, padx=5, pady=5)
item_quantity_entry.pack(side=tk.LEFT, padx=5, pady=5)
item_weight_label.pack(side=tk.LEFT, padx=5, pady=5)
item_weight_entry.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
