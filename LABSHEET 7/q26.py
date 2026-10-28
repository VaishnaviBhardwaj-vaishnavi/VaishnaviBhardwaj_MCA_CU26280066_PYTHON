import csv

with open("students.csv", "r") as f1:
    data = list(csv.reader(f1))

with open("copy.csv", "w", newline="") as f2:
    w = csv.writer(f2)
    w.writerows(data)

print("CSV file copied.")