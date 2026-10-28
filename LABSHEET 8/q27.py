import sqlite3
import csv

con = sqlite3.connect("college.db")
cur = con.cursor()

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cur.execute("""
        INSERT INTO students (id, name, age, marks)
        VALUES (?, ?, ?, ?)
        """, (
            int(row["id"]),
            row["name"],
            int(row["age"]),
            float(row["marks"])
        ))

con.commit()
print("CSV data imported successfully!")
con.close()