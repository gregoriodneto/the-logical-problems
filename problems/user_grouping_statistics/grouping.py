import json, os

def grouping(users):  
    grouping_countries = {}  

    for user in users:
        country = user["country"]

        if country in grouping_countries:
            grouping_countries[country]["total_users"] += 1
            grouping_countries[country]["total_age"] += user["age"] 
            grouping_countries[country]["total_purchases"] += sum(user["purchases"])
        else:
            grouping_countries[country] = {
                "total_users": 1,
                "total_age": user["age"],
                "total_purchases": sum(user["purchases"])
            }

    for country, data in grouping_countries.items():
        data["average_age"] = round(data["total_age"] / data["total_users"], 2)
        del data["total_age"]

    return grouping_countries

if __name__  == "__main__":
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "users.json")
    try:
        with open(file_path, "r") as users_file:
            users = json.load(users_file)
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")

    group = grouping(users)
    print(group)