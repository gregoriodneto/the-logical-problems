import os, json

def temperature_recording(temps):
    grouping = {}
    for t in temps:
        city = t["city"]
        grouping[city] = {
            "average_temperature": round(sum(t["temperatures"]) / len(t["temperatures"]), 2),
            "highest_temperature": max(t["temperatures"]),
            "lowest_temperature": min(t["temperatures"]),
        }
    return grouping

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file_path = os.path.join(path, "temperatures.json")
    with open(file_path, "r") as f:
        temps = json.load(f)
    result = temperature_recording(temps)
    print(result)