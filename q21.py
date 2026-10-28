import csv

with open("students.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Name", "Marks"])
    w.writerow(["Aman", 85])
    w.writerow(["Riya", 92])

print("CSV file created.")