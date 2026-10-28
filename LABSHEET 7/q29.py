import csv

name = input("Enter student name: ").strip().lower()
found = False

with open("students.csv", "r") as f:
    r = csv.DictReader(f)

    for row in r:
        if row["Name"].strip().lower() == name:
            print(row)
            found = True

if not found:
    print("Student not found.")