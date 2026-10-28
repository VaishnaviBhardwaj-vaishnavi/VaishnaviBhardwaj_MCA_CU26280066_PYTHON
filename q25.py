import csv

with open("students.csv", "a", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Rahul", 78])

print("Record added successfully.")