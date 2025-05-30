import os, json

def control_automatic(products):
    grouping = {}
    to_restock = 0
    total_cost = 0.0
    for product in products:
        p = product["product"]
        stock = product["stock"]
        min_level = product["min_level"]
        ideal_level = product["ideal_level"]
        unit_price = product["unit_price"]

        if stock < min_level:
            status = "Repor"
            ideal_count = ideal_level - stock
            cost = round(ideal_count * unit_price, 2)
            to_restock += 1
            total_cost += cost
        else:
            status = "OK"
            ideal_count = 0
            cost = 0.0

        grouping[p] = {
            "status": status,
            "missing": ideal_count,
            "cost": cost
        }

    grouping["summary"] = {
        "products_to_restock": to_restock,
        "total_cost": total_cost
    }
    return grouping

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file_path = os.path.join(path, "products.json")
    with open(file_path, "r") as f:
        products = json.load(f)
    result = control_automatic(products)
    print(result)