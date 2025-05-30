import os, json

def notes_students(notes):
    grouping = {}
    approved = 0
    failed = 0
    for note in notes:
        student = note["name"]
        average = round(sum(note["grades"]) / len(note["grades"]), 2)
        attendance = note["attendance"]        
        grouping[student] = {
            "average": average,
            "attendance": attendance,
            "status": "Approved" if average >= 7 and attendance >= 75 else "Failed"
        }
        approved += 1 if grouping[student]["status"] == "Approved" else 0
        failed += 1 if grouping[student]["status"] == "Failed" else 0
    grouping["summary"] = {
        "approved": approved,
        "failed": failed,
        "approved_percent": round((approved * 100) / len(notes), 2),
        "failed_percent": round((failed * 100) / len(notes),2)
    }
    return grouping

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file_path = os.path.join(path, "students.json")
    with open(file_path, "r") as f:
        notes = json.load(f)
    result = notes_students(notes)
    print(result)