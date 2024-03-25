import tkinter as tk
from tkinter import messagebox

drop_down_menu_options = []

def bin_search_button_clicked():
    print("Will implement search function later")
    #bin_identifier = bin_search_textbox.get()
    #bin_success = f"{bin_identifier} is succesfully saved"
    #messagebox.showinfo("Success" , bin_success )

def add_item_button_clicked():
    bin_identifier = add_item_textbox.get()
    bin_success = f"{bin_identifier} is succesfully saved"
    global drop_down_menu_options
    drop_down_menu_options.append(bin_identifier)
    print(drop_down_menu_options)
    messagebox.showinfo("Success" , bin_success ) 

root = tk.Tk()
root.title("Warehouse Inventory system")
root.geometry("500x500")

#set a max size for better view ability
#create a drop down section for a quick search option

bin_search_button = tk.Button(root, text="Search Bin", command=bin_search_button_clicked)
add_item_button = tk.Button(root, text="Add Item to Bin", command=add_item_button_clicked)

bin_search_textbox = tk.Entry(root)
add_item_textbox = tk.Entry(root)

bin_search_button.pack(side=tk.TOP, padx=5, pady=5, anchor=tk.CENTER)
bin_search_textbox.pack(side=tk.TOP, padx=5, pady=5, anchor=tk.CENTER)
add_item_button.pack(side=tk.TOP, padx=5, pady=5, anchor=tk.CENTER)
add_item_textbox.pack(side=tk.TOP, padx=5, pady=5, anchor=tk.CENTER)

root.mainloop()
