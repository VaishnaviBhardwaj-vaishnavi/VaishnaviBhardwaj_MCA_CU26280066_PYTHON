import csv

with open("students.csv", "r") as f:
    rows = list(csv.reader(f))

if rows:
    print("Rows excluding header:", len(rows) - 1)
    print("Columns:", len(rows[0]))
else:
    print("CSV file is empty.")