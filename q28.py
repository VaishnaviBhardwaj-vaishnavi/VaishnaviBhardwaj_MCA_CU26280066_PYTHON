import csv

with open("students.csv", "r") as f:
    r = csv.DictReader(f)
    students = list(r)

if students:
    topper = max(students, key=lambda x: float(x["Marks"]))
    print("Name:", topper["Name"])
    print("Highest Marks:", topper["Marks"])
else:
    print("No student records found.")