import os, json

def statistics(sales):
    grouping_category = {}

    for sale in sales:
        category = sale["category"]
        if category in grouping_category:
            grouping_category[category]["total_products_sold"] += sale["quantity"]
            grouping_category[category]["total_revenue"] += (sale["quantity"] * sale["price"])
        else:
            grouping_category[category] = {
                "total_products_sold": sale["quantity"],
                "total_revenue": sale["quantity"] * sale["price"]
            }

    for sale, data in grouping_category.items():
        data["average_price"] = round(data["total_revenue"] / data["total_products_sold"], 2)
        data["total_revenue"] = round(data["total_revenue"], 2)
        data["total_products_sold"] = round(data["total_products_sold"], 2)

    return grouping_category

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "sales.json")
    try:
        with open(file_path, "r") as f:
            sales = json.load(f)
    except FileNotFoundError:
        print("Arquivo não encontrado!")

    data = statistics(sales)
    print(data)