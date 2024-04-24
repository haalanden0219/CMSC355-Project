def update_item(locations, item_name, item_id, new_weight, new_quantity):
    for location in locations:
        for item in location.items:
            if item.name == item_name and item.id == item_id:
                item.weight = new_weight
                item.quantity = new_quantity
                print(f"Item '{item_name}' with ID '{item_id}' updated successfully:")
                item.print_out()
                return
    print(f"No item with name '{item_name}' and ID '{item_id}' found in any location.")