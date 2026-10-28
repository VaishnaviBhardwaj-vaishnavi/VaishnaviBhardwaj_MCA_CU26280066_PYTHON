import csv

marks = []

with open("students.csv", "r") as f:
    r = csv.DictReader(f)

    for row in r:
        marks.append(float(row["Marks"]))

if marks:
    print("Average:", sum(marks) / len(marks))
else:
    print("No numeric data found.")