import os
from collections import defaultdict
from problems.utils.load_files import load_files

def inventory_system(inventory):
    grouping = {}
    item_quantities = defaultdict(int)
    most_valuable_item = {"item": "", "unit_price": 0, "owner": ""}

    total_values = {}

    for char in inventory:
        char_name   = char["name"]
        inventory   = char["inventory"]

        total_inventory_value = 0

        for item in inventory:
            item_name   = item["item"]
            quantity    = item["quantity"]
            unit_price  = item["unit_price"]

            total_inventory_value += quantity * unit_price

            item_quantities[item_name] += quantity

            if unit_price > most_valuable_item["unit_price"]:
                most_valuable_item = {
                    "item": item_name,
                    "unit_price": unit_price,
                    "owner": char_name
                }

        grouping[char_name] = {
            "total_inventory_value": total_inventory_value            
        }
        total_values[char_name] = total_inventory_value
    
    richest_character = max(total_values, key=total_values.get)
    most_common_item = max(item_quantities, key=item_quantities.get)
    most_common_quantity = item_quantities[most_common_item]

    grouping["summary"] = {
        "richest_character": richest_character,
        "most_common_item": { "item": most_common_item, "quantity": most_common_quantity },
        "most_valuable_item": most_valuable_item
    }

    return grouping

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file_path = os.path.join(path, "inventory.json")
    inventory = load_files(file_path)
    result = inventory_system(inventory)
    print(result)