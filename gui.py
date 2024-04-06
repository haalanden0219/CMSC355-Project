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
    item_name = add_item_name_entry.get()
    item_id = add_item_id_entry.get()
    item_quantity = add_item_quantity_entry.get()
    item_weight = add_item_weight_entry.get()

    new_item = Item(item_name, item_id, item_quantity, item_weight)
    new_item.print_out()

    warehouse_object[counter].items.append(new_item)
    print(warehouse_object[counter].items)
    item_add_success = f"{item_name} is succesfully saved"
    messagebox.showinfo("Success", item_add_success)

def delete_item_button_clicked():
    print("delete button pressed")

def print_location_button_clicked():
    print("delete button pressed")


global warehouse_object
warehouse_object = [Location(1, 1, 1), Location(1, 1, 2)]

root = tk.Tk()
root.title("Warehouse Inventory system")
root.geometry("1200x1200")

#Button Creation
bin_search_button = tk.Button(root, text="Search Bin", command=bin_search_button_clicked)
add_item_button = tk.Button(root, text="Add Item to Bin", command=add_item_button_clicked)
delete_item_button = tk.Button(root, text="Delete Item", command= delete_item_button_clicked)
print_location_button = tk.Button(root, text="Print Location", command= print_location_button_clicked)


#bin_search entry creation
bin_search_name_entry = tk.Entry(root)
bin_search_id_entry = tk.Entry(root)

#add_item entry creation
add_item_name_entry = tk.Entry(root)
add_item_id_entry = tk.Entry(root)
add_item_quantity_entry = tk.Entry(root)
add_item_weight_entry = tk.Entry(root)

#delete_item entry creation
delete_item_name_entry = tk.Entry(root)
delete_item_id_entry = tk.Entry(root)


#bin_search label creation
bin_search_name_label = tk.Label(root, text="Item Name:")
bin_search_id_label = tk.Label(root, text="Item ID:")

#add_item label creation
add_item_name_label = tk.Label(root, text="Item Name:")
add_item_id_label = tk.Label(root, text="Item ID:")
add_item_quantity_label = tk.Label(root, text="Item Quantity:")
add_item_weight_label = tk.Label(root, text="Item Weight:")

#delete_item label creation
delete_item_name_label = tk.Label(root, text="Item Name:")
delete_item_id_label = tk.Label(root, text="Item ID:")

#buttons layout
bin_search_button.place( x = 300 , y = 300 , width = 100)
add_item_button.place(x = 300 , y = 350 , width=100)
delete_item_button.place(x = 300 , y = 400 , width=100)
print_location_button.place(x = 300 , y = 450 , width=100)


#bin search layout
bin_search_name_label.place(x = 400 , y = 300 , width = 100)
bin_search_name_entry.place(x = 500 , y = 300 , width = 100)
bin_search_id_label.place(x = 600 , y = 300 , width = 100)
bin_search_id_entry.place(x = 700 , y = 300 , width = 100)

#add item layout
add_item_name_label.place(x = 400, y = 350 , width=100)
add_item_name_entry.place(x = 500, y = 350 , width=100)
add_item_id_label.place(x = 600, y = 350 , width=100)
add_item_id_entry.place(x = 700, y = 350 , width=100)
add_item_quantity_label.place(x = 800, y = 350 , width=100)
add_item_quantity_entry.place(x = 900, y = 350 , width=100)
add_item_weight_label.place(x = 1000, y = 350 , width=100)
add_item_weight_entry.place(x = 1100, y = 350 , width=100)

#delete item layout
delete_item_name_label.place(x = 400, y = 400 , width=100)
delete_item_name_entry.place(x = 500, y = 400 , width=100)
delete_item_id_label.place(x = 600, y = 400 , width=100)
delete_item_id_entry.place(x = 700, y = 400 , width=100)

root.mainloop()
