import os, json

def notes_students(notes):
    grouping = {}
    for note in notes:
        student = note["name"]
        average = round(sum(note["grades"]) / len(note["grades"]), 2)
        attendance = note["attendance"]
        grouping[student] = {
            "average": average,
            "attendance": attendance,
            "status": "Approved" if average >= 7 and attendance >= 75 else "Failed"
        }
    return grouping

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file_path = os.path.join(path, "students.json")
    with open(file_path, "r") as f:
        notes = json.load(f)
    result = notes_students(notes)
    print(result)