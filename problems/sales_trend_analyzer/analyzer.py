import os
from collections import defaultdict
from problems.utils.load_files import load_files

def analyzer(sales):
    clients = defaultdict(float)
    products = defaultdict(int)
    dates = defaultdict(float)
    total_revenue = 0

    for sale in sales:
        client      = sale["client"]
        quantity    = sale["quantity"]
        unit_price  = sale["unit_price"]
        product     = sale["product"]
        date        = sale["date"]

        revenue = quantity * unit_price
        total_revenue += revenue

        clients[client] += revenue
        products[product] += quantity
        dates[date] += revenue

    most_sold_product = max(products, key=products.get)
    busiest_day       = max(dates, key=dates.get)    
    top_client        = max(clients, key=clients.get)

    grouping = {
        "clients": dict(clients),
        "most_sold_product": most_sold_product,
        "busiest_day": busiest_day,
        "summary": {
            "total_revenue": total_revenue,
            "top_client": top_client,
            "top_product": most_sold_product
        }
    }

    return grouping

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    file_path = os.path.join(current_path, "sales.json")
    sales = load_files(file_path)
    result = analyzer(sales)
    print(result)