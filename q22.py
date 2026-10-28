import csv

with open("students.csv", "r") as f:
    r = csv.reader(f)

    for row in r:
        print(row)